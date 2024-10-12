import os
import uuid
from typing import override

from langchain_text_splitters import RecursiveCharacterTextSplitter
from qdrant_client import QdrantClient
from qdrant_client.conversions.common_types import Distance
from qdrant_client.grpc import VectorParams, PointStruct
from qdrant_client.http.models import UpdateResult

from app.bot.api.ollama.impl.ollama import Ollama
from app.bot.api.pdf.base_pdf import BasePDFProcessor
from FlagEmbedding import BGEM3FlagModel
from pdfminer.high_level import extract_text

class PDFProcessor(BasePDFProcessor):
    def __init__(self, coll_name: str = 'test', qdrant_host: str = 'qdrant', qdrant_port: int = 6333):
        super().__init__(coll_name, qdrant_host, qdrant_port)
        self.encoder = BGEM3FlagModel('USER-bge-m3')
        self.qdrant_client = QdrantClient(qdrant_host, port=qdrant_port)
        self.coll_name = coll_name
        self.prompt_temp = '''Используй только следующий Контекст, чтобы кратко ответить на Вопрос в конце.
        Используй ТОЛЬКО Контекст для ответа. Если ты не знаешь ответа напиши "Ответ не найден". Не пытайся выдумывать ответ.
        
        ### Контекст ###
        {chunks_join}
        
        ### Вопрос ###
        {query}'''

    @override
    def get_emb(self, sentence: str) -> list:
        emb = self.encoder.encode(sentence)['dense_vecs']
        return emb

    @override
    def get_pdf_content(self, file_path: str) -> str:
        content = extract_text(file_path)
        return content

    @override
    def content_to_chunks(self, content: str, sep: list, chunk_size: int, chunk_overlap: int) -> list:
        text_splitter = RecursiveCharacterTextSplitter(
            separators=sep,
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
            length_function=len,
            is_separator_regex=False,
            add_start_index=False
        )
        chunks = text_splitter.split_text(content)
        return chunks

    @override
    def chunks_to_vecdb(self, chunks: list, embeddings: list) -> UpdateResult:
        points = []
        for i in range(len(chunks)):
            point = PointStruct(
                id=str(uuid.uuid4()),
                vector=embeddings[i],
                payload={'chunk': chunks[i]}
            )
            points.append(point)

        operation_info = self.qdrant_client.upsert(
            collection_name=self.coll_name,
            wait=True,
            points=points
        )

        return operation_info

    @override
    def vec_search(self, query: str, n_top_cos: int) -> list:
        query_emb = self.get_emb(query)

        search_result = self.qdrant_client.search(
            collection_name=self.coll_name,
            query_vector=query_emb,
            limit=n_top_cos,
            with_vectors=False
        )

        top_chunks = [x.payload['chunk'] for x in search_result]

        return top_chunks

    @override
    def get_prompt(self, top_chunks: list, query: str) -> str:
        chunks_join = '\n'.join(top_chunks)
        prompt = self.prompt_temp.format(chunks_join=chunks_join, query=query)
        return prompt

    @override
    async def llm_request(self, prompt: str) -> str:
        ollama = Ollama(prompt)
        await ollama.send_request()
        return ollama.get_formatted_response()

    @override
    def initialize_collection(self) -> None:
        self.qdrant_client.delete_collection(collection_name=self.coll_name)
        self.qdrant_client.create_collection(
            collection_name=self.coll_name,
            vectors_config=VectorParams(size=1024, distance=Distance.COSINE)
        )

    @override
    def process_pdf(self, file_path: str, sep: list, chunk_size: int, chunk_overlap: int) -> None:
        content = self.get_pdf_content(file_path)
        chunks = self.content_to_chunks(content, sep, chunk_size, chunk_overlap)
        embs = [self.get_emb(chunk) for chunk in chunks]
        self.chunks_to_vecdb(chunks, embs)

    @override
    async def query_pdf(self, query: str, n_top_cos: int) -> str:
        top_chunks = self.vec_search(query, n_top_cos)
        prompt = self.get_prompt(top_chunks, query)
        answer = await self.llm_request(prompt)
        return answer

    def load_all_documents(self, directory: str, sep: list, chunk_size: int, chunk_overlap: int) -> None:
        for root, _, files in os.walk(directory):
            for file in files:
                if file.endswith('.pdf'):
                    file_path = os.path.join(root, file)
                    self.process_pdf(file_path, sep, chunk_size, chunk_overlap)

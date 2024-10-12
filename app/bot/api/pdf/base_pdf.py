from abc import ABC, abstractmethod


class BasePDFProcessor(ABC):
    def __init__(self, coll_name: str, qdrant_host: str, qdrant_port: int):
        """
        Initialize the BasePDFProcessor class.

        :param coll_name: Name of the collection in Qdrant.
        :param qdrant_host: Host of the Qdrant server.
        :param qdrant_port: Port of the Qdrant server.
        """
        self.coll_name = coll_name
        self.qdrant_host = qdrant_host
        self.qdrant_port = qdrant_port

    @abstractmethod
    def get_emb(self, sentence: str) -> list:
        """
        Convert a sentence to a vector.

        :param sentence: The sentence to convert.
        :return: The vector representation of the sentence.
        """

    @abstractmethod
    def get_pdf_content(self, file_path: str) -> str:
        """
        Extract content from a PDF file.

        :param file_path: Path to the PDF file.
        :return: The extracted content as a string.
        """

    @abstractmethod
    def content_to_chunks(self, content: str, sep: list, chunk_size: int, chunk_overlap: int) -> list:
        """
        Split the content into chunks.

        :param content: The content to split.
        :param sep: List of separators.
        :param chunk_size: Size of each chunk.
        :param chunk_overlap: Overlap between chunks.
        :return: List of chunks.
        """

    @abstractmethod
    def chunks_to_vecdb(self, chunks: list, embs: list) -> dict:
        """
        Insert chunks and their vector representations into the vector database.

        :param chunks: List of chunks.
        :param embs: List of vector representations.
        :return: Operation info from the vector database.
        """

    @abstractmethod
    def vec_search(self, query: str, n_top_cos: int) -> list:
        """
        Search for chunks similar to the query.

        :param query: The query string.
        :param n_top_cos: Number of top results to return.
        :return: List of top chunks.
        """

    @abstractmethod
    def get_prompt(self, top_chunks: list, query: str) -> str:
        """
        Generate a prompt from the top chunks and query.

        :param top_chunks: List of top chunks.
        :param query: The query string.
        :return: The generated prompt.
        """

    @abstractmethod
    def llm_request(self, prompt: str) -> str:
        """
        Send a request to the LLM.

        :param prompt: The prompt to send.
        :return: The response from the LLM.
        """

    @abstractmethod
    def initialize_collection(self) -> None:
        """
        Initialize the collection in the vector database.

        :return: None
        """

    @abstractmethod
    def process_pdf(self, file_path: str, sep: list, chunk_size: int, chunk_overlap: int) -> None:
        """
        Process the PDF file and insert chunks into the vector database.

        :param file_path: Path to the PDF file.
        :param sep: List of separators.
        :param chunk_size: Size of each chunk.
        :param chunk_overlap: Overlap between chunks.
        :return: None
        """

    @abstractmethod
    def query_pdf(self, query: str, n_top_cos: int) -> str:
        """
        Query the PDF content and get an answer from the LLM.

        :param query: The query string.
        :param n_top_cos: Number of top results to return.
        :return: The answer from the LLM.
        """
from time import perf_counter
from typing import override, final, Optional

import aiohttp

from app.bot import logger
from app.bot.api.ollama.base_ollama import BaseOllama
from app.bot.config import available_llm_models


@final
class Ollama(BaseOllama):
    def __init__(self, prompt: str, model: available_llm_models = available_llm_models,
                 stream: bool = False, endpoint: str = "http://ollama:11434/api/generate",
                 system_prompt: Optional[str] = None):
        """
        Initialize the Llama class.

        Args:
            prompt (str): The input prompt for the model.
            model (Literal["qwen2"], optional): The model to use.".
            stream (bool, optional): Whether to stream the response. Defaults to False.
            endpoint (str, optional): The API endpoint to send the request to. Defaults to "http://ollama:11434/api/generate".
            system_prompt (str, optional): System prompt for the model.
        """
        super().__init__(prompt=prompt, model=model, stream=stream, endpoint=endpoint, system_prompt=system_prompt)

    @override
    async def send_request(self) -> None:
        """
        Send a request to the model.

        This method sends a POST request to the specified endpoint with the given prompt,
        model, and stream settings. The response is stored in self.response.
        """
        url = self.endpoint
        data = {
            "model": self.model,
            "prompt": self.prompt,
            "stream": self.stream,
            "options": {
                "temperature": 0.3
            },
        }

        if self.system_prompt is not None:
            data["system"] = self.system_prompt

        start_time = perf_counter()
        async with aiohttp.ClientSession() as session:
            async with session.post(url, json=data) as response:
                if response.status == 200:
                    result = await response.json()
                    self.response = result
                    logger.info("Response from server:", result)
                else:
                    logger.warning(f"Error: {response.status}\n{await response.json()}")

        logger.info(f"The LLM response was {perf_counter() - start_time} second")

    @override
    def get_formatted_response(self) -> str:
        """
        Get the formatted response from the model.

        This method formats the response stored in self.response and returns it as a string.

        Returns:
            str: The formatted response.
        """
        assert self.response is not None
        return self.response['response']
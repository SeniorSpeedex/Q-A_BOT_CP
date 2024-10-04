import asyncio

from aiogram import Dispatcher

from app.bot import bot, logger
from app.bot.api.ollama.impl.ollama import Ollama
from app.bot.utils.singleton import singleton


@singleton
class Startup:
    _dp = Dispatcher()

    async def start_polling(self):
        await self.test()

    @staticmethod
    async def test():
        ollama = Ollama("Расскажи стих")
        await ollama.send_request()
        logger.info(ollama.get_formatted_response())


if __name__ == "__main__":
    startup = Startup()
    asyncio.run(startup.start_polling())
import asyncio

from aiogram import Dispatcher, Bot
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from app.bot import BOT_TOKEN
from app.bot.utils.singleton import singleton

from app.bot.handlers.start import router as start_router


@singleton
class Startup:
    bot = Bot(BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    _dp = Dispatcher()

    async def start_polling(self):
        await self._dp.start_polling(self.bot)


    def register_routes(self):
        self._dp.include_routers(*[start_router])


if __name__ == "__main__":
    startup = Startup()
    startup.register_routes()
    asyncio.run(startup.start_polling())
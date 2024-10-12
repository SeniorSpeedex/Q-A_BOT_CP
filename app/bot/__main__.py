import asyncio

from aiogram import Dispatcher, Bot
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient

from app.bot import BOT_TOKEN
from app.bot.config import MONGO_URI, super_user_id
from app.bot.database.models.user import User
from app.bot.utils.singleton import singleton
from app.bot.handlers.general import router as general_router
from app.bot.handlers.staff import router as admin_router


@singleton
class Startup:
    bot = Bot(BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    _dp = Dispatcher()

    @staticmethod
    async def _init_database():
        client = AsyncIOMotorClient(MONGO_URI)
        await init_beanie(database=client.db_name, document_models=[User])

    async def start_polling(self):
        await self._init_database()
        await self._dp.start_polling(self.bot)

    async def promote_super_user(self):
        chat = await self.bot.get_chat(super_user_id)
        user = await User(full_name=chat.full_name, telegram_id=super_user_id, post="admin")
        await user.insert()

    def register_routes(self):
        self._dp.include_routers(*[general_router, admin_router])


if __name__ == "__main__":
    startup = Startup()
    startup.register_routes()
    asyncio.run(startup.start_polling())
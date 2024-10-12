from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from app.bot.config import super_user_id

router = Router()

@router.message(Command(commands=["help"]))
async def define_post(message: Message):
    ...
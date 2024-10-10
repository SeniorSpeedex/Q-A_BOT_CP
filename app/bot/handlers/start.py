from aiogram import Router
from aiogram.filters import Command
from aiogram.types import CallbackQuery, Message

from app.bot.keyboards.start import start_keyboard
from app.bot.utils.utils import reco_txt

router = Router()

@router.message(Command(commands=["start"]))
async def start_handler(message: Message):
    await message.reply(
        'Commands: /start.                                                                                   '
        'Выберите действие',
        reply_markup=start_keyboard
    )

@router.callback_query(lambda query: query.data in ('faq', 'ai', 'sap', 'menu'))
async def callback_handler(query: CallbackQuery):
    with open(f'{12}.txt', 'r', encoding='utf-8') as file: # HARDCODE
        content = file.read()
    if query.data == 'faq':
        await query.message.reply(f'{content}')
    elif query.data == 'ai':
        await query.message.reply('ollama')
    elif query.data == 'sap':
        await query.message.reply('3')
    elif query.data == 'menu':
        await query.message.reply(f'Воть {reco_txt}')
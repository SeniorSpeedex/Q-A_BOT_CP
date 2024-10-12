from aiogram import Router, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery

from app.bot.api.pdf.impl.pdf import PDFProcessor
from app.bot.keyboards.general import start_keyboard
from app.bot.utils.utils import GeneralStates

router = Router()

@router.message(Command(commands=["start"]))
async def start_handler(message: Message, state: FSMContext):
    await state.clear()
    await message.reply('Выберите действие',reply_markup=start_keyboard)



@router.callback_query(F.data == "support_button")
async def support_handler(message: Message, state: FSMContext):
    await state.set_state(GeneralStates.GET_HELP)
    await message.reply(text='Напишите ваш запрос в тех.поддержку')

@router.callback_query(GeneralStates.GET_HELP)
async def get_help(callback_query: CallbackQuery, state: FSMContext):
    processor = PDFProcessor()
    processor.initialize_collection()
    processor.load_all_documents('../../../uploads', ['\n\n', '\n'], 1500, 300)

    answer = await processor.query_pdf(callback_query.message.text, 5)
    await callback_query.message.answer(answer)


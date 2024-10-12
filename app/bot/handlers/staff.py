import os
from typing import Optional

from aiogram import Router, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery, Document

from app.bot.config import posts
from app.bot.database.models.employee import Employee
from app.bot.keyboards.staff import admin_keyboard, choice_keyboard, document_keyboard
from app.bot.utils.utils import StaffStates
from app.bot import logger

router = Router()

@router.message(Command(commands=["admin"]))
async def define_post(message: Message):
    user: Optional[Employee] = await Employee.find_one(
        Employee.telegram_id == message.from_user.id
    )

    if user is None:
        return

    await message.answer("Меню открыто", reply_markup=choice_keyboard)

@router.callback_query(F.data == "back_to_choice")
async def back_to_choice(callback_query: CallbackQuery):
    await callback_query.message.edit_text(text="Вы вернулись в главное меню", reply_markup=choice_keyboard)

@router.callback_query(F.data == "back_to_choice_admin")
async def back_to_choice_admin(callback_query: CallbackQuery):
    await callback_query.message.edit_text(text="Вы вернулись в главное меню", reply_markup=choice_keyboard)

@router.callback_query(F.data.startswith("document_management_button"))
async def open_document_panel(callback_query: CallbackQuery):
    await callback_query.message.edit_text(text="Документная панель открыта", reply_markup=document_keyboard)

@router.callback_query(F.data.startswith("admin_keyboard_button"))
async def open_admin_panel(callback_query: CallbackQuery):
    await callback_query.message.edit_text(text="Административная панель открыта", reply_markup=admin_keyboard)

###

UPLOADS_DIR = '../../../uploads'

if not os.path.exists(UPLOADS_DIR):
    os.makedirs(UPLOADS_DIR)

@router.callback_query(F.data.startswith("load_document_button"))
async def load_document(callback_query: CallbackQuery, state: FSMContext):
    await callback_query.message.answer("Загрузите документ")
    await state.set_state(StaffStates.LOAD_DOCUMENT)

@router.message(StaffStates.LOAD_DOCUMENT)
async def handle_document(message: Message, state: FSMContext):
    document: Optional[Document] = message.document
    if document is None:
        await message.answer("Загрузите валидный документ")
        return

    file_id = document.file_id
    file = await message.bot.get_file(file_id)
    file_path = file.file_path

    destination = os.path.join(UPLOADS_DIR, document.file_name)
    await message.bot.download_file(file_path, destination)

    await message.answer(f"Документ {document.file_name} загружен")
    await state.clear()

@router.callback_query(F.data.startswith("unload_document_button"))
async def unload_document(callback_query: CallbackQuery, state: FSMContext):
    await callback_query.answer("Введите имя файла для удаления")
    await state.set_state(StaffStates.UNLOAD_DOCUMENT)

@router.message(StaffStates.UNLOAD_DOCUMENT)
async def handle_unload_document(message: Message, state: FSMContext):
    file_name = message.text
    file_path = os.path.join(UPLOADS_DIR, file_name)

    if os.path.exists(file_path):
        os.remove(file_path)
        await message.answer(f"Файл {file_name} удален")
    else:
        await message.answer(f"Файл {file_name} не найден")

    await state.clear()

###

@router.callback_query(F.data.startswith("promote_button"))
async def promote_callback(callback_query: CallbackQuery, state: FSMContext):
    await callback_query.message.answer("Введите Telegram ID сотрудника")
    await state.set_state(StaffStates.INSERT_NAME)

@router.message(StaffStates.INSERT_NAME)
async def insert_name_message(message: Message, state: FSMContext):
    tg_id = message.text
    try:
        tg_id = int(tg_id)
        await message.answer(f"Вы ввели Telegram ID: {tg_id}")
        await state.update_data(telegram_id=tg_id)
        await state.set_state(StaffStates.INSERT_POST)
        await message.answer(f"Введите должность сотрудника. Доступные - {posts}")
    except ValueError:
        await message.answer("Вы ввели неверный Telegram ID. Пожалуйста, введите число.")
        logger.info(f"Неверный Telegram ID: {tg_id}")

@router.message(StaffStates.INSERT_POST)
async def insert_post_message(message: Message, state: FSMContext):
    post = message.text
    if post not in posts:
        await message.answer(f"Вы ввели неверную должность. Пожалуйста, введите одну из следующих: {posts}")
        return

    data = await state.get_data()
    telegram_id = data.get("telegram_id")

    await message.answer(f"Вы ввели должность: {post} для Telegram ID: {telegram_id}")

    await state.clear()

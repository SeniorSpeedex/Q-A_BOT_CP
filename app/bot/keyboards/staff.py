from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

admin_keyboard_button = InlineKeyboardButton(text="Административная панель", callback_data="admin_keyboard_button")
document_management_button = InlineKeyboardButton(text="Документная панель", callback_data="document_management_button")

choice_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [admin_keyboard_button, document_management_button]
    ]
)
s
load_document_button = InlineKeyboardButton(text="Загрузить документ", callback_data="load_document_button")
list_document_button = InlineKeyboardButton(text="Список документов", callback_data="list_document_button")
unload_document_button = InlineKeyboardButton(text="Выгрузить документ", callback_data="unload_document_button")

document_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [load_document_button, unload_document_button],
        [list_document_button]
    ]
)

promote_button = InlineKeyboardButton(text="Повысить права сотрудника.", callback_data="promote_button")
employee_list_button = InlineKeyboardButton(text="Список сотрудников.", callback_data="employee_list_button")
demote_button = InlineKeyboardButton(text="Понизить права сотрудника.", callback_data="demote_button")

admin_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [promote_button, demote_button],
        [employee_list_button]
    ]
)

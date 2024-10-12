from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

admin_keyboard_button = InlineKeyboardButton(text="Административная панель", callback_data="admin_keyboard_button")
document_management_button = InlineKeyboardButton(text="Документная панель", callback_data="document_management_button")

choice_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [admin_keyboard_button, document_management_button]
    ]
)

load_document_button = InlineKeyboardButton(text="Загрузить документ", callback_data="load_document_button")
list_document_button = InlineKeyboardButton(text="Список документов", callback_data="list_document_button")
unload_document_button = InlineKeyboardButton(text="Выгрузить документ", callback_data="unload_document_button")
back_to_choice_button = InlineKeyboardButton(text="Назад", callback_data="back_to_choice")

document_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [load_document_button, unload_document_button],
        [list_document_button],
        [back_to_choice_button]
    ]
)

promote_button = InlineKeyboardButton(text="Повысить права сотрудника.", callback_data="promote_button")
employee_list_button = InlineKeyboardButton(text="Список сотрудников.", callback_data="employee_list_button")
demote_button = InlineKeyboardButton(text="Понизить права сотрудника.", callback_data="demote_button")
back_to_choice_admin_button = InlineKeyboardButton(text="Назад", callback_data="back_to_choice_admin")

admin_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [promote_button, demote_button],
        [employee_list_button],
        [back_to_choice_admin_button]
    ]
)
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

faq_button = InlineKeyboardButton(text='FAQ', callback_data='faq')
llm_answer_button = InlineKeyboardButton(text='Ответ от ИИ', callback_data='ai')
support_button = InlineKeyboardButton(text='Поддержка', callback_data='sap')
menu_button = InlineKeyboardButton(text='Menu', callback_data='menu')

start_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            faq_button,
            llm_answer_button,
            support_button,
            menu_button
        ]
    ]
)

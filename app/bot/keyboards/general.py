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


one_button = InlineKeyboardButton(text='Какие гарантии предоставляются молодому специалисту?', callback_data='1')
two_button = InlineKeyboardButton(text='Стоимость оплаты за корпоративный детский сад со стороны работника?', callback_data='2')
three_button = InlineKeyboardButton(text='Какие льготы положены моей семье?', callback_data='3')
four_button = InlineKeyboardButton(text='Как получить абонемент в спортивный клуб?', callback_data='4')


faque_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            one_button,
            two_button,
            three_button,
            four_button
        ]
    ]
)

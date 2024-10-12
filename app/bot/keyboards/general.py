from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

faq_button = InlineKeyboardButton(text='FAQ', callback_data='faq_button')
guide_button = InlineKeyboardButton(text='Руководство', callback_data='guide_button')
support_button = InlineKeyboardButton(text='Поддержка', callback_data='support_button')

start_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [faq_button, support_button],
        [guide_button],
    ]
)


one_button = InlineKeyboardButton(text='Какие гарантии предоставляются молодому специалисту?', callback_data='1')
two_button = InlineKeyboardButton(text='Стоимость оплаты за корпоративный детский сад со стороны работника?', callback_data='2')
three_button = InlineKeyboardButton(text='Какие льготы положены моей семье?', callback_data='3')
four_button = InlineKeyboardButton(text='Как получить абонемент в спортивный клуб?', callback_data='4')


faq_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            one_button,
            two_button,
            three_button,
            four_button
        ]
    ]
)

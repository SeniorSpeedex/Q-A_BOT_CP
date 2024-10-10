import asyncio
from aiogram import Bot, Dispatcher, types, executor
# from app.bot import bot, logger
# from app.bot.api.ollama.impl.ollama import Ollama
# from app.bot.utils.singleton import singleton
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# фанка для сравнения текстов

def obama_func(base, base1):
    # Векторизация
    vector = TfidfVectorizer()
    matric = vector.fit_transform([base, base1])
    # Расчитываем косинусное сходство
    cosinus_reg = cosine_similarity(matric[0:1], matric[1:2])

    # Делаем процентики
    return cosinus_reg[0][0] * 100


# результат
reco_txt = obama_func('Ты и я', 'Я и ты')

promt = 'Как рулить?'
doxnum = 12
API_TOKEN = '7946623770:AAFSgy7AL1lgRxcHwawPZI-kJLUzJXivKXQ'
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)




@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    await message.reply(
        'Commands: /start.                                                                                   '
        'Выберите действие',
        reply_markup=types.InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    types.InlineKeyboardButton('FAQ', callback_data='faq'),
                    types.InlineKeyboardButton('Ответ от ИИ', callback_data='ai'),
                    types.InlineKeyboardButton('Поддержка', callback_data='sap'),
                    types.InlineKeyboardButton('Menu', callback_data='menu')
                ]
            ]
        ))


with open(f'{doxnum}.txt', 'r', encoding='utf-8') as file:
    content = file.read()


@dp.callback_query_handler(lambda query: query.data in ('faq', 'ai', 'sap', 'menu'))
async def callback_handler(query: types.CallbackQuery):
    if query.data == 'faq':
        await query.message.reply(f'{content}')
    elif query.data == 'ai':
        await query.message.reply('ollama')
    elif query.data == 'sap':
        await query.message.reply('3')
    elif query.data == 'menu':
        await query.message.reply(f'Воть {reco_txt}')


if __name__ == '__main__':
    # startup = Startup()
    executor.start_polling(dp, skip_updates=True)

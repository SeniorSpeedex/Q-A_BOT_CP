from aiogram import Router
from aiogram.filters import Command
from aiogram.types import CallbackQuery, Message
from app.bot.keyboards.general import start_keyboard
from app.bot.keyboards.general import faque_keyboard


router = Router()

@router.message(Command(commands=["start"]))
async def start_handler(message: Message):
    await message.reply(
        'Commands: /start.                                                                                   '
        'Выберите действие',
        reply_markup=start_keyboard

    )

@router.message(commands=["faque"])
async def faque_handler(message: Message):
    await message.reply(
        "Самые популярные вопросы:",
        replay_markup = faque_keyboard

    )
@router.callback_query(lambda query: query.data in ('1', '2', '3', '4'))
async def callback_handler(query: CallbackQuery):
    if query.data == '1':
        await query.message.reply('Молодому специалисту предоставляются льготы в соответствии с законодательством Российской Федерации, '
                                  'Положением о молодом специалисте ОАО «РЖД», утвержденном распоряжением ОАО «РЖД» от 18 июля 2017 г. '
                                  '№ 1397/р. Ознакомиться с Положением о молодом специалисте можно на сайте компании РЖД '
                                  'https://company.rzd.ru  в разделе «Документы» или проконсультироваться по интересующему вопросу у '
                                  'ответственного специалиста отдела по управлению персоналом структурного подразделения.'
                                  )
    elif query.data == '2':
        await query.message.reply('Оплата за посещение ребёнком детского сада определяется в соответствии с Положением об '
                                  'установлении стоимости и оплате услуг в дошкольных группах частных образовательных учреждений ОАО «РЖД» и зависит '
                                  'от количества детей в семье и социального статуса работника.'
                                  )
    elif query.data == '3':
        await query.message.reply('Для информировании работников о льготах и гарантиях, предоставляемых в компании, разработан Путеводитель по льготам, который разъясняет предоставление льгот в простом и доступном формате с пошаговым алгоритмом.'
                                    "Путеводитель структурирован в пакетные предложения под жизненные ситуации работника и включает в себя 11 тематических блоков:"
                                    "1. Бесплатный проезд."
                                    "2. Отпуск. "
                                    "3. Здоровье."
                                    "4. Досуг."
                                    "5. Семья (семейное благополучие)."
                                    "6. Компенсируемый социальный пакет. Бонусный пакет."
                                    "7. Молодежь."
                                    '8. Комфортные условия.'
                                    '9. Перед выходом на пенсию.'
                                    '10. Корпоративное волонтерство.'
                                    '11. Здоровый образ жизни.'
                                    'Ознакомиться с Путеводителем можно на Сервисном портале в блоге «Социальная поддержка».'
                                  )
    elif query.data == '4':
        await query.message.reply('Если вы хотите получить компенсацию на абонемент в спортивный клуб, обратитесь '
                                  'с заявлением к ответственному работнику подразделения ОАО «РЖД», в ведении которого '
                                  'находится вопрос оформления документов на компенсацию затрат занятий физической культурой.'
                                  )





@router.callback_query(lambda query: query.data in ('faq', 'ai', 'sap', 'menu'))
async def callback_handler(query: CallbackQuery):
    if query.data == 'faq':
        await query.message.reply("FAQ")
    elif query.data == 'ai':
        await query.message.reply('ollama')
    elif query.data == 'sap':
        await query.message.reply('Для получения более подробной информации, ответа на '
                                  'прочие вопросы или информации, касающейся вопросов '
                                  'частного порядка, просьба писать @F1lin_GG'
                                  )
    elif query.data == 'menu':
        await query.message.reply('назад')

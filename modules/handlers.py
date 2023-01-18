from aiogram import types, Dispatcher
from modules.bot_base import dp, bot
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from modules.buttons import main_menu_keyboard, doc_generator_start_keyboard, cancel_generator_keyboard, doc_generator_finish_keyboard, consultation_keyboard, consultation_keyboard_in, feedback_keyboard, about_me_keyboard, cooperation_keyboard, suggestion_keyboard
from modules.judicial_writer_1 import data_print

# Машина состояний генератора документов

class DocGenerator(StatesGroup):
    doc_generator1 = State()
    doc_generator2 = State()
    doc_generator3 = State()
    doc_generator4 = State()
    doc_generator5 = State()
    doc_generator6 = State()
    doc_generator7 = State()
    doc_generator8 = State()
    doc_generator9 = State()
    doc_generator10 = State()
    doc_generator11 = State()
    doc_generator12 = State()
    doc_generator13 = State()
    doc_generator14 = State()













# Главное меню

async def start_command(message: types.Message):
    await bot.send_message(chat_id = message.from_user.id, text='Вас приветствует юрист Павлюков Я.Я. Выберите интересующий Вас раздел ниже:', reply_markup=main_menu_keyboard)

async def restart_command(message: types.Message):
    # await bot.delete_message(chat_id = message.from_user.id, message_id=message.message_id)
    await bot.send_message(chat_id = message.from_user.id, text='Выберите то, что Вас интересует:', reply_markup=main_menu_keyboard)

# Меню консультации

async def consultation_start_command(message: types.Message):
    await bot.send_message(chat_id = message.from_user.id, text='По какой тематике Вы желаете получить консультацию?', reply_markup=consultation_keyboard)

async def consultation_mobilization(message: types.Message):
    await bot.send_message(chat_id = message.from_user.id, text='Оставьте своё обращение ответным сообщением, и я свяжусь с Вами в ближайшее время', reply_markup=consultation_keyboard_in)

async def consultation_migration(message: types.Message):
    await bot.send_message(chat_id = message.from_user.id, text='Оставьте своё обращение ответным сообщением, и я свяжусь с Вами в ближайшее время', reply_markup=consultation_keyboard_in)

async def consultation_employment(message: types.Message):
    await bot.send_message(chat_id = message.from_user.id, text='Оставьте своё обращение ответным сообщением, и я свяжусь с Вами в ближайшее время', reply_markup=consultation_keyboard_in)

async def consultation_consumer(message: types.Message):
    await bot.send_message(chat_id = message.from_user.id, text='Оставьте своё обращение ответным сообщением, и я свяжусь с Вами в ближайшее время', reply_markup=consultation_keyboard_in)

async def consultation_back(message: types.Message):
    await bot.send_message(chat_id = message.from_user.id, text='Вы можете обратиться и по другой тематике:', reply_markup=consultation_keyboard)

# Меню отзывов и замечаний

async def feedback(message: types.Message):
    await bot.send_message(chat_id = message.from_user.id, text='Вы можете оставить отзыв о нашем с Вами сотрудничестве ответным сообщением, и он обязательно будет опубликован в моих социальных сетях. А если у Вас есть замечания или предложения по поводу моих услуг, буду рад принять их к сведению. Благодарю Вас!', reply_markup=feedback_keyboard)

# Меню сотрудничества

async def cooperation(message: types.Message):
    await bot.send_message(chat_id = message.from_user.id, text='Я всегда открыт для сотрудничества, и Вы можете написать мне свои идеи или предложения ответным сообщением', reply_markup=cooperation_keyboard)

# Меню предложений

async def suggestion(message: types.Message):
    await bot.send_message(chat_id = message.from_user.id, text='https://t.me/bettercallpavlukov/480')
    await bot.send_message(chat_id = message.from_user.id, text='Вы можете ознакомиться с моими статьями на юридическую тематику, используя хэштеги по ссылке выше, и если они пока-что не затронули сферу Ваших интересов, Вы можете обратиться ко мне за индивидуальной консультацией в другом разделе главного меню или озвучить своё предложение ответным сообщением ниже, и, вполне вероятно, я сделаю публикацию на данную тематику', reply_markup=suggestion_keyboard)

# Обо мне

async def about_me_start_command(message: types.Message):
    await bot.send_photo(chat_id=message.chat.id, photo=open('/home/lines14/projects/judicial_telegram_bot/documents/about_me.jpg', 'rb'))
    await bot.send_message(chat_id = message.from_user.id, text='Подписывайтесь на мои социальные сети, чтобы быть в курсе всех юридических новостей:', reply_markup=about_me_keyboard)

async def about_me_telegram(message: types.Message):
    await bot.send_message(chat_id = message.from_user.id, text='https://t.me/bettercallpavlukov', reply_markup=about_me_keyboard)

async def about_me_instagram(message: types.Message):
    await bot.send_message(chat_id = message.from_user.id, text='https://www.instagram.com/bettercallpavlukov/', reply_markup=about_me_keyboard)

async def about_me_vk(message: types.Message):
    await bot.send_message(chat_id = message.from_user.id, text='https://vk.com/yaroslaw_org', reply_markup=about_me_keyboard)

# Меню генератора документов:

async def generator_start_command(message: types.Message):
    await bot.send_message(chat_id = message.from_user.id, text='Добро пожаловать в сервис генерации судебных документов. Нажмите кнопку "создать", а затем введите требуемые данные, чтобы сформировать документ. Или можете посмотреть пример готового документа, нажав кнопку "пример"', reply_markup=doc_generator_start_keyboard)

async def get_example(message: types.Message):
    await message.reply_document(open('/home/lines14/projects/judicial_telegram_bot/example/judicial_writer_1_example.docx', 'rb'))

async def add_data(message: types.Message):
    await DocGenerator.doc_generator1.set()
    await message.reply('Введите название инстанции для обращения:', reply_markup=cancel_generator_keyboard)

async def cancel_handlers_pick_data(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await message.reply('Вы можете начать заново с нажатия кнопки "создать"', reply_markup=doc_generator_start_keyboard)

async def doc_generator1(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['user_data1'] = message.text
    await DocGenerator.next()
    await bot.send_message(chat_id = message.from_user.id, text='Укажите адрес инстанции для обращения:')

async def doc_generator2(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['user_data2'] = message.text
    await DocGenerator.next()
    await bot.send_message(chat_id = message.from_user.id, text='Введите ФИО истца:')

async def doc_generator3(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['user_data3'] = message.text
    await DocGenerator.next()
    await bot.send_message(chat_id = message.from_user.id, text='Укажите адрес истца:')

async def doc_generator4(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['user_data4'] = message.text
    await DocGenerator.next()
    await bot.send_message(chat_id = message.from_user.id, text='Введите адрес истца для корреспонденции при необходимости:')

async def doc_generator5(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['user_data5'] = message.text
    await DocGenerator.next()
    await bot.send_message(chat_id = message.from_user.id, text='Укажите представителя истца при необходимости:')

async def doc_generator6(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['user_data6'] = message.text
    await DocGenerator.next()
    await bot.send_message(chat_id = message.from_user.id, text='Введите контактные данные представителя истца:')

async def doc_generator7(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['user_data7'] = message.text
    await DocGenerator.next()
    await bot.send_message(chat_id = message.from_user.id, text='Укажите ответчика:')

async def doc_generator8(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['user_data8'] = message.text
    await DocGenerator.next()
    await bot.send_message(chat_id = message.from_user.id, text='Введите адрес ответчика:')

async def doc_generator9(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['user_data9'] = message.text
    await DocGenerator.next()
    await bot.send_message(chat_id = message.from_user.id, text='Укажите номер дела:')

async def doc_generator10(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['user_data10'] = message.text
    await DocGenerator.next()
    await bot.send_message(chat_id = message.from_user.id, text='Введите дату подачи Вашего обращения:')

async def doc_generator11(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['user_data11'] = message.text
    await DocGenerator.next()
    await bot.send_message(chat_id = message.from_user.id, text='Сформулируйте текст Вашего обращения:')

async def doc_generator12(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['user_data12'] = message.text
    await DocGenerator.next()
    await bot.send_message(chat_id = message.from_user.id, text='Укажите процессуальный статус обращающегося:')

async def doc_generator13(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['user_data13'] = message.text
    await DocGenerator.next()
    await bot.send_message(chat_id = message.from_user.id, text='Введите инициалы обращающегося:')

async def doc_generator14(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['user_data14'] = message.text
    await data_print(state)
    await bot.send_message(chat_id = message.from_user.id, text='Указанные Вами данные приняты, нажмите кнопку "получить", чтобы выгрузить готовый документ', reply_markup=doc_generator_finish_keyboard)
    await state.finish()

async def get_file(message: types.Message):
    await message.reply_document(open('/home/lines14/projects/judicial_telegram_bot/documents/judicial_writer_1.docx', 'rb'))















# Регистраторы функций-хэндлеров

def register_handler_client(dp: Dispatcher):

    # Регистраторы главного меню

    dp.register_message_handler(start_command, commands=['start'])
    dp.register_message_handler(consultation_start_command, commands=['получитьㅤконсультацию'])
    dp.register_message_handler(generator_start_command, commands=['перейтиㅤвㅤгенераторㅤсудебныхㅤдокументов'])
    dp.register_message_handler(about_me_start_command, commands=['обоㅤмне'])
    dp.register_message_handler(feedback, commands=['оставитьㅤотзывㅤилиㅤзамечание'])
    dp.register_message_handler(cooperation, commands=['сотрудничество'])
    dp.register_message_handler(suggestion, commands=['предложитьㅤтемуㅤдляㅤновойㅤпубликации'])
    dp.register_message_handler(restart_command, commands=['вㅤглавноеㅤменю'])

    # Регистраторы меню консультаций

    dp.register_message_handler(consultation_mobilization, commands=['мобилизация'])
    dp.register_message_handler(consultation_migration, commands=['миграция'])
    dp.register_message_handler(consultation_employment, commands=['трудовыеㅤспоры'])
    dp.register_message_handler(consultation_consumer, commands=['защитаㅤправㅤпотребителей'])
    dp.register_message_handler(consultation_back, commands=['назад'])

    # Регистраторы меню обо мне

    dp.register_message_handler(about_me_telegram, commands=['telegramㅤpublic'])
    dp.register_message_handler(about_me_instagram, commands=['instagram'])
    dp.register_message_handler(about_me_vk, commands=['vk'])

    # Регистраторы генератора документов

    dp.register_message_handler(get_example, commands=['пример'])
    dp.register_message_handler(add_data, commands=['создать'], state=None)
    dp.register_message_handler(cancel_handlers_pick_data, state='*', commands=['отмена'])
    dp.register_message_handler(doc_generator1, state=DocGenerator.doc_generator1)
    dp.register_message_handler(doc_generator2, state=DocGenerator.doc_generator2)
    dp.register_message_handler(doc_generator3, state=DocGenerator.doc_generator3)
    dp.register_message_handler(doc_generator4, state=DocGenerator.doc_generator4)
    dp.register_message_handler(doc_generator5, state=DocGenerator.doc_generator5)
    dp.register_message_handler(doc_generator6, state=DocGenerator.doc_generator6)
    dp.register_message_handler(doc_generator7, state=DocGenerator.doc_generator7)
    dp.register_message_handler(doc_generator8, state=DocGenerator.doc_generator8)
    dp.register_message_handler(doc_generator9, state=DocGenerator.doc_generator9)
    dp.register_message_handler(doc_generator10, state=DocGenerator.doc_generator10)
    dp.register_message_handler(doc_generator11, state=DocGenerator.doc_generator11)
    dp.register_message_handler(doc_generator12, state=DocGenerator.doc_generator12)
    dp.register_message_handler(doc_generator13, state=DocGenerator.doc_generator13)
    dp.register_message_handler(doc_generator14, state=DocGenerator.doc_generator14)
    dp.register_message_handler(get_file, commands=['получить'])
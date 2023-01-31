from aiogram import types, Dispatcher
from modules.bot_base import dp, bot
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from modules.buttons import intro_inline_keyboard, consultation_inline_keyboard, consultation_inline_keyboard_missclick, consultation_inline_keyboard_phone_keeper, socials_inline_keyboard, main_menu_keyboard, doc_generator_start_keyboard, cancel_generator_keyboard, doc_generator_finish_keyboard, consultation_keyboard, consultation_keyboard_in_mobilization, consultation_keyboard_in_migration, consultation_keyboard_in_employment, consultation_keyboard_in_consumer, consultation_keyboard_in_only_telegram, consultation_keyboard_in_abort, consultation_keyboard_in_after_recomendations, consultation_keyboard_in_after_inline_mobilization, consultation_keyboard_in_after_inline_migration, consultation_keyboard_in_after_inline_employment, consultation_keyboard_in_after_inline_consumer, consultation_keyboard_in_after_inline_recomendations, feedback_keyboard, cooperation_keyboard_in, cooperation_keyboard_in_abort, cooperation_keyboard_in_only_telegram, suggestion_keyboard, feedback_keyboard_abort, suggestion_keyboard_abort
from modules.judicial_writer_1 import data_print
from modules import data_base
from modules.phone_processing import phone_checker
from datetime import datetime
import typing
from aiogram.types import ReplyKeyboardRemove

# Машины состояний бота

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

# Машины состояний инлайн обращений за консультациями

class InlineAppealMobilization(StatesGroup):
    inline_appeal_mobilization1 = State()
    inline_appeal_mobilization2 = State()

class InlineAppealMigration(StatesGroup):
    inline_appeal_migration1 = State()
    inline_appeal_migration2 = State()

class InlineAppealEmployment(StatesGroup):
    inline_appeal_employment1 = State()
    inline_appeal_employment2 = State()

class InlineAppealConsumer(StatesGroup):
    inline_appeal_consumer1 = State()
    inline_appeal_consumer2 = State()

# Машины состояний обращений за консультациями через основное меню

class AppealMobilization(StatesGroup):
    appeal_mobilization1 = State()
    appeal_mobilization2 = State()

class AppealMigration(StatesGroup):
    appeal_migration1 = State()
    appeal_migration2 = State()

class AppealEmployment(StatesGroup):
    appeal_employment1 = State()
    appeal_employment2 = State()

class AppealConsumer(StatesGroup):
    appeal_consumer1 = State()
    appeal_consumer2 = State()

# Машины состояний отзывов, предложений сотрудничества и предложений тем для публикаций

class AppealFeedback(StatesGroup):
    appeal_feedback1 = State()

class AppealCooperation(StatesGroup):
    appeal_cooperation1 = State()
    appeal_cooperation2 = State()

class AppealSuggestion(StatesGroup):
    appeal_suggestion1 = State()

# Хэндлеры бота
# Диалог приветствия и главное меню

async def start_command(message: types.Message):
    fullname = message.from_user.full_name
    await bot.send_message(chat_id = message.from_user.id, text=f'Приветствую вас, {fullname}!\nНа связи Ярослав Павлюков. Хотите получить консультацию?', reply_markup=intro_inline_keyboard)

async def start_inline_keyboard_callback_redirect(message: types.Message):
    await bot.send_message(chat_id = message.from_user.id, text='Вы можете выбрать интересующий вас раздел в меню ниже:', reply_markup=main_menu_keyboard)

async def restart_command(message: types.Message):
    # await bot.delete_message(chat_id = message.from_user.id, message_id=message.message_id)
    await bot.send_message(chat_id = message.from_user.id, text='Выберите то, что вас интересует:', reply_markup=main_menu_keyboard)

async def restart_command_inline(message: types.Message):
    # await bot.delete_message(chat_id = message.from_user.id, message_id=message.message_id)
    await bot.send_message(chat_id = message.from_user.id, text='Выберите то, что вас интересует:', reply_markup=main_menu_keyboard)

async def restart_command_for_all_FSM(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await message.reply('Выберите то, что вас интересует:', reply_markup=main_menu_keyboard)

# Стартовый диалог на тему консультации со сборщиками данных

async def start_inline_keyboard_callback_pick(message: types.Message):
    await bot.send_message(chat_id = message.from_user.id, text='В каком направлении вы хотите получить консультацию?', reply_markup=consultation_inline_keyboard)

async def restart_inline_keyboard_callback_pick(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await bot.send_message(chat_id = message.from_user.id, text='Вы можете выбрать другое направление', reply_markup=types.ReplyKeyboardRemove())
    await bot.send_message(chat_id = message.from_user.id, text='В каком направлении вы хотите получить консультацию?', reply_markup=consultation_inline_keyboard)

async def recomendations_after_inline(message: types.Message):
    await bot.send_message(chat_id = message.from_user.id, text='Вы можете ознакомиться с моими постами на интересующую вас тему, используя хэштеги по ссылке ниже')
    await bot.send_message(chat_id = message.from_user.id, text='https://t.me/bettercallpavlukov/480', reply_markup=consultation_keyboard_in_after_inline_recomendations)

# Мобилизация

async def start_inline_keyboard_callback_mobilization(message: types.Message):
    await InlineAppealMobilization.inline_appeal_mobilization1.set()
    await bot.send_message(chat_id = message.from_user.id, text='Напишите пожалуйста ответным сообщением ваш номер телефона, чтобы я мог связаться с вами', reply_markup=consultation_inline_keyboard_phone_keeper)
    await bot.send_message(chat_id = message.from_user.id, text='В международном формате с "+7" (или с другим кодом), без пробелов или тире', reply_markup=consultation_inline_keyboard_missclick)

async def start_inline_keyboard_callback_mobilization_phone_processing(message: typing.Union[types.Contact, types.Message], state: FSMContext):
    async with state.proxy() as data:
        if not message.text:
            data['status'] = 'Свяжитесь со мной в Telegram'
            data['phone'] = message.contact.phone_number
            phone_checked = await phone_checker(data['phone'])
        else:
            data['status'] = 'Позвоните мне'
            data['phone'] = message.text
            phone_checked = await phone_checker(data['phone'])
        
        if phone_checked != 'fail':
            data['phone'] = await phone_checker(data['phone'])
            await InlineAppealMobilization.inline_appeal_mobilization2.set()
            await bot.send_message(chat_id = message.from_user.id, text='Напишите пожалуйста ваш вопрос ответным сообщением', reply_markup=types.ReplyKeyboardRemove())
            await bot.send_message(chat_id = message.from_user.id, text='Я свяжусь с вами в ближайшее время', reply_markup=consultation_inline_keyboard_missclick)
        else:
            await InlineAppealMobilization.inline_appeal_mobilization1.set()
            await bot.send_message(chat_id = message.from_user.id, text='Некорректно введён номер телефона', reply_markup=consultation_inline_keyboard_phone_keeper)
            await bot.send_message(chat_id = message.from_user.id, text='Пожалуйста повторите, начиная с "+7" (или с другим кодом), без пробелов или тире', reply_markup=consultation_inline_keyboard_missclick)

async def start_inline_keyboard_callback_mobilization_add_appeal(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['user_id'] = message.chat.id
        if message.from_user.username == None:
            data['nickname'] = ''
        else:
            data['nickname'] = message.from_user.username
        data['fullname'] = message.from_user.full_name
        data['section'] = 'Мобилизация'
        current_datetime = datetime.now()
        data['datetime'] = str(current_datetime)[0:-7]
        data['appeal'] = message.text
    await data_base.sql_add_appeal(state)
    await bot.send_message(chat_id = message.from_user.id, text='Спасибо за ваше обращение! Я свяжусь с вами в ближайшее время. Мы работаем с 10:00 до 20:00 (МСК) по будням, в выходные мы отдыхаем', reply_markup=consultation_keyboard_in_after_inline_mobilization)
    await state.finish()

# Миграция

async def start_inline_keyboard_callback_migration(message: types.Message):
    await InlineAppealMigration.inline_appeal_migration1.set()
    await bot.send_message(chat_id = message.from_user.id, text='Напишите пожалуйста ответным сообщением ваш номер телефона в международном формате с "+7" (или с другим кодом), без пробелов или тире, чтобы я мог связаться с вами', reply_markup=consultation_inline_keyboard_phone_keeper)
    await bot.send_message(chat_id = message.from_user.id, text='В следующем сообщении я попрошу вас написать ваш вопрос, а сразу после отправки вашего вопроса, вы получите от меня в подарок чек-лист "Переезд из России: деньги и документы"', reply_markup=consultation_inline_keyboard_missclick)

async def start_inline_keyboard_callback_migration_phone_processing(message: typing.Union[types.Contact, types.Message], state: FSMContext):
    async with state.proxy() as data:
        if not message.text:
            data['status'] = 'Свяжитесь со мной в Telegram'
            data['phone'] = message.contact.phone_number
            phone_checked = await phone_checker(data['phone'])
        else:
            data['status'] = 'Позвоните мне'
            data['phone'] = message.text
            phone_checked = await phone_checker(data['phone'])
        
        if phone_checked != 'fail':
            data['phone'] = await phone_checker(data['phone'])
            await InlineAppealMigration.inline_appeal_migration2.set()
            await bot.send_message(chat_id = message.from_user.id, text='Напишите пожалуйста ваш вопрос ответным сообщением', reply_markup=types.ReplyKeyboardRemove())
            await bot.send_message(chat_id = message.from_user.id, text='Я свяжусь с вами в ближайшее время', reply_markup=consultation_inline_keyboard_missclick)
        else:
            await InlineAppealMigration.inline_appeal_migration1.set()
            await bot.send_message(chat_id = message.from_user.id, text='Некорректно введён номер телефона', reply_markup=consultation_inline_keyboard_phone_keeper)
            await bot.send_message(chat_id = message.from_user.id, text='Пожалуйста повторите, начиная с "+7" (или с другим кодом), без пробелов или тире', reply_markup=consultation_inline_keyboard_missclick)

async def start_inline_keyboard_callback_migration_add_appeal(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['user_id'] = message.chat.id
        if message.from_user.username == None:
            data['nickname'] = ''
        else:
            data['nickname'] = message.from_user.username
        data['fullname'] = message.from_user.full_name
        data['section'] = 'Миграция'
        current_datetime = datetime.now()
        data['datetime'] = str(current_datetime)[0:-7]
        data['appeal'] = message.text
    await data_base.sql_add_appeal(state)
    await bot.send_message(chat_id = message.from_user.id, text='Спасибо за ваше обращение! Я свяжусь с вами в ближайшее время. Мы работаем с 10:00 до 20:00 (МСК) по будням, в выходные мы отдыхаем', reply_markup=consultation_keyboard_in_after_inline_migration)
    await bot.send_message(chat_id = message.from_user.id, text='Помимо этого, рад презентовать вам свой чек-лист "Переезд из России: деньги и документы" по ссылке ниже:\nhttps://drive.google.com/file/d/1Y2rMo_GcgpF3ck2NzU0JPbQU2of3VQpT/view')
    await state.finish()

# Трудовые споры

async def start_inline_keyboard_callback_employment(message: types.Message):
    await InlineAppealEmployment.inline_appeal_employment1.set()
    await bot.send_message(chat_id = message.from_user.id, text='Напишите пожалуйста ответным сообщением ваш номер телефона, чтобы я мог связаться с вами', reply_markup=consultation_inline_keyboard_phone_keeper)
    await bot.send_message(chat_id = message.from_user.id, text='В международном формате с "+7" (или с другим кодом), без пробелов или тире', reply_markup=consultation_inline_keyboard_missclick)

async def start_inline_keyboard_callback_employment_phone_processing(message: typing.Union[types.Contact, types.Message], state: FSMContext):
    async with state.proxy() as data:
        if not message.text:
            data['status'] = 'Свяжитесь со мной в Telegram'
            data['phone'] = message.contact.phone_number
            phone_checked = await phone_checker(data['phone'])
        else:
            data['status'] = 'Позвоните мне'
            data['phone'] = message.text
            phone_checked = await phone_checker(data['phone'])
        
        if phone_checked != 'fail':
            data['phone'] = await phone_checker(data['phone'])
            await InlineAppealEmployment.inline_appeal_employment2.set()
            await bot.send_message(chat_id = message.from_user.id, text='Напишите пожалуйста ваш вопрос ответным сообщением', reply_markup=types.ReplyKeyboardRemove())
            await bot.send_message(chat_id = message.from_user.id, text='Я свяжусь с вами в ближайшее время', reply_markup=consultation_inline_keyboard_missclick)
        else:
            await InlineAppealEmployment.inline_appeal_employment1.set()
            await bot.send_message(chat_id = message.from_user.id, text='Некорректно введён номер телефона', reply_markup=consultation_inline_keyboard_phone_keeper)
            await bot.send_message(chat_id = message.from_user.id, text='Пожалуйста повторите, начиная с "+7" (или с другим кодом), без пробелов или тире', reply_markup=consultation_inline_keyboard_missclick)

async def start_inline_keyboard_callback_employment_add_appeal(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['user_id'] = message.chat.id
        if message.from_user.username == None:
            data['nickname'] = ''
        else:
            data['nickname'] = message.from_user.username
        data['fullname'] = message.from_user.full_name
        data['section'] = 'Трудовые споры'
        current_datetime = datetime.now()
        data['datetime'] = str(current_datetime)[0:-7]
        data['appeal'] = message.text
    await data_base.sql_add_appeal(state)
    await bot.send_message(chat_id = message.from_user.id, text='Спасибо за ваше обращение! Я свяжусь с вами в ближайшее время. Мы работаем с 10:00 до 20:00 (МСК) по будням, в выходные мы отдыхаем', reply_markup=consultation_keyboard_in_after_inline_employment)
    await state.finish()

# Защита прав потребителей

async def start_inline_keyboard_callback_consumer(message: types.Message):
    await InlineAppealConsumer.inline_appeal_consumer1.set()
    await bot.send_message(chat_id = message.from_user.id, text='Напишите пожалуйста ответным сообщением ваш номер телефона, чтобы я мог связаться с вами', reply_markup=consultation_inline_keyboard_phone_keeper)
    await bot.send_message(chat_id = message.from_user.id, text='В международном формате с "+7" (или с другим кодом), без пробелов или тире', reply_markup=consultation_inline_keyboard_missclick)

async def start_inline_keyboard_callback_consumer_phone_processing(message: typing.Union[types.Contact, types.Message], state: FSMContext):
    async with state.proxy() as data:
        if not message.text:
            data['status'] = 'Свяжитесь со мной в Telegram'
            data['phone'] = message.contact.phone_number
            phone_checked = await phone_checker(data['phone'])
        else:
            data['status'] = 'Позвоните мне'
            data['phone'] = message.text
            phone_checked = await phone_checker(data['phone'])
        
        if phone_checked != 'fail':
            data['phone'] = await phone_checker(data['phone'])
            await InlineAppealConsumer.inline_appeal_consumer2.set()
            await bot.send_message(chat_id = message.from_user.id, text='Напишите пожалуйста ваш вопрос ответным сообщением', reply_markup=types.ReplyKeyboardRemove())
            await bot.send_message(chat_id = message.from_user.id, text='Я свяжусь с вами в ближайшее время', reply_markup=consultation_inline_keyboard_missclick)
        else:
            await InlineAppealConsumer.inline_appeal_consumer1.set()
            await bot.send_message(chat_id = message.from_user.id, text='Некорректно введён номер телефона', reply_markup=consultation_inline_keyboard_phone_keeper)
            await bot.send_message(chat_id = message.from_user.id, text='Пожалуйста повторите, начиная с "+7" (или с другим кодом), без пробелов или тире', reply_markup=consultation_inline_keyboard_missclick)

async def start_inline_keyboard_callback_consumer_add_appeal(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['user_id'] = message.chat.id
        if message.from_user.username == None:
            data['nickname'] = ''
        else:
            data['nickname'] = message.from_user.username
        data['fullname'] = message.from_user.full_name
        data['section'] = 'Защита прав потребителей'
        current_datetime = datetime.now()
        data['datetime'] = str(current_datetime)[0:-7]
        data['appeal'] = message.text
    await data_base.sql_add_appeal(state)
    await bot.send_message(chat_id = message.from_user.id, text='Спасибо за ваше обращение! Я свяжусь с вами в ближайшее время. Мы работаем с 10:00 до 20:00 (МСК) по будням, в выходные мы отдыхаем', reply_markup=consultation_keyboard_in_after_inline_consumer)
    await state.finish()

# Меню консультации со сборщиками данных

async def consultation_start_command(message: types.Message):
    await bot.send_message(chat_id = message.from_user.id, text='В каком направлении вы хотите получить консультацию?', reply_markup=consultation_keyboard)

async def consultation_back(message: types.Message):
    await bot.send_message(chat_id = message.from_user.id, text='Вы можете обратиться и по другому направлению:', reply_markup=consultation_keyboard)

async def consultation_back_for_consultation_FSM(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await message.reply('Вы можете обратиться и по другому направлению:', reply_markup=consultation_keyboard)

async def recomendations_after(message: types.Message):
    await bot.send_message(chat_id = message.from_user.id, text='Вы можете ознакомиться с моими постами на интересующую вас тему, используя хэштеги по ссылке ниже')
    await bot.send_message(chat_id = message.from_user.id, text='https://t.me/bettercallpavlukov/480', reply_markup=consultation_keyboard_in_after_recomendations)

# Мобилизация

async def consultation_mobilization(message: types.Message):
    await AppealMobilization.appeal_mobilization1.set()
    await bot.send_message(chat_id = message.from_user.id, text='Напишите пожалуйста ответным сообщением ваш номер телефона в международном формате с "+7" (или с другим кодом), без пробелов или тире, чтобы я мог связаться с вами', reply_markup=consultation_keyboard_in_only_telegram)

async def consultation_mobilization_phone_processing(message: typing.Union[types.Contact, types.Message], state: FSMContext):
    async with state.proxy() as data:
        if not message.text:
            data['status'] = 'Свяжитесь со мной в Telegram'
            data['phone'] = message.contact.phone_number
            phone_checked = await phone_checker(data['phone'])
        else:
            data['status'] = 'Позвоните мне'
            data['phone'] = message.text
            phone_checked = await phone_checker(data['phone'])
        
        if phone_checked != 'fail':
            data['phone'] = await phone_checker(data['phone'])
            await AppealMobilization.appeal_mobilization2.set()
            await bot.send_message(chat_id = message.from_user.id, text='Напишите пожалуйста ваш вопрос ответным сообщением, и я свяжусь с вами в ближайшее время', reply_markup=consultation_keyboard_in_abort)
        else:
            await AppealMobilization.appeal_mobilization1.set()
            await bot.send_message(chat_id = message.from_user.id, text='Некорректно введён номер телефона, пожалуйста повторите, начиная с "+7" (или с другим кодом), без пробелов или тире', reply_markup=consultation_keyboard_in_only_telegram)

async def consultation_mobilization_add_appeal(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['user_id'] = message.chat.id
        if message.from_user.username == None:
            data['nickname'] = ''
        else:
            data['nickname'] = message.from_user.username
        data['fullname'] = message.from_user.full_name
        data['section'] = 'Мобилизация'
        current_datetime = datetime.now()
        data['datetime'] = str(current_datetime)[0:-7]
        data['appeal'] = message.text
    await data_base.sql_add_appeal(state)
    await bot.send_message(chat_id = message.from_user.id, text='Спасибо за ваше обращение! Я свяжусь с вами в ближайшее время. Мы работаем с 10:00 до 20:00 (МСК) по будням, в выходные мы отдыхаем', reply_markup=consultation_keyboard_in_mobilization)
    await state.finish()

# Миграция

async def consultation_migration(message: types.Message):
    await AppealMigration.appeal_migration1.set()
    await bot.send_message(chat_id = message.from_user.id, text='Напишите пожалуйста ответным сообщением ваш номер телефона в международном формате с "+7" (или с другим кодом), без пробелов или тире, чтобы я мог связаться с вами.\n\nВ следующем сообщении я попрошу вас написать ваш вопрос, а сразу после отправки вашего вопроса, вы получите от меня в подарок чек-лист "Переезд из России: деньги и документы"', reply_markup=consultation_keyboard_in_only_telegram)

async def consultation_migration_phone_processing(message: typing.Union[types.Contact, types.Message], state: FSMContext):
    async with state.proxy() as data:
        if not message.text:
            data['status'] = 'Свяжитесь со мной в Telegram'
            data['phone'] = message.contact.phone_number
            phone_checked = await phone_checker(data['phone'])
        else:
            data['status'] = 'Позвоните мне'
            data['phone'] = message.text
            phone_checked = await phone_checker(data['phone'])
        
        if phone_checked != 'fail':
            data['phone'] = await phone_checker(data['phone'])
            await AppealMigration.appeal_migration2.set()
            await bot.send_message(chat_id = message.from_user.id, text='Напишите пожалуйста ваш вопрос ответным сообщением, и я свяжусь с вами в ближайшее время', reply_markup=consultation_keyboard_in_abort)
        else:
            await AppealMigration.appeal_migration1.set()
            await bot.send_message(chat_id = message.from_user.id, text='Некорректно введён номер телефона, пожалуйста повторите, начиная с "+7" (или с другим кодом), без пробелов или тире', reply_markup=consultation_keyboard_in_only_telegram)

async def consultation_migration_add_appeal(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['user_id'] = message.chat.id
        if message.from_user.username == None:
            data['nickname'] = ''
        else:
            data['nickname'] = message.from_user.username
        data['fullname'] = message.from_user.full_name
        data['section'] = 'Миграция'
        current_datetime = datetime.now()
        data['datetime'] = str(current_datetime)[0:-7]
        data['appeal'] = message.text
    await data_base.sql_add_appeal(state)
    await bot.send_message(chat_id = message.from_user.id, text='Спасибо за ваше обращение! Я свяжусь с вами в ближайшее время. Мы работаем с 10:00 до 20:00 (МСК) по будням, в выходные мы отдыхаем', reply_markup=consultation_keyboard_in_migration)
    await bot.send_message(chat_id = message.from_user.id, text='Помимо этого, рад презентовать вам свой чек-лист "Переезд из России: деньги и документы" по ссылке ниже:\nhttps://drive.google.com/file/d/1Y2rMo_GcgpF3ck2NzU0JPbQU2of3VQpT/view')
    await state.finish()

# Трудовые споры

async def consultation_employment(message: types.Message):
    await AppealEmployment.appeal_employment1.set()
    await bot.send_message(chat_id = message.from_user.id, text='Напишите пожалуйста ответным сообщением ваш номер телефона в международном формате с "+7" (или с другим кодом), без пробелов или тире, чтобы я мог связаться с вами', reply_markup=consultation_keyboard_in_only_telegram)

async def consultation_employment_phone_processing(message: typing.Union[types.Contact, types.Message], state: FSMContext):
    async with state.proxy() as data:
        if not message.text:
            data['status'] = 'Свяжитесь со мной в Telegram'
            data['phone'] = message.contact.phone_number
            phone_checked = await phone_checker(data['phone'])
        else:
            data['status'] = 'Позвоните мне'
            data['phone'] = message.text
            phone_checked = await phone_checker(data['phone'])
        
        if phone_checked != 'fail':
            data['phone'] = await phone_checker(data['phone'])
            await AppealEmployment.appeal_employment2.set()
            await bot.send_message(chat_id = message.from_user.id, text='Напишите пожалуйста ваш вопрос ответным сообщением, и я свяжусь с вами в ближайшее время', reply_markup=consultation_keyboard_in_abort)
        else:
            await AppealEmployment.appeal_employment1.set()
            await bot.send_message(chat_id = message.from_user.id, text='Некорректно введён номер телефона, пожалуйста повторите, начиная с "+7" (или с другим кодом), без пробелов или тире', reply_markup=consultation_keyboard_in_only_telegram)

async def consultation_employment_add_appeal(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['user_id'] = message.chat.id
        if message.from_user.username == None:
            data['nickname'] = ''
        else:
            data['nickname'] = message.from_user.username
        data['fullname'] = message.from_user.full_name
        data['section'] = 'Трудовые споры'
        current_datetime = datetime.now()
        data['datetime'] = str(current_datetime)[0:-7]
        data['appeal'] = message.text
    await data_base.sql_add_appeal(state)
    await bot.send_message(chat_id = message.from_user.id, text='Спасибо за ваше обращение! Я свяжусь с вами в ближайшее время. Мы работаем с 10:00 до 20:00 (МСК) по будням, в выходные мы отдыхаем', reply_markup=consultation_keyboard_in_employment)
    await state.finish()

# Защита прав потребителей

async def consultation_consumer(message: types.Message):
    await AppealConsumer.appeal_consumer1.set()
    await bot.send_message(chat_id = message.from_user.id, text='Напишите пожалуйста ответным сообщением ваш номер телефона в международном формате с "+7" (или с другим кодом), без пробелов или тире, чтобы я мог связаться с вами', reply_markup=consultation_keyboard_in_only_telegram)

async def consultation_consumer_phone_processing(message: typing.Union[types.Contact, types.Message], state: FSMContext):
    async with state.proxy() as data:
        if not message.text:
            data['status'] = 'Свяжитесь со мной в Telegram'
            data['phone'] = message.contact.phone_number
            phone_checked = await phone_checker(data['phone'])
        else:
            data['status'] = 'Позвоните мне'
            data['phone'] = message.text
            phone_checked = await phone_checker(data['phone'])
        
        if phone_checked != 'fail':
            data['phone'] = await phone_checker(data['phone'])
            await AppealConsumer.appeal_consumer2.set()
            await bot.send_message(chat_id = message.from_user.id, text='Напишите пожалуйста ваш вопрос ответным сообщением, и я свяжусь с вами в ближайшее время', reply_markup=consultation_keyboard_in_abort)
        else:
            await AppealConsumer.appeal_consumer1.set()
            await bot.send_message(chat_id = message.from_user.id, text='Некорректно введён номер телефона, пожалуйста повторите, начиная с "+7" (или с другим кодом), без пробелов или тире', reply_markup=consultation_keyboard_in_only_telegram)

async def consultation_consumer_add_appeal(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['user_id'] = message.chat.id
        if message.from_user.username == None:
            data['nickname'] = ''
        else:
            data['nickname'] = message.from_user.username
        data['fullname'] = message.from_user.full_name
        data['section'] = 'Защита прав потребителей'
        current_datetime = datetime.now()
        data['datetime'] = str(current_datetime)[0:-7]
        data['appeal'] = message.text
    await data_base.sql_add_appeal(state)
    await bot.send_message(chat_id = message.from_user.id, text='Спасибо за ваше обращение! Я свяжусь с вами в ближайшее время. Мы работаем с 10:00 до 20:00 (МСК) по будням, в выходные мы отдыхаем', reply_markup=consultation_keyboard_in_consumer)
    await state.finish()

# Меню отзывов и замечаний

async def feedback(message: types.Message):
    await AppealFeedback.appeal_feedback1.set()
    await bot.send_message(chat_id = message.from_user.id, text='Вы можете оставить отзыв о нашем сотрудничестве ответным сообщением, и он обязательно будет опубликован в моих социальных сетях. А если у вас есть замечания или предложения по поводу моих услуг, буду рад принять их к сведению', reply_markup=feedback_keyboard_abort)

async def feedback_add_appeal(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['status'] = ''
        data['phone'] = ''
        data['user_id'] = message.chat.id
        if message.from_user.username == None:
            data['nickname'] = ''
        else:
            data['nickname'] = message.from_user.username
        data['fullname'] = message.from_user.full_name
        data['section'] = 'Отзывы'
        current_datetime = datetime.now()
        data['datetime'] = str(current_datetime)[0:-7]
        data['appeal'] = message.text
    await data_base.sql_add_appeal(state)
    await bot.send_message(chat_id = message.from_user.id, text='Благодарю! Я ценю вашу обратную связь', reply_markup=feedback_keyboard)
    await state.finish()

# Меню предложений

async def suggestion(message: types.Message):
    await AppealSuggestion.appeal_suggestion1.set()
    await bot.send_message(chat_id = message.from_user.id, text='Вы можете ознакомиться с моими постами на юридические темы, используя хэштеги по ссылке ниже, и если они пока-что не затронули сферу ваших интересов, можете обратиться ко мне за индивидуальной консультацией из главного меню или предложить тему для нового поста ответным сообщением ниже', reply_markup=suggestion_keyboard_abort)
    await bot.send_message(chat_id = message.from_user.id, text='https://t.me/bettercallpavlukov/480')

async def suggestion_add_appeal(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['status'] = ''
        data['phone'] = ''
        data['user_id'] = message.chat.id
        if message.from_user.username == None:
            data['nickname'] = ''
        else:
            data['nickname'] = message.from_user.username
        data['fullname'] = message.from_user.full_name
        data['section'] = 'Предложения тем для публикаций'
        current_datetime = datetime.now()
        data['datetime'] = str(current_datetime)[0:-7]
        data['appeal'] = message.text
    await data_base.sql_add_appeal(state)
    await bot.send_message(chat_id = message.from_user.id, text='Ваше предложение принято, спасибо!', reply_markup=suggestion_keyboard)
    await state.finish()

# Меню сотрудничества

async def cooperation(message: types.Message):
    await AppealCooperation.appeal_cooperation1.set()
    await bot.send_message(chat_id = message.from_user.id, text='Я всегда открыт для сотрудничества, и вы можете написать мне свои идеи или предложения')
    await bot.send_message(chat_id = message.from_user.id, text='Напишите пожалуйста ответным сообщением ваш номер телефона в международном формате с "+7" (или с другим кодом), без пробелов или тире, чтобы я мог связаться с вами', reply_markup=cooperation_keyboard_in_only_telegram)

async def cooperation_phone_processing(message: typing.Union[types.Contact, types.Message], state: FSMContext):
    async with state.proxy() as data:
        if not message.text:
            data['status'] = 'Свяжитесь со мной в Telegram'
            data['phone'] = message.contact.phone_number
            phone_checked = await phone_checker(data['phone'])
        else:
            data['status'] = 'Позвоните мне'
            data['phone'] = message.text
            phone_checked = await phone_checker(data['phone'])
        
        if phone_checked != 'fail':
            data['phone'] = await phone_checker(data['phone'])
            await AppealCooperation.appeal_cooperation2.set()
            await bot.send_message(chat_id = message.from_user.id, text='Напишите пожалуйста ваше предложение ответным сообщением, и я свяжусь с вами в ближайшее время', reply_markup=cooperation_keyboard_in_abort)
        else:
            await AppealCooperation.appeal_cooperation1.set()
            await bot.send_message(chat_id = message.from_user.id, text='Некорректно введён номер телефона, пожалуйста повторите, начиная с "+7" (или с другим кодом), без пробелов или тире', reply_markup=cooperation_keyboard_in_only_telegram)

async def cooperation_add_appeal(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['user_id'] = message.chat.id
        if message.from_user.username == None:
            data['nickname'] = ''
        else:
            data['nickname'] = message.from_user.username
        data['fullname'] = message.from_user.full_name
        data['section'] = 'Сотрудничество'
        current_datetime = datetime.now()
        data['datetime'] = str(current_datetime)[0:-7]
        data['appeal'] = message.text
    await data_base.sql_add_appeal(state)
    await bot.send_message(chat_id = message.from_user.id, text='Я рассмотрю ваше предложение на тему сотрудничества и свяжусь с вами в самое ближайшее время. Мы работаем с 10:00 до 20:00 (МСК) по будням, в выходные мы отдыхаем', reply_markup=cooperation_keyboard_in)
    await state.finish()

# Обо мне

async def about_me_start_command(message: types.Message):
    await bot.send_photo(chat_id=message.chat.id, photo=open('/home/lines14/projects/judicial_telegram_bot/documents/about_me.jpg', 'rb'))
    await bot.send_message(chat_id = message.from_user.id, text='Еще в школе я знал, что хочу помогать людям. Всегда считал профессию юриста благородной. Перед глазами был пример отца-юриста, который стал моим ориентиром и наставником. В последнем классе я поступил в кадетский класс при Следственном комитете. После школы поступил в МГУ, В 2015 закончил бакалавриат. Во время магистратуры во ВШЭ учился по обмену в Германии. После возвращения имел стойкое желание строить карьеру в международной компании, изучал английский и немецкий языки, чтобы получить должный опыт, а потом основать свою компанию. Отработал в разных компаниях несколько лет, получил много опыта. Именно в это время я понял, что мне нравится заниматься судебными спорами. Но работать на кого-то не очень хотелось, в конце 2017 ушел. На начальных этапах использовал фриланс платформы и нетворкинг. Нашел первых клиентов без использования сторонних сервисов, чем очень горжусь. Еще ни разу не пожалел, что ушел с проторенной дорожки юриста-карьериста и начал самостоятельную деятельность. За 3 года помог 60 клиентам, провел 150 заседаний. В основе моей деятельности работа с гражданами по защите прав потребителей и спорам с работодателями. Однако часто работаю с малым и средним бизнесом. Более 70% моих дел так или иначе связаны с судами')
    await bot.send_message(chat_id = message.from_user.id, text='Подписывайтесь на мои социальные сети, чтобы быть в курсе всех юридических новостей:', reply_markup=socials_inline_keyboard)

# async def about_me_telegram(message: types.Message):
#     await bot.send_message(chat_id = message.from_user.id, text='https://t.me/bettercallpavlukov', reply_markup=about_me_keyboard)

# async def about_me_instagram(message: types.Message):
#     await bot.send_message(chat_id = message.from_user.id, text='https://www.instagram.com/bettercallpavlukov/', reply_markup=about_me_keyboard)

# async def about_me_vk(message: types.Message):
#     await bot.send_message(chat_id = message.from_user.id, text='https://vk.com/yaroslaw_org', reply_markup=about_me_keyboard)

# Меню генератора документов:

# async def generator_start_command(message: types.Message):
#     await bot.send_message(chat_id = message.from_user.id, text='Добро пожаловать в сервис генерации судебных документов. Нажмите кнопку "Создать", а затем введите требуемые данные, чтобы сформировать документ. Или можете посмотреть пример готового документа, нажав кнопку "Пример"', reply_markup=doc_generator_start_keyboard)

# async def get_example(message: types.Message):
#     await message.reply_document(open('/home/lines14/projects/judicial_telegram_bot/example/document_example.docx', 'rb'))

# async def add_data(message: types.Message):
#     await DocGenerator.doc_generator1.set()
#     await message.reply('Введите название инстанции для обращения:', reply_markup=cancel_generator_keyboard)

# async def cancel_handlers_pick_data(message: types.Message, state: FSMContext):
#     current_state = await state.get_state()
#     if current_state is None:
#         return
#     await state.finish()
#     await message.reply('Вы можете начать заново с нажатия кнопки "Создать"', reply_markup=doc_generator_start_keyboard)

# async def doc_generator1(message: types.Message, state: FSMContext):
#     async with state.proxy() as data:
#         data['user_data1'] = message.text
#     await DocGenerator.next()
#     await bot.send_message(chat_id = message.from_user.id, text='Укажите адрес инстанции для обращения:')

# async def doc_generator2(message: types.Message, state: FSMContext):
#     async with state.proxy() as data:
#         data['user_data2'] = message.text
#     await DocGenerator.next()
#     await bot.send_message(chat_id = message.from_user.id, text='Введите ФИО истца:')

# async def doc_generator3(message: types.Message, state: FSMContext):
#     async with state.proxy() as data:
#         data['user_data3'] = message.text
#     await DocGenerator.next()
#     await bot.send_message(chat_id = message.from_user.id, text='Укажите адрес истца:')

# async def doc_generator4(message: types.Message, state: FSMContext):
#     async with state.proxy() as data:
#         data['user_data4'] = message.text
#     await DocGenerator.next()
#     await bot.send_message(chat_id = message.from_user.id, text='Введите адрес истца для корреспонденции при необходимости:')

# async def doc_generator5(message: types.Message, state: FSMContext):
#     async with state.proxy() as data:
#         data['user_data5'] = message.text
#     await DocGenerator.next()
#     await bot.send_message(chat_id = message.from_user.id, text='Укажите представителя истца при необходимости:')

# async def doc_generator6(message: types.Message, state: FSMContext):
#     async with state.proxy() as data:
#         data['user_data6'] = message.text
#     await DocGenerator.next()
#     await bot.send_message(chat_id = message.from_user.id, text='Введите контактные данные представителя истца:')

# async def doc_generator7(message: types.Message, state: FSMContext):
#     async with state.proxy() as data:
#         data['user_data7'] = message.text
#     await DocGenerator.next()
#     await bot.send_message(chat_id = message.from_user.id, text='Укажите ответчика:')

# async def doc_generator8(message: types.Message, state: FSMContext):
#     async with state.proxy() as data:
#         data['user_data8'] = message.text
#     await DocGenerator.next()
#     await bot.send_message(chat_id = message.from_user.id, text='Введите адрес ответчика:')

# async def doc_generator9(message: types.Message, state: FSMContext):
#     async with state.proxy() as data:
#         data['user_data9'] = message.text
#     await DocGenerator.next()
#     await bot.send_message(chat_id = message.from_user.id, text='Укажите номер дела:')

# async def doc_generator10(message: types.Message, state: FSMContext):
#     async with state.proxy() as data:
#         data['user_data10'] = message.text
#     await DocGenerator.next()
#     await bot.send_message(chat_id = message.from_user.id, text='Введите дату подачи Вашего обращения:')

# async def doc_generator11(message: types.Message, state: FSMContext):
#     async with state.proxy() as data:
#         data['user_data11'] = message.text
#     await DocGenerator.next()
#     await bot.send_message(chat_id = message.from_user.id, text='Сформулируйте текст Вашего обращения:')

# async def doc_generator12(message: types.Message, state: FSMContext):
#     async with state.proxy() as data:
#         data['user_data12'] = message.text
#     await DocGenerator.next()
#     await bot.send_message(chat_id = message.from_user.id, text='Укажите процессуальный статус обращающегося:')

# async def doc_generator13(message: types.Message, state: FSMContext):
#     async with state.proxy() as data:
#         data['user_data13'] = message.text
#     await DocGenerator.next()
#     await bot.send_message(chat_id = message.from_user.id, text='Введите инициалы обращающегося:')

# async def doc_generator14(message: types.Message, state: FSMContext):
#     async with state.proxy() as data:
#         data['user_data14'] = message.text
#     await data_print(state)
#     await bot.send_message(chat_id = message.from_user.id, text='Указанные Вами данные приняты, нажмите кнопку "Получить", чтобы выгрузить готовый документ', reply_markup=doc_generator_finish_keyboard)
#     await state.finish()

# async def get_file(message: types.Message):
#     await message.reply_document(open('/home/lines14/projects/judicial_telegram_bot/documents/your_document.docx', 'rb'))

# Регистратура хэндлеров бота

def register_handler_client(dp: Dispatcher):

    # Регистраторы диалога приветствия и главного меню со сборщиками данных

    dp.register_message_handler(start_command, commands=['start'])
    dp.register_callback_query_handler(start_inline_keyboard_callback_pick, text='yes')
    dp.register_callback_query_handler(start_inline_keyboard_callback_redirect, text='no')
    dp.register_message_handler(restart_command, text=['Главное меню', 'Спасибо, буду ждать'])
    dp.register_callback_query_handler(restart_command_inline, text=['To main menu', 'Thank you'])
    dp.register_message_handler(recomendations_after, text=['Хочу почитать посты на тему мобилизации', 'Хочу почитать посты на тему миграции', 'Хочу почитать посты на тему трудовых споров', 'Хочу почитать посты на тему защиты прав потребителей'])
    dp.register_callback_query_handler(recomendations_after_inline, text=['Read mobilization', 'Read migration', 'Read employment', 'Read consumer'])
    dp.register_message_handler(restart_command_for_all_FSM, state='*', text='В главное меню')
    dp.register_message_handler(consultation_start_command, text='Получить консультацию')
    # dp.register_message_handler(generator_start_command, text='Генератор судебных документов')
    dp.register_message_handler(about_me_start_command, text='Обо мне')
    dp.register_message_handler(feedback, text='Оставить отзыв или замечание', state=None)
    dp.register_message_handler(feedback_add_appeal, state=AppealFeedback.appeal_feedback1)
    dp.register_message_handler(suggestion, text='Предложить тему для публикации', state=None)
    dp.register_message_handler(suggestion_add_appeal, state=AppealSuggestion.appeal_suggestion1)

    # Регистраторы стартового диалога на тему консультаций со сборщиками данных

    #Мобилизация

    dp.register_callback_query_handler(start_inline_keyboard_callback_mobilization, text='mobilization', state=None)
    dp.register_callback_query_handler(restart_inline_keyboard_callback_pick, state='*', text='missclick')
    dp.register_message_handler(start_inline_keyboard_callback_mobilization_phone_processing, content_types=['contact', 'text'], state=InlineAppealMobilization.inline_appeal_mobilization1)
    dp.register_message_handler(start_inline_keyboard_callback_mobilization_add_appeal, state=InlineAppealMobilization.inline_appeal_mobilization2)

    # Миграция

    dp.register_callback_query_handler(start_inline_keyboard_callback_migration, text='migration', state=None)
    dp.register_callback_query_handler(restart_inline_keyboard_callback_pick, state='*', text='missclick')
    dp.register_message_handler(start_inline_keyboard_callback_migration_phone_processing, content_types=['contact', 'text'], state=InlineAppealMigration.inline_appeal_migration1)
    dp.register_message_handler(start_inline_keyboard_callback_migration_add_appeal, state=InlineAppealMigration.inline_appeal_migration2)

    # Трудовые споры

    dp.register_callback_query_handler(start_inline_keyboard_callback_employment, text='employment', state=None)
    dp.register_callback_query_handler(restart_inline_keyboard_callback_pick, state='*', text='missclick')
    dp.register_message_handler(start_inline_keyboard_callback_employment_phone_processing, content_types=['contact', 'text'], state=InlineAppealEmployment.inline_appeal_employment1)
    dp.register_message_handler(start_inline_keyboard_callback_employment_add_appeal, state=InlineAppealEmployment.inline_appeal_employment2)

    # Защита прав потребителей

    dp.register_callback_query_handler(start_inline_keyboard_callback_consumer, text='consumer', state=None)
    dp.register_callback_query_handler(restart_inline_keyboard_callback_pick, state='*', text='missclick')
    dp.register_message_handler(start_inline_keyboard_callback_consumer_phone_processing, content_types=['contact', 'text'], state=InlineAppealConsumer.inline_appeal_consumer1)
    dp.register_message_handler(start_inline_keyboard_callback_consumer_add_appeal, state=InlineAppealConsumer.inline_appeal_consumer2)
    
    # Регистраторы меню консультаций со сборщиками данных

    dp.register_message_handler(consultation_back, text='Назад')
    dp.register_message_handler(consultation_back_for_consultation_FSM, state='*', text='Вернуться назад')

    # Мобилизация

    dp.register_message_handler(consultation_mobilization, text='Мобилизация', state=None)
    dp.register_message_handler(consultation_mobilization_phone_processing, content_types=['contact', 'text'], state=AppealMobilization.appeal_mobilization1)
    dp.register_message_handler(consultation_mobilization_add_appeal, state=AppealMobilization.appeal_mobilization2)

    # Миграция

    dp.register_message_handler(consultation_migration, text='Миграция', state=None)
    dp.register_message_handler(consultation_migration_phone_processing, content_types=['contact', 'text'], state=AppealMigration.appeal_migration1)
    dp.register_message_handler(consultation_migration_add_appeal, state=AppealMigration.appeal_migration2)

    # Трудовые споры

    dp.register_message_handler(consultation_employment, text='Трудовые споры', state=None)
    dp.register_message_handler(consultation_employment_phone_processing, content_types=['contact', 'text'], state=AppealEmployment.appeal_employment1)
    dp.register_message_handler(consultation_employment_add_appeal, state=AppealEmployment.appeal_employment2)

    # Защита прав потребителей

    dp.register_message_handler(consultation_consumer, text='Защита прав потребителей', state=None)
    dp.register_message_handler(consultation_consumer_phone_processing, content_types=['contact', 'text'], state=AppealConsumer.appeal_consumer1)
    dp.register_message_handler(consultation_consumer_add_appeal, state=AppealConsumer.appeal_consumer2)

    # Регистраторы меню обо мне

    # dp.register_message_handler(about_me_telegram, text='Моя группа в Telegram')
    # dp.register_message_handler(about_me_instagram, text='Мой Instagram')
    # dp.register_message_handler(about_me_vk, text='Мой VK')

    # Регистраторы меню сотрудничества

    dp.register_message_handler(cooperation, text='Сотрудничество', state=None)
    dp.register_message_handler(cooperation_phone_processing, content_types=['contact', 'text'], state=AppealCooperation.appeal_cooperation1)
    dp.register_message_handler(cooperation_add_appeal, state=AppealCooperation.appeal_cooperation2)

    # Регистраторы генератора документов

    # dp.register_message_handler(get_example, text='Пример')
    # dp.register_message_handler(add_data, text='Создать', state=None)
    # dp.register_message_handler(cancel_handlers_pick_data, state='*', text='Отмена')
    # dp.register_message_handler(doc_generator1, state=DocGenerator.doc_generator1)
    # dp.register_message_handler(doc_generator2, state=DocGenerator.doc_generator2)
    # dp.register_message_handler(doc_generator3, state=DocGenerator.doc_generator3)
    # dp.register_message_handler(doc_generator4, state=DocGenerator.doc_generator4)
    # dp.register_message_handler(doc_generator5, state=DocGenerator.doc_generator5)
    # dp.register_message_handler(doc_generator6, state=DocGenerator.doc_generator6)
    # dp.register_message_handler(doc_generator7, state=DocGenerator.doc_generator7)
    # dp.register_message_handler(doc_generator8, state=DocGenerator.doc_generator8)
    # dp.register_message_handler(doc_generator9, state=DocGenerator.doc_generator9)
    # dp.register_message_handler(doc_generator10, state=DocGenerator.doc_generator10)
    # dp.register_message_handler(doc_generator11, state=DocGenerator.doc_generator11)
    # dp.register_message_handler(doc_generator12, state=DocGenerator.doc_generator12)
    # dp.register_message_handler(doc_generator13, state=DocGenerator.doc_generator13)
    # dp.register_message_handler(doc_generator14, state=DocGenerator.doc_generator14)
    # dp.register_message_handler(get_file, text='Получить')
from aiogram import types, Dispatcher
from modules.bot_base import dp, bot
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from modules import data_base
from modules.admin_buttons import admin_menu_keyboard, admin_menu_in_consultations_keyboard, admin_menu_in_consultations_sections_keyboard, inline_admin_menu_in_consultations_mobilization_keyboard, inline_admin_menu_in_consultations_migration_keyboard, inline_admin_menu_in_consultations_employment_keyboard, inline_admin_menu_in_consultations_consumer_keyboard, admin_menu_in_cooperation_keyboard, inline_admin_menu_in_cooperation_keyboard, admin_menu_in_consultations_sections_categories_keyboard
from modules.admin_buttons import keyboard_generator
from modules.admin_buttons import stage_keyboard_generator
from modules.handlers import restart_command_for_all_FSM
# from modules.token import ID

# ADMIN = ID

ADMIN = set()

# Машины состояний бота

class AdminConsultations(StatesGroup):
    admin_consultations1 = State()
    admin_consultations2 = State()
    admin_consultations3 = State()
    admin_consultations4 = State()

class AdminCooperation(StatesGroup):
    admin_cooperation1 = State()
    admin_cooperation2 = State()
    admin_cooperation3 = State()

class AdminSuggestion(StatesGroup):
    admin_suggestion1 = State()
    admin_suggestion2 = State()

class AdminFeedback(StatesGroup):
    admin_feedback1 = State()
    admin_feedback2 = State()

# Хэндлеры бота
# Меню администратора

async def start_admin_command(message: types.Message):
    global ADMIN
    ADMIN.add(message.from_user.id)
    if message.from_user.id in ADMIN:
        # await bot.delete_message(chat_id = message.from_user.id, message_id=message.message_id)
        await bot.send_message(chat_id = message.from_user.id, text='Выберите раздел из меню администратора:', reply_markup=admin_menu_keyboard)

async def restart_command_for_all_FSM_admin_menu(message: types.Message, state: FSMContext):
    global ADMIN
    if message.from_user.id in ADMIN:
        current_state = await state.get_state()
        if current_state is None:
            return
        await state.finish()
        await message.reply('Выберите раздел из меню администратора:', reply_markup=admin_menu_keyboard)

# Меню заявок на консультации

async def admin_consultations(message: types.Message):
    global ADMIN
    if message.from_user.id in ADMIN:
        await AdminConsultations.admin_consultations1.set()
        await bot.send_message(chat_id = message.from_user.id, text='Выберите способ сортировки:', reply_markup=admin_menu_in_consultations_keyboard)

async def all_get_sorted_by_time_desc(message: types.Message, state: FSMContext):
    global ADMIN
    if message.from_user.id in ADMIN:
        await AdminConsultations.next()
        key_list = await data_base.sql_all_get_sorted_by_time_desc()
        await bot.send_message(chat_id = message.from_user.id, text='Выберите заявку:', reply_markup=await keyboard_generator(key_list, 1))

async def all_get_sorted_by_time_asc(message: types.Message, state: FSMContext):
    global ADMIN
    if message.from_user.id in ADMIN:
        await AdminConsultations.next()
        key_list = await data_base.sql_all_get_sorted_by_time_asc()
        await bot.send_message(chat_id = message.from_user.id, text='Выберите заявку:', reply_markup=await keyboard_generator(key_list, 1))

async def admin_consultations_sections(message: types.Message, state: FSMContext):
    global ADMIN
    if message.from_user.id in ADMIN:
        await AdminConsultations.next()
        await bot.send_message(chat_id = message.from_user.id, text='Выберите тематику:', reply_markup=admin_menu_in_consultations_sections_keyboard)

async def forward_to_admin_consultations_sections_categories_or_back_to_admin_consultations_or_query_delivery(message: types.Message, state: FSMContext):
    global ADMIN
    if message.from_user.id in ADMIN:
        if message.text == '<<<':
            await AdminConsultations.admin_consultations1.set()
            await message.reply('Выберите способ сортировки:', reply_markup=admin_menu_in_consultations_keyboard)
        elif message.text == 'Мобилизация':
            await admin_consultations_mobilization(message, state)
        elif message.text == 'Миграция':
            await admin_consultations_migration(message, state)
        elif message.text == 'Трудовые споры':
            await admin_consultations_employment(message, state)
        elif message.text == 'Защита прав потребителей':
            await admin_consultations_consumer(message, state)
        elif message.text == 'Админ меню':
            await restart_command_for_all_FSM_admin_menu(message, state)
        elif message.text == 'Главное меню':
            await restart_command_for_all_FSM(message, state)
        else:
            if len(message.text) > 11 and message.text[11] == '|':
                info = await data_base.sql_get_info(message.text)
                generalize = f'Статус:\n=>\t\t\t{info[0][6]}\nРаздел:\n=>\t\t\t{info[0][5]}\nСпособ связи:\n=>\t\t\t{info[0][0]}\nНомер телефона:\n=>\t\t\t{info[0][1]}\nНикнейм в Telegram:\n=>\t\t\t@{info[0][2]}\nИнициалы:\n=>\t\t\t{info[0][3]}\nДоп. ссылка (может потребоваться добавить в контакты):\n=>\t\t\thttps://t.me/{info[0][1]}\nОбращение:\n=>\t\t\t{info[0][4]}'
                await bot.send_message(chat_id = message.from_user.id, text=generalize, reply_markup=await stage_keyboard_generator(info[0][7]))
            else:
                await AdminConsultations.admin_consultations1.set()
                await message.reply('Выберите способ сортировки:', reply_markup=admin_menu_in_consultations_keyboard)

async def back_to_admin_consultations_sections(message: types.Message, state: FSMContext):
    global ADMIN
    if message.from_user.id in ADMIN:
        await AdminConsultations.admin_consultations2.set()
        await message.reply('Выберите тематику:', reply_markup=admin_menu_in_consultations_sections_keyboard)

async def back_to_admin_consultations_sections_categories_or_query_delivery(message: types.Message, state: FSMContext):
    global ADMIN
    if message.from_user.id in ADMIN:
        if message.text == '<<':
            await AdminConsultations.admin_consultations2.set()
            await message.reply('Выберите тематику:', reply_markup=admin_menu_in_consultations_sections_keyboard)
        else:
            if len(message.text) > 11 and message.text[11] == '|':
                info = await data_base.sql_get_info(message.text)
                generalize = f'Статус:\n=>\t\t\t{info[0][6]}\nРаздел:\n=>\t\t\t{info[0][5]}\nСпособ связи:\n=>\t\t\t{info[0][0]}\nНомер телефона:\n=>\t\t\t{info[0][1]}\nНикнейм в Telegram:\n=>\t\t\t@{info[0][2]}\nИнициалы:\n=>\t\t\t{info[0][3]}\nДоп. ссылка (может потребоваться добавить в контакты):\n=>\t\t\thttps://t.me/{info[0][1]}\nОбращение:\n=>\t\t\t{info[0][4]}'
                await bot.send_message(chat_id = message.from_user.id, text=generalize, reply_markup=await stage_keyboard_generator(info[0][7]))
            else:
                await AdminConsultations.admin_consultations2.set()
                await message.reply('Выберите тематику:', reply_markup=admin_menu_in_consultations_sections_keyboard)

# Мобилизация

async def admin_consultations_mobilization(message: types.Message, state: FSMContext):
    global ADMIN
    if message.from_user.id in ADMIN:
        await AdminConsultations.next()
        await bot.send_message(chat_id = message.from_user.id, text='ㅤ', reply_markup=admin_menu_in_consultations_sections_categories_keyboard)
        await bot.send_message(chat_id = message.from_user.id, text='Выберите способ сортировки:', reply_markup=inline_admin_menu_in_consultations_mobilization_keyboard)

async def mobilization_get_sorted_by_time_desc(message: types.Message, state: FSMContext):
    global ADMIN
    if message.from_user.id in ADMIN:
        await AdminConsultations.next()
        key_list = await data_base.sql_mobilization_get_sorted_by_time_desc()
        await bot.send_message(chat_id = message.from_user.id, text='Выберите заявку:', reply_markup=await keyboard_generator(key_list, 2))

async def mobilization_get_sorted_by_time_asc(message: types.Message, state: FSMContext):
    global ADMIN
    if message.from_user.id in ADMIN:
        await AdminConsultations.next()
        key_list = await data_base.sql_mobilization_get_sorted_by_time_asc()
        await bot.send_message(chat_id = message.from_user.id, text='Выберите заявку:', reply_markup=await keyboard_generator(key_list, 2))

# Миграция

async def admin_consultations_migration(message: types.Message, state: FSMContext):
    global ADMIN
    if message.from_user.id in ADMIN:
        await AdminConsultations.next()
        await bot.send_message(chat_id = message.from_user.id, text='ㅤ', reply_markup=admin_menu_in_consultations_sections_categories_keyboard)
        await bot.send_message(chat_id = message.from_user.id, text='Выберите способ сортировки:', reply_markup=inline_admin_menu_in_consultations_migration_keyboard)

async def migration_get_sorted_by_time_desc(message: types.Message, state: FSMContext):
    global ADMIN
    if message.from_user.id in ADMIN:
        await AdminConsultations.next()
        key_list = await data_base.sql_migration_get_sorted_by_time_desc()
        await bot.send_message(chat_id = message.from_user.id, text='Выберите заявку:', reply_markup=await keyboard_generator(key_list, 2))

async def migration_get_sorted_by_time_asc(message: types.Message, state: FSMContext):
    global ADMIN
    if message.from_user.id in ADMIN:
        await AdminConsultations.next()
        key_list = await data_base.sql_migration_get_sorted_by_time_asc()
        await bot.send_message(chat_id = message.from_user.id, text='Выберите заявку:', reply_markup=await keyboard_generator(key_list, 2))

# Трудовые споры

async def admin_consultations_employment(message: types.Message, state: FSMContext):
    global ADMIN
    if message.from_user.id in ADMIN:
        await AdminConsultations.next()
        await bot.send_message(chat_id = message.from_user.id, text='ㅤ', reply_markup=admin_menu_in_consultations_sections_categories_keyboard)
        await bot.send_message(chat_id = message.from_user.id, text='Выберите способ сортировки:', reply_markup=inline_admin_menu_in_consultations_employment_keyboard)

async def employment_get_sorted_by_time_desc(message: types.Message, state: FSMContext):
    global ADMIN
    if message.from_user.id in ADMIN:
        await AdminConsultations.next()
        key_list = await data_base.sql_employment_get_sorted_by_time_desc()
        await bot.send_message(chat_id = message.from_user.id, text='Выберите заявку:', reply_markup=await keyboard_generator(key_list, 2))

async def employment_get_sorted_by_time_asc(message: types.Message, state: FSMContext):
    global ADMIN
    if message.from_user.id in ADMIN:
        await AdminConsultations.next()
        key_list = await data_base.sql_employment_get_sorted_by_time_asc()
        await bot.send_message(chat_id = message.from_user.id, text='Выберите заявку:', reply_markup=await keyboard_generator(key_list, 2))

# Защита прав потребителей

async def admin_consultations_consumer(message: types.Message, state: FSMContext):
    global ADMIN
    if message.from_user.id in ADMIN:
        await AdminConsultations.next()
        await bot.send_message(chat_id = message.from_user.id, text='ㅤ', reply_markup=admin_menu_in_consultations_sections_categories_keyboard)
        await bot.send_message(chat_id = message.from_user.id, text='Выберите способ сортировки:', reply_markup=inline_admin_menu_in_consultations_consumer_keyboard)

async def consumer_get_sorted_by_time_desc(message: types.Message, state: FSMContext):
    global ADMIN
    if message.from_user.id in ADMIN:
        await AdminConsultations.next()
        key_list = await data_base.sql_consumer_get_sorted_by_time_desc()
        await bot.send_message(chat_id = message.from_user.id, text='Выберите заявку:', reply_markup=await keyboard_generator(key_list, 2))

async def consumer_get_sorted_by_time_asc(message: types.Message, state: FSMContext):
    global ADMIN
    if message.from_user.id in ADMIN:
        await AdminConsultations.next()
        key_list = await data_base.sql_consumer_get_sorted_by_time_asc()
        await bot.send_message(chat_id = message.from_user.id, text='Выберите заявку:', reply_markup=await keyboard_generator(key_list, 2))

# Меню сотрудничества

async def admin_cooperation(message: types.Message):
    global ADMIN
    if message.from_user.id in ADMIN:
        await AdminCooperation.admin_cooperation1.set()
        await bot.send_message(chat_id = message.from_user.id, text='ㅤ', reply_markup=admin_menu_in_cooperation_keyboard)
        await bot.send_message(chat_id = message.from_user.id, text='Выберите способ сортировки:', reply_markup=inline_admin_menu_in_cooperation_keyboard)

async def cooperation_get_sorted_by_time_desc(message: types.Message, state: FSMContext):
    global ADMIN
    if message.from_user.id in ADMIN:
        await AdminCooperation.next()
        key_list = await data_base.sql_cooperation_get_sorted_by_time_desc()
        await bot.send_message(chat_id = message.from_user.id, text='Выберите заявку:', reply_markup=await keyboard_generator(key_list, 3))

async def cooperation_get_sorted_by_time_asc(message: types.Message, state: FSMContext):
    global ADMIN
    if message.from_user.id in ADMIN:
        await AdminCooperation.next()
        key_list = await data_base.sql_cooperation_get_sorted_by_time_asc()
        await bot.send_message(chat_id = message.from_user.id, text='Выберите заявку:', reply_markup=await keyboard_generator(key_list, 3))

async def back_from_cooperation_to_admin_menu_or_query_delivery(message: types.Message, state: FSMContext):
    global ADMIN
    if message.from_user.id in ADMIN:
        if message.text == 'Админ меню':
            await restart_command_for_all_FSM_admin_menu(message, state)
            await message.reply('Выберите раздел из меню администратора:', reply_markup=admin_menu_keyboard)
        else:
            if len(message.text) > 11 and message.text[11] == '|':
                info = await data_base.sql_get_info(message.text)
                generalize = f'Статус:\n=>\t\t\t{info[0][6]}\nСпособ связи:\n=>\t\t\t{info[0][0]}\nНомер телефона:\n=>\t\t\t{info[0][1]}\nНикнейм в Telegram:\n=>\t\t\t@{info[0][2]}\nИнициалы:\n=>\t\t\t{info[0][3]}\nДоп. ссылка (может потребоваться добавить в контакты):\n=>\t\t\thttps://t.me/{info[0][1]}\nОбращение:\n=>\t\t\t{info[0][4]}'
                await bot.send_message(chat_id = message.from_user.id, text=generalize, reply_markup=await stage_keyboard_generator(info[0][7]))
            else:
                await restart_command_for_all_FSM_admin_menu(message, state)
                await message.reply('Выберите раздел из меню администратора:', reply_markup=admin_menu_keyboard)

# Меню предложений тем для публикаций и отзывов

async def admin_suggestion_get_sorted_by_time_desc(message: types.Message):
    global ADMIN
    if message.from_user.id in ADMIN:
        await AdminSuggestion.admin_suggestion1.set()
        key_list = await data_base.sql_suggestion_get_sorted_by_time_desc()
        await bot.send_message(chat_id = message.from_user.id, text='Выберите заявку:', reply_markup=await keyboard_generator(key_list, 3))

async def admin_feedback_get_sorted_by_time_desc(message: types.Message):
    global ADMIN
    if message.from_user.id in ADMIN:
        await AdminFeedback.admin_feedback1.set()
        key_list = await data_base.sql_feedback_get_sorted_by_time_desc()
        await bot.send_message(chat_id = message.from_user.id, text='Выберите заявку:', reply_markup=await keyboard_generator(key_list, 3))

async def back_from_suggestion_or_feedback_to_admin_menu_or_query_delivery(message: types.Message, state: FSMContext):
    global ADMIN
    if message.from_user.id in ADMIN:
        if message.text == 'Админ меню':
            await restart_command_for_all_FSM_admin_menu(message, state)
            await message.reply('Выберите раздел из меню администратора:', reply_markup=admin_menu_keyboard)
        else:
            if len(message.text) > 11 and message.text[11] == '|':
                info = await data_base.sql_get_info(message.text)
                generalize = f'Статус:\n=>\t\t\t{info[0][6]}\nНикнейм в Telegram:\n=>\t\t\t@{info[0][2]}\nИнициалы:\n=>\t\t\t{info[0][3]}\nОтзыв:\n=>\t\t\t{info[0][4]}'
                await bot.send_message(chat_id = message.from_user.id, text=generalize, reply_markup=await stage_keyboard_generator(info[0][7]))
            else:
                await restart_command_for_all_FSM_admin_menu(message, state)
                await message.reply('Выберите раздел из меню администратора:', reply_markup=admin_menu_keyboard)

# Смена статуса заявок

async def stage_changer(callback: types.CallbackQuery, state: FSMContext):
    global ADMIN
    if callback.from_user.id in ADMIN:
        callback_exceptions_list = ['yes', 'no', 'To main menu', 'Thank you', 'Read mobilization', 'Read migration', 'Read employment', 'Read consumer', 'mobilization', 'missclick', 'missclick_markup', 'migration', 'employment', 'consumer', 'mobilization_new', 'mobilization_old', 'migration_new', 'migration_old', 'employment_new', 'employment_old', 'consumer_new', 'consumer_old', 'cooperation_new', 'cooperation_old']
        if callback.data not in callback_exceptions_list:
            callback_slicer_1 = ''.join(callback.data.split(' ')[slice(1)])
            callback_slicer_2 = ' '.join(callback.data.split(' ')[slice(1,3)])
            if callback_slicer_1 == 'inwork':
                await data_base.sql_stage_changer(callback_slicer_2, 'В работе')
                # await bot.send_message(chat_id = callback.from_user.id, text=f'В работе {callback_slicer_2}')
            else:
                await data_base.sql_stage_changer(callback_slicer_2, 'Завершено')
                # await bot.send_message(chat_id = callback.from_user.id, text=f'Завершили {callback_slicer_2}')

# Регистратура хэндлеров бота

def register_handler_admin(dp: Dispatcher):

    # Регистраторы меню администратора

    dp.register_message_handler(start_admin_command, commands=['1959'], is_chat_admin = True) # is_chat_admin = True
    dp.register_message_handler(restart_command_for_all_FSM_admin_menu, state='*', text='Админ меню')

    # Регистраторы меню заявок на консультации

    dp.register_message_handler(admin_consultations, text='Заявки на консультации', state=None)
    dp.register_message_handler(all_get_sorted_by_time_desc, text='Самые новые', state=AdminConsultations.admin_consultations1)
    dp.register_message_handler(all_get_sorted_by_time_asc, text='Долго ждут', state=AdminConsultations.admin_consultations1)
    dp.register_message_handler(admin_consultations_sections, text='По тематике', state=AdminConsultations.admin_consultations1)
    dp.register_message_handler(forward_to_admin_consultations_sections_categories_or_back_to_admin_consultations_or_query_delivery, state=AdminConsultations.admin_consultations2)
    dp.register_message_handler(back_to_admin_consultations_sections, text='<<', state=AdminConsultations.admin_consultations3)
    dp.register_message_handler(back_to_admin_consultations_sections_categories_or_query_delivery, state=AdminConsultations.admin_consultations4)

    # Мобилизация

    dp.register_message_handler(admin_consultations_mobilization, text='Мобилизация', state=AdminConsultations.admin_consultations2)
    dp.register_callback_query_handler(mobilization_get_sorted_by_time_desc, text='mobilization_new', state=AdminConsultations.admin_consultations3)
    dp.register_callback_query_handler(mobilization_get_sorted_by_time_asc, text='mobilization_old', state=AdminConsultations.admin_consultations3)

    # Миграция

    dp.register_message_handler(admin_consultations_migration, text='Миграция', state=AdminConsultations.admin_consultations2)
    dp.register_callback_query_handler(migration_get_sorted_by_time_desc, text='migration_new', state=AdminConsultations.admin_consultations3)
    dp.register_callback_query_handler(migration_get_sorted_by_time_asc, text='migration_old', state=AdminConsultations.admin_consultations3)

    # Трудовые споры

    dp.register_message_handler(admin_consultations_employment, text='Трудовые споры', state=AdminConsultations.admin_consultations2)
    dp.register_callback_query_handler(employment_get_sorted_by_time_desc, text='employment_new', state=AdminConsultations.admin_consultations3)
    dp.register_callback_query_handler(employment_get_sorted_by_time_asc, text='employment_old', state=AdminConsultations.admin_consultations3)

    # Защита прав потребителей

    dp.register_message_handler(admin_consultations_consumer, text='Защита прав потребителей', state=AdminConsultations.admin_consultations2)
    dp.register_callback_query_handler(consumer_get_sorted_by_time_desc, text='consumer_new', state=AdminConsultations.admin_consultations3)
    dp.register_callback_query_handler(consumer_get_sorted_by_time_asc, text='consumer_old', state=AdminConsultations.admin_consultations3)

    # Регистраторы меню сотрудничества

    dp.register_message_handler(admin_cooperation, text='Предложения сотрудничества', state=None)
    dp.register_callback_query_handler(cooperation_get_sorted_by_time_desc, text='cooperation_new', state=AdminCooperation.admin_cooperation1)
    dp.register_callback_query_handler(cooperation_get_sorted_by_time_asc, text='cooperation_old', state=AdminCooperation.admin_cooperation1)
    dp.register_message_handler(back_from_cooperation_to_admin_menu_or_query_delivery, state=AdminCooperation.admin_cooperation2)

    # Регистраторы меню предложений тем для публикаций и отзывов

    dp.register_message_handler(admin_suggestion_get_sorted_by_time_desc, text='Предложения тем для публикаций', state=None)
    dp.register_message_handler(back_from_suggestion_or_feedback_to_admin_menu_or_query_delivery, state=AdminSuggestion.admin_suggestion1)
    dp.register_message_handler(admin_feedback_get_sorted_by_time_desc, text='Отзывы', state=None)
    dp.register_message_handler(back_from_suggestion_or_feedback_to_admin_menu_or_query_delivery, state=AdminFeedback.admin_feedback1)

    dp.register_callback_query_handler(stage_changer, state='*')


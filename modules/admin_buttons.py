from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

a0 = KeyboardButton('Все заявки')
a1 = KeyboardButton('Заявки на консультации')
a2 = KeyboardButton('Предложения сотрудничества')
a3 = KeyboardButton('Предложения тем для публикаций')
a4 = KeyboardButton('Отзывы')
a5 = KeyboardButton('Главное меню')
a6 = KeyboardButton('Админ меню')
a7 = KeyboardButton('<<<')
a8 = KeyboardButton('<<')

a9 = KeyboardButton('По тематике')
a10 = KeyboardButton('Мобилизация')
a11 = KeyboardButton('Миграция')
a12 = KeyboardButton('Трудовые споры')
a13 = KeyboardButton('Защита прав потребителей')
a14 = KeyboardButton('Другие темы')

a15 = KeyboardButton('Самые новые')
a16 = KeyboardButton('Долго ждут')

a17 = KeyboardButton('Архив')
a18 = KeyboardButton('Статистика')

i1 = InlineKeyboardButton(text='Самые новые', callback_data='mobilization_new')
i2 = InlineKeyboardButton(text='Долго ждут', callback_data='mobilization_old')
i3 = InlineKeyboardButton(text='Самые новые', callback_data='migration_new')
i4 = InlineKeyboardButton(text='Долго ждут', callback_data='migration_old')
i5 = InlineKeyboardButton(text='Самые новые', callback_data='employment_new')
i6 = InlineKeyboardButton(text='Долго ждут', callback_data='employment_old')
i7 = InlineKeyboardButton(text='Самые новые', callback_data='consumer_new')
i8 = InlineKeyboardButton(text='Долго ждут', callback_data='consumer_old')
i9 = InlineKeyboardButton(text='Самые новые', callback_data='cooperation_new')
i10 = InlineKeyboardButton(text='Долго ждут', callback_data='cooperation_old')
i11 = InlineKeyboardButton(text='Самые новые', callback_data='another_new')
i12 = InlineKeyboardButton(text='Долго ждут', callback_data='another_old')

# i13 = InlineKeyboardButton(text='В работе', callback_data='inwork')
# i14 = InlineKeyboardButton(text='Завершено', callback_data='closed')

admin_menu_keyboard = ReplyKeyboardMarkup(resize_keyboard=True) # one_time_keyboard=True .insert(b6)
admin_menu_keyboard.add(a0).insert(a1).add(a2).insert(a3).add(a4).insert(a17).add(a18).insert(a5)

admin_menu_in_consultations_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
admin_menu_in_consultations_keyboard.add(a9).insert(a15).insert(a16).add(a6).insert(a5)

admin_menu_in_consultations_sections_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
admin_menu_in_consultations_sections_keyboard.add(a10).insert(a11).insert(a12).add(a7).insert(a13).insert(a14).add(a6).insert(a5)

admin_menu_in_consultations_sections_categories_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
admin_menu_in_consultations_sections_categories_keyboard.add(a8).insert(a6).insert(a5)

inline_admin_menu_in_consultations_mobilization_keyboard = InlineKeyboardMarkup(row_width=1)
inline_admin_menu_in_consultations_mobilization_keyboard.add(i1).add(i2)

inline_admin_menu_in_consultations_migration_keyboard = InlineKeyboardMarkup(row_width=1)
inline_admin_menu_in_consultations_migration_keyboard.add(i3).add(i4)

inline_admin_menu_in_consultations_employment_keyboard = InlineKeyboardMarkup(row_width=1)
inline_admin_menu_in_consultations_employment_keyboard.add(i5).add(i6)

inline_admin_menu_in_consultations_consumer_keyboard = InlineKeyboardMarkup(row_width=1)
inline_admin_menu_in_consultations_consumer_keyboard.add(i7).add(i8)

inline_admin_menu_in_consultations_another_keyboard = InlineKeyboardMarkup(row_width=1)
inline_admin_menu_in_consultations_another_keyboard.add(i11).add(i12)

admin_menu_in_cooperation_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
admin_menu_in_cooperation_keyboard.add(a6).insert(a5)

inline_admin_menu_in_cooperation_keyboard = InlineKeyboardMarkup(row_width=1)
inline_admin_menu_in_cooperation_keyboard.add(i9).add(i10)

# inline_status_keyboard = InlineKeyboardMarkup(row_width=1)
# inline_status_keyboard.add(i13).add(i14)

# Генератор клавиатур

# keyboard: Optional[List[List[KeyboardButton]]] = None
# key_list = ['1', '2', '3']

async def keyboard_generator(key_list, menu_section, direction, typo):
    if direction == 'desc':
        if menu_section == 1:
            tmp_buttons = []
            tmp_buttons.append([KeyboardButton('<<<')])
            tmp_buttons.append([KeyboardButton('Обновить ⬇️')])
            for i in key_list:
                tmp_buttons.append([KeyboardButton(i)])
            keyboard = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=tmp_buttons)
            return keyboard
        elif menu_section ==2:
            if typo == 'mobilization':
                tmp_buttons = []
                tmp_buttons.append([KeyboardButton('<<')])
                tmp_buttons.append([KeyboardButton('Обновить ⬇️')])
                for i in key_list:
                    tmp_buttons.append([KeyboardButton(i)])
                keyboard = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=tmp_buttons)
                return keyboard
            elif typo == 'migration':
                tmp_buttons = []
                tmp_buttons.append([KeyboardButton('<<')])
                tmp_buttons.append([KeyboardButton('Обновить ⬇️')])
                for i in key_list:
                    tmp_buttons.append([KeyboardButton(i)])
                keyboard = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=tmp_buttons)
                return keyboard
            elif typo == 'employment':
                tmp_buttons = []
                tmp_buttons.append([KeyboardButton('<<')])
                tmp_buttons.append([KeyboardButton('Обновить ⬇️')])
                for i in key_list:
                    tmp_buttons.append([KeyboardButton(i)])
                keyboard = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=tmp_buttons)
                return keyboard
            elif typo == 'consumer':
                tmp_buttons = []
                tmp_buttons.append([KeyboardButton('<<')])
                tmp_buttons.append([KeyboardButton('Обновить ⬇️')])
                for i in key_list:
                    tmp_buttons.append([KeyboardButton(i)])
                keyboard = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=tmp_buttons)
                return keyboard
            else:
                tmp_buttons = []
                tmp_buttons.append([KeyboardButton('<<')])
                tmp_buttons.append([KeyboardButton('Обновить ⬇️')])
                for i in key_list:
                    tmp_buttons.append([KeyboardButton(i)])
                keyboard = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=tmp_buttons)
                return keyboard
        else:
            if typo == 'cooperation':
                tmp_buttons = []
                tmp_buttons.append([KeyboardButton('Админ меню')])
                tmp_buttons.append([KeyboardButton('Обновить ⬇️')])
                for i in key_list:
                    tmp_buttons.append([KeyboardButton(i)])
                keyboard = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=tmp_buttons)
                return keyboard
            elif typo == 'suggestion':
                tmp_buttons = []
                tmp_buttons.append([KeyboardButton('Админ меню')])
                tmp_buttons.append([KeyboardButton('Обновить ⬇️')])
                for i in key_list:
                    tmp_buttons.append([KeyboardButton(i)])
                keyboard = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=tmp_buttons)
                return keyboard
            elif typo == 'feedback':
                tmp_buttons = []
                tmp_buttons.append([KeyboardButton('Админ меню')])
                tmp_buttons.append([KeyboardButton('Обновить ⬇️')])
                for i in key_list:
                    tmp_buttons.append([KeyboardButton(i)])
                keyboard = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=tmp_buttons)
                return keyboard
            elif typo == 'archive':
                tmp_buttons = []
                tmp_buttons.append([KeyboardButton('Админ меню')])
                tmp_buttons.append([KeyboardButton('Обновить ⬇️')])
                for i in key_list:
                    tmp_buttons.append([KeyboardButton(i)])
                keyboard = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=tmp_buttons)
                return keyboard
            else:
                tmp_buttons = []
                tmp_buttons.append([KeyboardButton('Админ меню')])
                tmp_buttons.append([KeyboardButton('Обновить ⬇️')])
                for i in key_list:
                    tmp_buttons.append([KeyboardButton(i)])
                keyboard = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=tmp_buttons)
                return keyboard
    else:
        if menu_section == 1:
            tmp_buttons = []
            tmp_buttons.append([KeyboardButton('<<<')])
            tmp_buttons.append([KeyboardButton('Обновить ⬆️')])
            for i in key_list:
                tmp_buttons.append([KeyboardButton(i)])
            keyboard = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=tmp_buttons)
            return keyboard
        elif menu_section ==2:
            if typo == 'mobilization':
                tmp_buttons = []
                tmp_buttons.append([KeyboardButton('<<')])
                tmp_buttons.append([KeyboardButton('Обновить ⬆️')])
                for i in key_list:
                    tmp_buttons.append([KeyboardButton(i)])
                keyboard = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=tmp_buttons)
                return keyboard
            elif typo == 'migration':
                tmp_buttons = []
                tmp_buttons.append([KeyboardButton('<<')])
                tmp_buttons.append([KeyboardButton('Обновить ⬆️')])
                for i in key_list:
                    tmp_buttons.append([KeyboardButton(i)])
                keyboard = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=tmp_buttons)
                return keyboard
            elif typo == 'employment':
                tmp_buttons = []
                tmp_buttons.append([KeyboardButton('<<')])
                tmp_buttons.append([KeyboardButton('Обновить ⬆️')])
                for i in key_list:
                    tmp_buttons.append([KeyboardButton(i)])
                keyboard = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=tmp_buttons)
                return keyboard
            elif typo == 'consumer':
                tmp_buttons = []
                tmp_buttons.append([KeyboardButton('<<')])
                tmp_buttons.append([KeyboardButton('Обновить ⬆️')])
                for i in key_list:
                    tmp_buttons.append([KeyboardButton(i)])
                keyboard = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=tmp_buttons)
                return keyboard
            else:
                tmp_buttons = []
                tmp_buttons.append([KeyboardButton('<<')])
                tmp_buttons.append([KeyboardButton('Обновить ⬆️')])
                for i in key_list:
                    tmp_buttons.append([KeyboardButton(i)])
                keyboard = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=tmp_buttons)
                return keyboard
        else:
            if typo == 'cooperation':
                tmp_buttons = []
                tmp_buttons.append([KeyboardButton('Админ меню')])
                tmp_buttons.append([KeyboardButton('Обновить ⬆️')])
                for i in key_list:
                    tmp_buttons.append([KeyboardButton(i)])
                keyboard = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=tmp_buttons)
                return keyboard
            elif typo == 'suggestion':
                tmp_buttons = []
                tmp_buttons.append([KeyboardButton('Админ меню')])
                tmp_buttons.append([KeyboardButton('Обновить ⬆️')])
                for i in key_list:
                    tmp_buttons.append([KeyboardButton(i)])
                keyboard = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=tmp_buttons)
                return keyboard
            elif typo == 'feedback':
                tmp_buttons = []
                tmp_buttons.append([KeyboardButton('Админ меню')])
                tmp_buttons.append([KeyboardButton('Обновить ⬆️')])
                for i in key_list:
                    tmp_buttons.append([KeyboardButton(i)])
                keyboard = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=tmp_buttons)
                return keyboard
            elif typo == 'archive':
                tmp_buttons = []
                tmp_buttons.append([KeyboardButton('Админ меню')])
                tmp_buttons.append([KeyboardButton('Обновить ⬆️')])
                for i in key_list:
                    tmp_buttons.append([KeyboardButton(i)])
                keyboard = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=tmp_buttons)
                return keyboard
            else:
                tmp_buttons = []
                tmp_buttons.append([KeyboardButton('Админ меню')])
                tmp_buttons.append([KeyboardButton('Обновить ⬆️')])
                for i in key_list:
                    tmp_buttons.append([KeyboardButton(i)])
                keyboard = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=tmp_buttons)
                return keyboard

# Генератор инлайн клавиатур статусов

async def stage_keyboard_generator(identifier):
    inline_buttons = InlineKeyboardMarkup()
    inline_buttons.row_width = 1
    inline_buttons.add(InlineKeyboardButton(text='В работе', callback_data=f'inwork {identifier}'))
    inline_buttons.add(InlineKeyboardButton(text='Завершено', callback_data=f'closed {identifier}'))
    return inline_buttons
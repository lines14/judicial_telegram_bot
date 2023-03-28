from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

k0 = InlineKeyboardButton(text='Задать вопрос', callback_data='another')
k1 = InlineKeyboardButton(text='Да', callback_data='yes')
k2 = InlineKeyboardButton(text='Нет, у меня другой вопрос', callback_data='no')
k3 = InlineKeyboardButton(text='В главное меню', callback_data='nope')

k4 = InlineKeyboardButton(text='Мобилизация', callback_data='mobilization')
k5 = InlineKeyboardButton(text='Миграция', callback_data='migration')
k6 = InlineKeyboardButton(text='Трудовые споры', callback_data='employment')
k7 = InlineKeyboardButton(text='Защита прав потребителей', callback_data='consumer')
k8 = InlineKeyboardButton(text='Хочу обратиться по другой теме', callback_data='missclick_markup')
k9 = InlineKeyboardButton(text='Хочу обратиться по другой теме', callback_data='missclick')

k10 = InlineKeyboardButton(text='Моя группа в Telegram', url='https://t.me/bettercallpavlukov')
k11 = InlineKeyboardButton(text='Мой Instagram', url='https://www.instagram.com/bettercallpavlukov/')
k12 = InlineKeyboardButton(text='Мой VK', url='https://vk.com/yaroslaw_org')

k13 = InlineKeyboardButton(text='Спасибо, буду ждать', callback_data='Thank you')
k14 = InlineKeyboardButton(text='Хочу почитать посты на тему мобилизации', callback_data='Read mobilization')
k15 = InlineKeyboardButton(text='Хочу почитать посты на тему миграции', callback_data='Read migration')
k16 = InlineKeyboardButton(text='Хочу почитать посты на тему трудовых споров', callback_data='Read employment')
k17 = InlineKeyboardButton(text='Хочу почитать посты на тему защиты прав потребителей', callback_data='Read consumer')
k18 = InlineKeyboardButton(text='Хочу почитать посты', callback_data='Read another')

k19 = InlineKeyboardButton(text='Главное меню', callback_data='To main menu')

b0 = KeyboardButton('Задать вопрос')
b1 = KeyboardButton('Получить консультацию')
b2 = KeyboardButton('Оставить отзыв или замечание')
b3 = KeyboardButton('Сотрудничество')
b4 = KeyboardButton('Предложить тему для публикации')
b5 = KeyboardButton('Обо мне')
b6 = KeyboardButton('Генератор судебных документов')
b7 = KeyboardButton('Главное меню')
b8 = KeyboardButton('Назад')

b9 = KeyboardButton('Создать')
b10 = KeyboardButton('Пример')
b11 = KeyboardButton('Отмена')
b12 = KeyboardButton('Получить')

b13 = KeyboardButton('Мобилизация')
b14 = KeyboardButton('Миграция')
b15 = KeyboardButton('Трудовые споры')
b16 = KeyboardButton('Защита прав потребителей')

b17 = KeyboardButton('Спасибо, буду ждать')
b18 = KeyboardButton('Хочу почитать посты на тему мобилизации')
b19 = KeyboardButton('Хочу почитать посты на тему миграции')
b20 = KeyboardButton('Хочу почитать посты на тему трудовых споров')
b21 = KeyboardButton('Хочу почитать посты на тему защиты прав потребителей')
b22 = KeyboardButton('Хочу почитать посты')

b23 = KeyboardButton('Свяжитесь со мной в Telegram', request_contact=True)

# b23 = KeyboardButton('Моя группа в Telegram')
# b24 = KeyboardButton('Мой Instagram')
# b25 = KeyboardButton('Мой VK')

intro_inline_keyboard = InlineKeyboardMarkup(row_width=1)
intro_inline_keyboard.add(k1).add(k2)

consultation_inline_keyboard = InlineKeyboardMarkup(row_width=1)
consultation_inline_keyboard.add(k4).add(k5).add(k6).add(k7).add(k0).add(k3)

consultation_inline_keyboard_phone_keeper = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
consultation_inline_keyboard_phone_keeper.add(b23)

consultation_inline_keyboard_missclick_markup = InlineKeyboardMarkup(row_width=1)
consultation_inline_keyboard_missclick_markup.add(k8)

consultation_inline_keyboard_missclick = InlineKeyboardMarkup(row_width=1)
consultation_inline_keyboard_missclick.add(k9)

socials_inline_keyboard = InlineKeyboardMarkup(row_width=1)
socials_inline_keyboard.add(k10).add(k11).add(k12)

main_menu_keyboard = ReplyKeyboardMarkup(resize_keyboard=True) # one_time_keyboard=True .insert(b6)
main_menu_keyboard.add(b1).insert(b2).add(b3).insert(b4).add(b5)

to_the_main_menu_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
to_the_main_menu_keyboard.add(b7)

consultation_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
consultation_keyboard.add(b13).insert(b14).insert(b15).add(b16).insert(b0).insert(b7)

consultation_keyboard_in_mobilization = ReplyKeyboardMarkup(resize_keyboard=True)
consultation_keyboard_in_mobilization.add(b17).insert(b18)

consultation_keyboard_in_migration = ReplyKeyboardMarkup(resize_keyboard=True)
consultation_keyboard_in_migration.add(b17).insert(b19)

consultation_keyboard_in_employment = ReplyKeyboardMarkup(resize_keyboard=True)
consultation_keyboard_in_employment.add(b17).insert(b20)

consultation_keyboard_in_consumer = ReplyKeyboardMarkup(resize_keyboard=True)
consultation_keyboard_in_consumer.add(b17).add(b21)

consultation_keyboard_in_another = ReplyKeyboardMarkup(resize_keyboard=True)
consultation_keyboard_in_another.add(b17).insert(b22)

consultation_keyboard_in_only_telegram = ReplyKeyboardMarkup(resize_keyboard=True)
consultation_keyboard_in_only_telegram.add(b23).add(b8).insert(b7)

consultation_keyboard_in_abort = ReplyKeyboardMarkup(resize_keyboard=True)
consultation_keyboard_in_abort.add(b8).insert(b7)

consultation_keyboard_in_after_inline_mobilization = InlineKeyboardMarkup(row_width=1)
consultation_keyboard_in_after_inline_mobilization.add(k13).add(k14)

consultation_keyboard_in_after_inline_migration = InlineKeyboardMarkup(row_width=1)
consultation_keyboard_in_after_inline_migration.add(k13).add(k15)

consultation_keyboard_in_after_inline_employment = InlineKeyboardMarkup(row_width=1)
consultation_keyboard_in_after_inline_employment.add(k13).add(k16)

consultation_keyboard_in_after_inline_consumer = InlineKeyboardMarkup(row_width=1)
consultation_keyboard_in_after_inline_consumer.add(k13).add(k17)

consultation_keyboard_in_after_inline_another = InlineKeyboardMarkup(row_width=1)
consultation_keyboard_in_after_inline_another.add(k13).add(k18)

consultation_keyboard_in_after_inline_recomendations = InlineKeyboardMarkup(row_width=1)
consultation_keyboard_in_after_inline_recomendations.add(k19)

cooperation_keyboard_in_only_telegram = ReplyKeyboardMarkup(resize_keyboard=True)
cooperation_keyboard_in_only_telegram.add(b23).add(b7)

# about_me_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
# about_me_keyboard.add(b17).insert(b18).insert(b19).add(b7)

doc_generator_start_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
doc_generator_start_keyboard.add(b9).insert(b10).insert(b7)

cancel_generator_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
cancel_generator_keyboard.add(b11)

doc_generator_finish_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
doc_generator_finish_keyboard.add(b9).insert(b12).insert(b7)
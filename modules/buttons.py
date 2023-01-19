from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

k1 = InlineKeyboardButton(text='Хочу получить консультацию', callback_data='yes')
k2 = InlineKeyboardButton(text='Хочу обратиться по другой теме', callback_data='no')

k3 = InlineKeyboardButton(text='Мобилизация', callback_data='mobilization')
k4 = InlineKeyboardButton(text='Миграция', callback_data='migration')
k5 = InlineKeyboardButton(text='Трудовые споры', callback_data='employment')
k6 = InlineKeyboardButton(text='Защита прав потребителей', callback_data='consumer')

k7 = InlineKeyboardButton(text='Моя группа в Telegram', url='https://t.me/bettercallpavlukov')
k8 = InlineKeyboardButton(text='Мой Instagram', url='https://www.instagram.com/bettercallpavlukov/')
k9 = InlineKeyboardButton(text='Мой VK', url='https://vk.com/yaroslaw_org')

b1 = KeyboardButton('Получить консультацию')
b2 = KeyboardButton('Оставить отзыв или замечание')
b3 = KeyboardButton('Сотрудничество')
b4 = KeyboardButton('Предложить тему для публикации')
b5 = KeyboardButton('Обо мне')
b6 = KeyboardButton('Генератор судебных документов')
b7 = KeyboardButton('Главное меню')
b8 = KeyboardButton('В главное меню')
b9 = KeyboardButton('Назад')
b10 = KeyboardButton('Вернуться назад')

b11 = KeyboardButton('Создать')
b12 = KeyboardButton('Пример')
b13 = KeyboardButton('Отмена')
b14 = KeyboardButton('Получить')

b15 = KeyboardButton('Мобилизация')
b16 = KeyboardButton('Миграция')
b17 = KeyboardButton('Трудовые споры')
b18 = KeyboardButton('Защита прав потребителей')

# b19 = KeyboardButton('Моя группа в Telegram')
# b20 = KeyboardButton('Мой Instagram')
# b21 = KeyboardButton('Мой VK')

intro_inline_keyboard = InlineKeyboardMarkup(row_width=1)
intro_inline_keyboard.add(k1).add(k2)

consultation_inline_keyboard = InlineKeyboardMarkup(row_width=1)
consultation_inline_keyboard.add(k3).add(k4).add(k5).add(k6).add(k2)

socials_inline_keyboard = InlineKeyboardMarkup(row_width=1)
socials_inline_keyboard.add(k7).add(k8).add(k9)

main_menu_keyboard = ReplyKeyboardMarkup(resize_keyboard=True) # one_time_keyboard=True
main_menu_keyboard.add(b1).insert(b2).add(b3).insert(b4).add(b5).insert(b6)

consultation_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
consultation_keyboard.add(b15).insert(b16).insert(b17).add(b18).insert(b7)

consultation_keyboard_in = ReplyKeyboardMarkup(resize_keyboard=True)
consultation_keyboard_in.add(b9).insert(b7)

consultation_keyboard_in_abort = ReplyKeyboardMarkup(resize_keyboard=True)
consultation_keyboard_in_abort.add(b10).insert(b8)

consultation_keyboard_in_after_inline = ReplyKeyboardMarkup(resize_keyboard=True)
consultation_keyboard_in_after_inline.add(b7)

consultation_keyboard_in_after_inline_abort = ReplyKeyboardMarkup(resize_keyboard=True)
consultation_keyboard_in_after_inline_abort.add(b8)

feedback_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
feedback_keyboard.add(b7)

feedback_keyboard_abort = ReplyKeyboardMarkup(resize_keyboard=True)
feedback_keyboard_abort.add(b8)

cooperation_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
cooperation_keyboard.add(b7)

cooperation_keyboard_abort = ReplyKeyboardMarkup(resize_keyboard=True)
cooperation_keyboard_abort.add(b8)

suggestion_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
suggestion_keyboard.add(b7)

suggestion_keyboard_abort = ReplyKeyboardMarkup(resize_keyboard=True)
suggestion_keyboard_abort.add(b8)

# about_me_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
# about_me_keyboard.add(b19).insert(b20).insert(b21).add(b7)

doc_generator_start_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
doc_generator_start_keyboard.add(b11).insert(b12).insert(b7)

cancel_generator_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
cancel_generator_keyboard.add(b13)

doc_generator_finish_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
doc_generator_finish_keyboard.add(b11).insert(b14).insert(b7)

# # keyboard: Optional[List[List[KeyboardButton]]] = None
# async def keyboard_generator(key_list):
#     # key_list = ['1', '2', '3']
#     tmp_buttons = []
#     for i in key_list:
#         tmp_buttons.append([KeyboardButton(i)])
#     tmp_buttons.append([KeyboardButton('/cancel')])
#     keyboard = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=tmp_buttons)
#     return keyboard
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

b1 = KeyboardButton('/получитьㅤконсультацию')
b2 = KeyboardButton('/оставитьㅤотзывㅤоㅤмоейㅤработе')
b3 = KeyboardButton('/сотрудничество')
b4 = KeyboardButton('/обоㅤмне')
b5 = KeyboardButton('/предложитьㅤтемуㅤдляㅤновойㅤпубликации')
b6 = KeyboardButton('/перейтиㅤвㅤгенераторㅤсудебныхㅤдокументов')
b7 = KeyboardButton('/вㅤглавноеㅤменю')
b8 = KeyboardButton('/назад')

b9 = KeyboardButton('/создать')
b10 = KeyboardButton('/пример')
b11 = KeyboardButton('/отмена')
b12 = KeyboardButton('/получить')

b13 = KeyboardButton('/мобилизация')
b14 = KeyboardButton('/миграция')
b15 = KeyboardButton('/трудовыеㅤспоры')
b16 = KeyboardButton('/защитаㅤправㅤпотребителей')


main_menu_keyboard = ReplyKeyboardMarkup(resize_keyboard=True) # one_time_keyboard=True
main_menu_keyboard.add(b1).insert(b2).add(b3).insert(b4).add(b5).add(b6)

consultation_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
consultation_keyboard.add(b13).insert(b14).insert(b15).add(b16).insert(b7)

consultation_keyboard_in = ReplyKeyboardMarkup(resize_keyboard=True)
consultation_keyboard_in.add(b8).insert(b7)

doc_generator_start_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
doc_generator_start_keyboard.add(b9).insert(b10).insert(b7)

cancel_generator_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
cancel_generator_keyboard.add(b11)

doc_generator_finish_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
doc_generator_finish_keyboard.add(b9).insert(b12).insert(b7)

# # keyboard: Optional[List[List[KeyboardButton]]] = None
# async def keyboard_generator(key_list):
#     # key_list = ['1', '2', '3']
#     tmp_buttons = []
#     for i in key_list:
#         tmp_buttons.append([KeyboardButton(i)])
#     tmp_buttons.append([KeyboardButton('/cancel')])
#     keyboard = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=tmp_buttons)
#     return keyboard
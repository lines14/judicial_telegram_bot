from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

b1 = KeyboardButton('/хочуㅤполучитьㅤконсультацию')
b2 = KeyboardButton('/хочуㅤоставитьㅤотзывㅤоㅤработе')
b3 = KeyboardButton('/хочуㅤсотрудничать')
b4 = KeyboardButton('/хочуㅤпредложитьㅤтемуㅤдляㅤновойㅤпубликации')
b5 = KeyboardButton('/перейтиㅤвㅤгенераторㅤсудебныхㅤдокументов')
b6 = KeyboardButton('/вㅤглавноеㅤменю')
b7 = KeyboardButton('/назад')

b8 = KeyboardButton('/создать')
b9 = KeyboardButton('/пример')
b10 = KeyboardButton('/отмена')
b11 = KeyboardButton('/получить')

b12 = KeyboardButton('/мобилизация')
b13 = KeyboardButton('/миграция')
b14 = KeyboardButton('/трудовыеㅤспоры')
b15 = KeyboardButton('/защитаㅤправㅤпотребителей')


main_menu_keyboard = ReplyKeyboardMarkup(resize_keyboard=True) # one_time_keyboard=True
main_menu_keyboard.add(b1).insert(b2).insert(b3).add(b4).insert(b5)

consultation_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
consultation_keyboard.add(b12).insert(b13).insert(b14).add(b15).insert(b6)

consultation_keyboard_in = ReplyKeyboardMarkup(resize_keyboard=True)
consultation_keyboard_in.add(b7).insert(b6)

doc_generator_start_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
doc_generator_start_keyboard.add(b8).insert(b9).insert(b6)

cancel_generator_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
cancel_generator_keyboard.add(b10)

doc_generator_finish_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
doc_generator_finish_keyboard.add(b8).insert(b11).insert(b6)

# # keyboard: Optional[List[List[KeyboardButton]]] = None
# async def keyboard_generator(key_list):
#     # key_list = ['1', '2', '3']
#     tmp_buttons = []
#     for i in key_list:
#         tmp_buttons.append([KeyboardButton(i)])
#     tmp_buttons.append([KeyboardButton('/cancel')])
#     keyboard = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=tmp_buttons)
#     return keyboard
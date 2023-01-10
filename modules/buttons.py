from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

b1 = KeyboardButton('/start')
b2 = KeyboardButton('/download')

kb_client = ReplyKeyboardMarkup(resize_keyboard=True) # one_time_keyboard=True
kb_client.add(b1).insert(b2)

# keyboard: Optional[List[List[KeyboardButton]]] = None
async def keyboard_generator(key_list):
    # key_list = ['1', '2', '3']
    tmp_buttons = []
    for i in key_list:
        tmp_buttons.append([KeyboardButton(i)])
    tmp_buttons.append([KeyboardButton('/cancel')])
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=tmp_buttons)
    return keyboard
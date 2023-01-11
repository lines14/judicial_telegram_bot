from aiogram import types, Dispatcher
from modules.bot_base import dp, bot
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from modules.buttons import keys
from modules.buttons import keyboard_generator
from modules.template import data_print
class InputUserData(StatesGroup):
    user_data1 = State()
    user_data2 = State()
    user_data3 = State()

async def start_command(message: types.Message):
    await message.reply('Привет, отправь мне свой запрос!', reply_markup=keys)

async def add_data(message: types.Message):
    await InputUserData.user_data1.set()
    await message.reply('Введите данные 1')

async def pick_data1(message: types.Message, state: FSMContext):

    async with state.proxy() as data:
        data['user_data1'] = message.text
    await InputUserData.next()
    await bot.send_message(chat_id = message.from_user.id, text='Введите данные 2')

async def pick_data2(message: types.Message, state: FSMContext):

    async with state.proxy() as data:
        data['user_data2'] = message.text
    await InputUserData.next()
    await bot.send_message(chat_id = message.from_user.id, text='Введите данные 3')

async def pick_data3(message: types.Message, state: FSMContext):

    async with state.proxy() as data:
        data['user_data3'] = message.text
    await data_print(state)
    await bot.send_message(chat_id = message.from_user.id, text='Данные записаны')
    await state.finish()

async def get_file(message: types.Message):
    await message.reply_document(open('/home/lines14/projects/judicial_telegram_bot/documents/judicial_writer_1.docx', 'rb'))

def register_handler_client(dp: Dispatcher):
    dp.register_message_handler(start_command, commands=['start'])
    dp.register_message_handler(get_file, commands=['download'])
    dp.register_message_handler(add_data, commands=['add'], state=None)
    dp.register_message_handler(pick_data1, state=InputUserData.user_data1)
    dp.register_message_handler(pick_data2, state=InputUserData.user_data2)
    dp.register_message_handler(pick_data3, state=InputUserData.user_data3)
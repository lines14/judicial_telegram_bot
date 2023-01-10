from aiogram import types, Dispatcher
from modules.bot_base import dp, bot
from aiogram.dispatcher import FSMContext
from modules.buttons import keys
from modules.buttons import keyboard_generator

async def start_command(message: types.Message):
    await message.reply('Привет, отправь мне свой запрос!', reply_markup=keys)

async def get_file(message: types.Message):
    await message.reply_document(open('/home/lines14/projects/judicial_telegram_bot/documents/judicial_writer_1.docx', 'rb'))

def register_handler_client(dp: Dispatcher):
    dp.register_message_handler(start_command, commands=['start'])
    dp.register_message_handler(get_file, commands=['download'])
    
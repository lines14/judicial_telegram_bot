from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import os
import dotenv

dotenv.load_dotenv()
TG_TOKEN = os.environ.get('TG_TOKEN')

bot = Bot(token=TG_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.reply('Привет, отправь мне свой запрос!')

@dp.message_handler(commands=['download'])
async def get_file(message: types.Message):
    await message.reply_document(open('/home/lines14/projects/judicial_telegram_bot/judicial_writer_1.docx', 'rb'))

def main():
    pass

if __name__ == '__main__':
    executor.start_polling(dp)
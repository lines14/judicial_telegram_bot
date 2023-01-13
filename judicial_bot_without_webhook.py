from aiogram.utils import executor
from modules.bot_base import dp

async def on_startup(_):
    print('Бот успешно запущен!')

from modules import handlers

handlers.register_handler_client(dp)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup, timeout=200)
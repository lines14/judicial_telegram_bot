from aiogram.utils import executor
from modules.bot_base import dp
from modules import data_base
from modules import handlers
from modules import admin_handlers
import aioschedule

async def on_startup(_):
    data_base.sql_start()
    aioschedule.every(3).days.at("12:00").do(handlers.reminder)
    print('Бот успешно запущен!')

handlers.register_handler_client(dp)
admin_handlers.register_handler_admin(dp)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup, timeout=200)
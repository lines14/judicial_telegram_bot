import logging
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.utils.executor import start_webhook
from modules.config import WEBHOOK_PATH, WEBHOOK_URL, WEBAPP_HOST, WEBAPP_PORT
from modules.bot_base import bot
from modules.bot_base import dp
from modules import data_base

logging.basicConfig(level=logging.INFO)
dp.middleware.setup(LoggingMiddleware())

async def on_startup(_):
    await bot.set_webhook(WEBHOOK_URL, drop_pending_updates=True) #certificate=CERT
    data_base.sql_start()
    print('Бот успешно запущен!')

async def on_shutdown(_):
    logging.warning('Shutting down..')
    await bot.delete_webhook()
    await dp.storage.close()
    await dp.storage.wait_closed()
    logging.warning('Bye!')

from modules import handlers

handlers.register_handler_client(dp)

if __name__ == '__main__':
    start_webhook(dp, WEBHOOK_PATH, skip_updates=True, on_startup=on_startup, on_shutdown=on_shutdown, host=WEBAPP_HOST, port=WEBAPP_PORT, )
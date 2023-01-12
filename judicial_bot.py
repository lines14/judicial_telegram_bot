import logging
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.utils.executor import start_webhook
from aiogram.types import InputFile
from modules.config import WEBHOOK_PATH, WEBHOOK_URL, WEBAPP_HOST, WEBAPP_PORT
from modules.bot_base import bot
from modules.bot_base import dp

logging.basicConfig(level=logging.INFO)
dp.middleware.setup(LoggingMiddleware())

# CERT=InputFile('/home/lines14/projects/judicial_telegram_bot/judicial_bot_public.pem', 'r')

async def on_startup(dp):
    await bot.set_webhook(url=WEBHOOK_URL) #drop_pending_updates=True
    print('Бот успешно запущен!')

async def on_shutdown(dp):
    logging.warning('Shutting down..')
    await bot.delete_webhook()
    await dp.storage.close()
    await dp.storage.wait_closed()
    logging.warning('Bye!')

from modules import handlers

handlers.register_handler_client(dp)

if __name__ == '__main__':
    start_webhook(dispatcher=dp, webhook_path=WEBHOOK_PATH, skip_updates=True, on_startup=on_startup, on_shutdown=on_shutdown, host=WEBAPP_HOST, port=WEBAPP_PORT, )
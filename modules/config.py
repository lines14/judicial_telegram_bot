import os
from dotenv import load_dotenv
load_dotenv()

DB_PATH = os.getenv('DB_PATH')
TG_TOKEN = os.getenv('TG_TOKEN')
ADMIN_ID = os.getenv('ADMIN_ID')

# webhook settings
WEBHOOK_HOST=os.getenv('WEBHOOK_HOST')
WEBHOOK_PATH=f'/{TG_TOKEN}'
WEBHOOK_URL=f'https://{WEBHOOK_HOST}{WEBHOOK_PATH}'

# webserver settings
WEBAPP_HOST = os.getenv('WEBAPP_HOST')
WEBAPP_PORT = os.getenv('WEBAPP_PORT')
WEBAPP_PORT = WEBAPP_PORT if type(WEBAPP_PORT) == int else int(WEBAPP_PORT)
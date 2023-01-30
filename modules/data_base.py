import sqlite3 as sq
from modules.bot_base import bot

def sql_start():
    global base, cur
    base = sq.connect('/home/lines14/projects/judicial_telegram_bot/documents/database.db')
    cur = base.cursor()
    if base:
        print('[ОК] - База данных подключена!')
    base.execute('CREATE TABLE IF NOT EXISTS bank_of_appeals(phone TEXT, user_id TEXT, section TEXT, date TEXT, time TEXT, appeal TEXT)')
    base.commit()

# Добавление обращения в базу данных

async def sql_add_appeal(state):
    async with state.proxy() as data:
        print(tuple(data.values()))
        cur.execute('INSERT INTO bank_of_appeals VALUES (?, ?, ?, ?, ?, ?)', tuple(data.values()))
        base.commit()
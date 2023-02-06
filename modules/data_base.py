import sqlite3 as sq
from modules.bot_base import bot

def sql_start():
    global base, cur
    base = sq.connect('/home/lines14/projects/judicial_telegram_bot/documents/database.db')
    cur = base.cursor()
    if base:
        print('[ОК] - База данных подключена!')
    base.execute("CREATE TABLE IF NOT EXISTS bank_of_appeals(status TEXT, phone TEXT, user_id TEXT, nickname TEXT, fullname TEXT, section TEXT, datetime TEXT, appeal TEXT)")
    base.commit()

# Добавление обращения в базу данных

async def sql_add_appeal(state):
    async with state.proxy() as data:
        print(tuple(data.values()))
        cur.execute("INSERT INTO bank_of_appeals VALUES (?, ?, ?, ?, ?, ?, ?, ?)", tuple(data.values()))
        base.commit()       

# Чтение обращений из базы данных

async def sql_all_get_sorted_by_time_desc():
    key_list = []
    response = cur.execute("SELECT section FROM bank_of_appeals WHERE section = 'Мобилизация' OR section = 'Миграция' OR section = 'Трудовые споры' OR section = 'Защита прав потребителей' ORDER BY datetime DESC;").fetchall()
    for i in response:
        key_list.append(str(*i))
    return key_list

async def sql_all_get_sorted_by_time_asc():
    key_list = []
    response = cur.execute("SELECT section FROM bank_of_appeals WHERE section = 'Мобилизация' OR section = 'Миграция' OR section = 'Трудовые споры' OR section = 'Защита прав потребителей' ORDER BY datetime;").fetchall()
    for i in response:
        key_list.append(str(*i))
    return key_list

async def sql_mobilization_get_sorted_by_time_desc():
    key_list = []
    response = cur.execute("SELECT section FROM bank_of_appeals WHERE section = 'Мобилизация' ORDER BY datetime DESC;").fetchall()
    for i in response:
        key_list.append(str(*i))
    return key_list

async def sql_mobilization_get_sorted_by_time_asc():
    key_list = []
    response = cur.execute("SELECT section FROM bank_of_appeals WHERE section = 'Мобилизация' ORDER BY datetime;").fetchall()
    for i in response:
        key_list.append(str(*i))
    return key_list

async def sql_migration_get_sorted_by_time_desc():
    key_list = []
    response = cur.execute("SELECT section FROM bank_of_appeals WHERE section = 'Миграция' ORDER BY datetime DESC;").fetchall()
    for i in response:
        key_list.append(str(*i))
    return key_list

async def sql_migration_get_sorted_by_time_asc():
    key_list = []
    response = cur.execute("SELECT section FROM bank_of_appeals WHERE section = 'Миграция' ORDER BY datetime;").fetchall()
    for i in response:
        key_list.append(str(*i))
    return key_list

async def sql_employment_get_sorted_by_time_desc():
    key_list = []
    response = cur.execute("SELECT section FROM bank_of_appeals WHERE section = 'Трудовые споры' ORDER BY datetime DESC;").fetchall()
    for i in response:
        key_list.append(str(*i))
    return key_list

async def sql_employment_get_sorted_by_time_asc():
    key_list = []
    response = cur.execute("SELECT section FROM bank_of_appeals WHERE section = 'Трудовые споры' ORDER BY datetime;").fetchall()
    for i in response:
        key_list.append(str(*i))
    return key_list

async def sql_consumer_get_sorted_by_time_desc():
    key_list = []
    response = cur.execute("SELECT section FROM bank_of_appeals WHERE section = 'Защита прав потребителей' ORDER BY datetime DESC;").fetchall()
    for i in response:
        key_list.append(str(*i))
    return key_list

async def sql_consumer_get_sorted_by_time_asc():
    key_list = []
    response = cur.execute("SELECT section FROM bank_of_appeals WHERE section = 'Защита прав потребителей' ORDER BY datetime;").fetchall()
    for i in response:
        key_list.append(str(*i))
    return key_list
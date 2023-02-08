import sqlite3 as sq
from modules.bot_base import bot

def sql_start():
    global base, cur
    base = sq.connect('/home/lines14/projects/judicial_telegram_bot/documents/database.db')
    cur = base.cursor()
    if base:
        print('[ОК] - База данных подключена!')
    base.execute("CREATE TABLE IF NOT EXISTS bank_of_appeals(user_id TEXT, nickname TEXT, fullname TEXT, section TEXT, datetime TEXT, appeal TEXT, status TEXT, phone TEXT)")
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
    response = cur.execute("SELECT datetime, fullname FROM bank_of_appeals WHERE section = 'Мобилизация' OR section = 'Миграция' OR section = 'Трудовые споры' OR section = 'Защита прав потребителей' ORDER BY datetime DESC;").fetchall()
    for i in response:
        j = ''.join(i[0].split(' ')[slice(1, 2)])
        a = ''.join(i[0].split(' ')[slice(0, 1)])
        b = a.split('-')
        b.reverse()
        c = '.'.join(b)
        key_list.append(c+' | '+j+' | '+i[1])
    return key_list

async def sql_all_get_sorted_by_time_asc():
    key_list = []
    response = cur.execute("SELECT datetime, fullname FROM bank_of_appeals WHERE section = 'Мобилизация' OR section = 'Миграция' OR section = 'Трудовые споры' OR section = 'Защита прав потребителей' ORDER BY datetime;").fetchall()
    for i in response:
        j = ''.join(i[0].split(' ')[slice(1, 2)])
        a = ''.join(i[0].split(' ')[slice(0, 1)])
        b = a.split('-')
        b.reverse()
        c = '.'.join(b)
        key_list.append(c+' | '+j+' | '+i[1])
    return key_list

async def sql_mobilization_get_sorted_by_time_desc():
    key_list = []
    response = cur.execute("SELECT datetime, fullname FROM bank_of_appeals WHERE section = 'Мобилизация' ORDER BY datetime DESC;").fetchall()
    for i in response:
        j = ''.join(i[0].split(' ')[slice(1, 2)])
        a = ''.join(i[0].split(' ')[slice(0, 1)])
        b = a.split('-')
        b.reverse()
        c = '.'.join(b)
        key_list.append(c+' | '+j+' | '+i[1])
    return key_list

async def sql_mobilization_get_sorted_by_time_asc():
    key_list = []
    response = cur.execute("SELECT datetime, fullname FROM bank_of_appeals WHERE section = 'Мобилизация' ORDER BY datetime;").fetchall()
    for i in response:
        j = ''.join(i[0].split(' ')[slice(1, 2)])
        a = ''.join(i[0].split(' ')[slice(0, 1)])
        b = a.split('-')
        b.reverse()
        c = '.'.join(b)
        key_list.append(c+' | '+j+' | '+i[1])
    return key_list

async def sql_migration_get_sorted_by_time_desc():
    key_list = []
    response = cur.execute("SELECT datetime, fullname FROM bank_of_appeals WHERE section = 'Миграция' ORDER BY datetime DESC;").fetchall()
    for i in response:
        j = ''.join(i[0].split(' ')[slice(1, 2)])
        a = ''.join(i[0].split(' ')[slice(0, 1)])
        b = a.split('-')
        b.reverse()
        c = '.'.join(b)
        key_list.append(c+' | '+j+' | '+i[1])
    return key_list

async def sql_migration_get_sorted_by_time_asc():
    key_list = []
    response = cur.execute("SELECT datetime, fullname FROM bank_of_appeals WHERE section = 'Миграция' ORDER BY datetime;").fetchall()
    for i in response:
        j = ''.join(i[0].split(' ')[slice(1, 2)])
        a = ''.join(i[0].split(' ')[slice(0, 1)])
        b = a.split('-')
        b.reverse()
        c = '.'.join(b)
        key_list.append(c+' | '+j+' | '+i[1])
    return key_list

async def sql_employment_get_sorted_by_time_desc():
    key_list = []
    response = cur.execute("SELECT datetime, fullname FROM bank_of_appeals WHERE section = 'Трудовые споры' ORDER BY datetime DESC;").fetchall()
    for i in response:
        j = ''.join(i[0].split(' ')[slice(1, 2)])
        a = ''.join(i[0].split(' ')[slice(0, 1)])
        b = a.split('-')
        b.reverse()
        c = '.'.join(b)
        key_list.append(c+' | '+j+' | '+i[1])
    return key_list

async def sql_employment_get_sorted_by_time_asc():
    key_list = []
    response = cur.execute("SELECT datetime, fullname FROM bank_of_appeals WHERE section = 'Трудовые споры' ORDER BY datetime;").fetchall()
    for i in response:
        j = ''.join(i[0].split(' ')[slice(1, 2)])
        a = ''.join(i[0].split(' ')[slice(0, 1)])
        b = a.split('-')
        b.reverse()
        c = '.'.join(b)
        key_list.append(c+' | '+j+' | '+i[1])
    return key_list

async def sql_consumer_get_sorted_by_time_desc():
    key_list = []
    response = cur.execute("SELECT datetime, fullname FROM bank_of_appeals WHERE section = 'Защита прав потребителей' ORDER BY datetime DESC;").fetchall()
    for i in response:
        j = ''.join(i[0].split(' ')[slice(1, 2)])
        a = ''.join(i[0].split(' ')[slice(0, 1)])
        b = a.split('-')
        b.reverse()
        c = '.'.join(b)
        key_list.append(c+' | '+j+' | '+i[1])
    return key_list

async def sql_consumer_get_sorted_by_time_asc():
    key_list = []
    response = cur.execute("SELECT datetime, fullname FROM bank_of_appeals WHERE section = 'Защита прав потребителей' ORDER BY datetime;").fetchall()
    for i in response:
        j = ''.join(i[0].split(' ')[slice(1, 2)])
        a = ''.join(i[0].split(' ')[slice(0, 1)])
        b = a.split('-')
        b.reverse()
        c = '.'.join(b)
        key_list.append(c+' | '+j+' | '+i[1])
    return key_list

async def sql_cooperation_get_sorted_by_time_desc():
    key_list = []
    response = cur.execute("SELECT datetime, fullname FROM bank_of_appeals WHERE section = 'Сотрудничество' ORDER BY datetime DESC;").fetchall()
    for i in response:
        j = ''.join(i[0].split(' ')[slice(1, 2)])
        a = ''.join(i[0].split(' ')[slice(0, 1)])
        b = a.split('-')
        b.reverse()
        c = '.'.join(b)
        key_list.append(c+' | '+j+' | '+i[1])
    return key_list

async def sql_cooperation_get_sorted_by_time_asc():
    key_list = []
    response = cur.execute("SELECT datetime, fullname FROM bank_of_appeals WHERE section = 'Сотрудничество' ORDER BY datetime;").fetchall()
    for i in response:
        j = ''.join(i[0].split(' ')[slice(1, 2)])
        a = ''.join(i[0].split(' ')[slice(0, 1)])
        b = a.split('-')
        b.reverse()
        c = '.'.join(b)
        key_list.append(c+' | '+j+' | '+i[1])
    return key_list

async def sql_suggestion_get_sorted_by_time_desc():
    key_list = []
    response = cur.execute("SELECT datetime, fullname FROM bank_of_appeals WHERE section = 'Предложения тем для публикаций' ORDER BY datetime DESC;").fetchall()
    for i in response:
        j = ''.join(i[0].split(' ')[slice(1, 2)])
        a = ''.join(i[0].split(' ')[slice(0, 1)])
        b = a.split('-')
        b.reverse()
        c = '.'.join(b)
        key_list.append(c+' | '+j+' | '+i[1])
    return key_list

async def sql_feedback_get_sorted_by_time_desc():
    key_list = []
    response = cur.execute("SELECT datetime, fullname FROM bank_of_appeals WHERE section = 'Отзывы' ORDER BY datetime DESC;").fetchall()
    for i in response:
        j = ''.join(i[0].split(' ')[slice(1, 2)])
        a = ''.join(i[0].split(' ')[slice(0, 1)])
        b = a.split('-')
        b.reverse()
        c = '.'.join(b)
        key_list.append(c+' | '+j+' | '+i[1])
    return key_list

async def sql_get_info(inbound_key):
    splitted_key = inbound_key.split(' | ')
    splitted_substr = splitted_key[0].split('.')
    splitted_substr.reverse()
    outbound_key = '-'.join(splitted_substr)+' '+splitted_key[1]
    response = cur.execute(f"SELECT status, phone, nickname, fullname, appeal FROM bank_of_appeals WHERE datetime = '{outbound_key}';").fetchall()
    return response
import sqlite3 as sq
from create_bot import bot
from keyboards import ikb_w_pay, ikb_w_confirm
from handlers import commands

def sql_start():
    global base, cur
    base = sq.connect('fines_database.db')
    cur = base.cursor()
    if base:
        print('[ОК] - База данных подключена!')
    base.execute('CREATE TABLE IF NOT EXISTS all_fines(id INTEGER PRIMARY KEY AUTOINCREMENT, photo TEXT, foul TEXT, latitude BLOB, longitude BLOB, gnumber TEXT, number TEXT, date TEXT, time TEXT, user_id TEXT, status TEXT, intruder TEXT)')
    base.execute('CREATE TABLE IF NOT EXISTS users(user_id TEXT, first_name TEXT, last_name TEXT, user_phone TEXT)')
    base.execute('CREATE TABLE IF NOT EXISTS personal_cars(gos_number TEXT, gos_name TEXT, user_id TEXT)')
    base.execute('CREATE TABLE IF NOT EXISTS bank_pn(phone_number TEXT, bank_name TEXT, user_id TEXT)')
    base.commit()

# Запись штрафов в базу сотрудниками /penalty
async def sql_add_command(state):
    async with state.proxy() as data:
        print(tuple(data.values()))
        # cur.execute('INSERT INTO all_fines VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', tuple(data.values()))
        cur.execute('INSERT INTO all_fines (photo, foul, latitude, longitude, gnumber, number, date, time, user_id, status, intruder) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', tuple(data.values()))
        base.commit()

# Выборка из базы сотрудников /list
async def sql_read(message):
    # for ret in cur.execute(f'SELECT photo, date, time, gnumber, latitude, longitude, status, id FROM all_fines WHERE user_id = \'{message.chat.id}\' AND status != \'Просрочен\' AND status != \'Погашен\';').fetchall():
    response = cur.execute(f'SELECT photo, date, time, gnumber, latitude, longitude, status, id FROM all_fines WHERE user_id = \'{message.chat.id}\' AND status = \'Ожидает подтверждение оплаты\'').fetchall()
    return response
    # if len(response) == 0:
    #     await bot.send_message(chat_id = message.from_user.id, text='Нет запросов на подтверждение платежей')
    # else:
    #     for ret in response:
    #         await bot.send_photo(message.from_user.id, ret[0], f'Дата и время:\n{ret[1]} - {ret[2]}\n\nГосномер авто:\n{ret[3]}\n\nЛокация: https://yandex.kz/maps/?from=tabbar&source=serp_navig&text={ret[4]}%2C{ret[5]}\n\nСтатус:\n{ret[6]}\n\nID Нарушения:\n{ret[7]}', reply_markup=ikb_w_confirm)

async def sql_my_income(message):
    response = cur.execute(f'SELECT foul FROM all_fines WHERE user_id = \'{message.chat.id}\' AND status = \'Погашен\'').fetchall()
    return response

# Регистрация клиента в базе /registration
async def sql_user_reg(state):
    async with state.proxy() as data:
        print(tuple(data.values()))
        cur.execute('INSERT INTO users VALUES (?, ?, ?, ?)', tuple(data.values()))
        base.commit()

# Добавление личного авто /add
async def sql_add_car(state):
    async with state.proxy() as data:
        print(tuple(data.values()))

        cur.execute('INSERT INTO personal_cars VALUES (?, ?, ?)', tuple(data.values()))
        base.commit()

# Проверка штрафа пользователем /check
async def sql_check_penaltys(message):
    car_list = cur.execute(f'SELECT gos_number FROM personal_cars WHERE user_id = \'{message.from_user.id}\'')
    
    if len(car_list.fetchall()) > 0:
        response = cur.execute(f'SELECT photo, foul, gnumber, date, time, latitude, longitude, status, id FROM all_fines LEFT OUTER JOIN personal_cars WHERE all_fines.gnumber = personal_cars.gos_number AND personal_cars.user_id = \'{message.chat.id}\' AND status != \'Просрочен\' AND status != \'Погашен\';').fetchall()
        if str(response) == '[]':
            await bot.send_message(chat_id = message.from_user.id, text='ОТЛИЧНО - У вас нет нарушений!')
        else:
            text = []
            for ret in response:
                if ret[1] == 'S597P1':
                    text.append(commands.S597P1)
                elif ret[1] == 'S597P2':
                    text.append(commands.S597P2)
                elif ret[1] == 'S597P3':
                    text.append(commands.S597P3)
                elif ret[1] == 'S597P4':
                    text.append(commands.S597P4)
                elif ret[1] == 'unidentified':
                    text.append(commands.UNIDENTIFIED)

                await bot.send_photo(message.from_user.id, ret[0], caption=f'{text[0]}\nГосномер авто:\n{ret[2]}\n\nДата и время:\n{ret[3]} - {ret[4]}\n\nЛокация:\nhttps://yandex.kz/maps/?from=tabbar&source=serp\_navig&text={ret[5]}%2C{ret[6]}\n\nСтатус:\n{ret[7]}\n\nID Нарушения:\n`{ret[8]}`', parse_mode='Markdown', reply_markup=ikb_w_pay)
    else:
        await bot.send_message(chat_id = message.from_user.id, text='У вас не добавлен не один Авто. Чтобы добавить Авто нажмите кнопку /add')

# Выборка под клавиатуру штрафов
async def sql_check_keyboard(message):
    key_list = []
    response = cur.execute(f'SELECT id FROM all_fines LEFT OUTER JOIN personal_cars WHERE all_fines.gnumber = personal_cars.gos_number AND personal_cars.user_id = \'{message.from_user.id}\' AND status != \'Ожидает подтверждение оплаты\' AND status != \'Погашен\' AND status != \'Просрочен\';').fetchall()
    for i in response:
        key_list.append(str(*i))
    return key_list

# Получения данных для оплаты
async def sql_check_pay_data(message, id_violation):
    response = cur.execute(f'SELECT foul, phone_number, all_fines.user_id FROM all_fines LEFT OUTER JOIN personal_cars, bank_pn WHERE all_fines.gnumber = personal_cars.gos_number AND personal_cars.user_id = \'{message.from_user.id}\' AND all_fines.id = \'{id_violation}\' AND bank_pn.user_id = all_fines.user_id').fetchall()
    for i in response:
        return i

# Получения данных для оплаты от клиента
async def sql_change_payment_status(id, user_id):
    cur.execute(f'UPDATE all_fines SET status = \'Ожидает подтверждение оплаты\', intruder = \'{user_id}\'  WHERE id = \'{id}\'')
    base.commit()

# Проверка существования пользователя
async def sql_existence_check(message):
    for ret in cur.execute(f'SELECT user_id FROM users WHERE user_id = \'{message.from_user.id}\''):
        if str(ret[0]) == str(message.from_user.id):
            return True
        else:
            return False

# Выборка номеров Авто пользователя
async def sql_my_cars(message):
    
    keys = []
    for ret in cur.execute(f'SELECT gos_number FROM personal_cars WHERE user_id = \'{message.from_user.id}\''):
        keys.append(list(ret))
    return keys

# Выборка номеров Авто пользователя
async def sql_del_my_cars(state):
    async with state.proxy() as data:
        message_id = data['message_id']
        gos_number = data['gos_number']
        cur.execute(f'DELETE FROM personal_cars WHERE user_id = \'{message_id}\' AND gos_number = \'{gos_number}\'')
        base.commit()
        print(f'Авто с номером: {gos_number} у пользователя {message_id} успешно удален')


# Добавление личного авто /add
async def sql_add_pn_kaspi(state):
    async with state.proxy() as data:
        print(tuple(data.values()))
        cur.execute('INSERT INTO bank_pn VALUES (?, ?, ?)', tuple(data.values()))
        base.commit()

# Проверка существования номера KASPI в базе
async def sql_check_pn_kaspi(message):

    for ret in cur.execute(f'SELECT bank_name FROM bank_pn WHERE user_id = \'{message.from_user.id}\''):
        if str(ret[0]) == 'KASPI':
            return True
        else:
            return False

async def sql_client_notification(gos_number):
    response = cur.execute(f'SELECT user_id FROM personal_cars WHERE gos_number = \'{gos_number}\'')
    return response

async def sql_check_worker_card(message):
    tmp = []
    for ret in cur.execute(f'SELECT bank_name FROM bank_pn WHERE user_id = \'{message.from_user.id}\''):
        tmp.append(ret)
    if len(tmp) == 0:
        return True
    else:
        return False

async def sql_corfirn_pay(message):
    tmp = []
    for ret in cur.execute(f'SELECT id FROM all_fines WHERE user_id = \'{message.from_user.id}\' AND status = \'Ожидает подтверждение оплаты\''):
        tmp.append(*ret)
    return tmp

# Получения данных для оплаты
async def sql_load_confirm(id):
    cur.execute(f'UPDATE all_fines SET status = \'Погашен\' WHERE id = \'{id}\'')
    base.commit()
    
    tmp = []
    for ret in cur.execute(f'SELECT intruder FROM all_fines WHERE id = \'{id}\''):
        tmp.append(*ret)
    return tmp



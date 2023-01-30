from datetime import datetime

current_datetime = datetime.now()

print(str(current_datetime)[0:-7])

# When you sure the format of text field is yyyy-MM-dd HH:mm:ss (ex.: 2017-01-02 16:02:55), So It works for me simply:

# SELECT * FROM Table ORDER BY dateColumn DESC Limit 1

# Without any extra date function!












# Ловим второй ответ

# async def load_gos_name(message: types.Message, state: FSMContext):
#     async with state.proxy() as data:
#         data['gos_name'] = message.text
#         data['user_id'] = message.chat.id
#     await bot.send_message(chat_id = message.from_user.id, text='Авто успешно добавлен', reply_markup=kb_client)
#     await sqlite_db.sql_add_car(state)
#     await state.finish()

# data['date'] = f'{current_datetime.day(day if len(day)==1 else )}:{current_datetime.month}:{current_datetime.year}'
# data['time'] = f'{current_datetime.hour}:{current_datetime.minute}'
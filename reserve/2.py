# Ловим второй ответ

async def load_gos_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['gos_name'] = message.text
        data['user_id'] = message.chat.id
    await bot.send_message(chat_id = message.from_user.id, text='Авто успешно добавлен', reply_markup=kb_client)
    await sqlite_db.sql_add_car(state)
    await state.finish()
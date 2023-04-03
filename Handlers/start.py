from loader import dp
from Data import add_new_user, find_user_tg_id
from aiogram.types import Message
from Keyboards import kb_main

@dp.message_handler(commands=['start'])
async def start_commands(message: Message):
    tg_id = message.from_user.id
    last_name = message.from_user.last_name
    first_name = message.from_user.first_name

    result = find_user_tg_id((tg_id, ))

    if not result:
        new_user = (tg_id, last_name, first_name, 'user')
        add_new_user(new_user)

    await message.answer(f'{message.from_user.first_name}, привет!', reply_markup=kb_main)
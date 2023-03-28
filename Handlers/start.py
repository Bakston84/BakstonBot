from loader import dp
from aiogram.types import Message
from Keyboards import kb_main

@dp.message_handler(commands=['start'])
async def start_commands(message: Message):
    await message.answer(f'{message.from_user.first_name}, привет!', reply_markup=kb_main)
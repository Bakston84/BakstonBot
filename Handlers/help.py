from loader import dp
from aiogram.types import Message

@dp.message_handler(commands=['help'])
async def help_commands(message: Message):
    await message.answer(f'Список команд: /start')
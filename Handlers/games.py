from loader import dp
from aiogram.types import Message

@dp.message_handler(commands=['games'])
async def games_commands(message: Message):
    await message.answer(f'{message.from_user.first_name}, во что поиграем?')
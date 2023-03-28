from loader import dp
from aiogram.types import Message

@dp.message_handler()
async def all_commands(message: Message):
    await message.answer(f'{message.from_user.first_name}, смотри что поймал - '
                         f'{message.text}')
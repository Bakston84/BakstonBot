from loader import dp
from aiogram.types import Message
from Keyboards.Standart.dynamic_keyboard import games_keyboard

@dp.message_handler(commands=['games'])
async def games_commands(message: Message):
    await message.answer(f'{message.from_user.first_name}, во что поиграем?',
                         reply_markup=games_keyboard(message))
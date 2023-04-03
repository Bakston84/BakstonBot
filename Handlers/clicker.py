from loader import dp
from aiogram.types import Message
from Keyboards.Standart.dynamic_keyboard import clicker_keyboard

click = 0

@dp.message_handler(commands=['clicker'])
async def clicker_commands(message: Message):
    await message.answer(f'{message.from_user.first_name}, жмякай по кнопке!',
                         reply_markup=clicker_keyboard(message))
    global click
    click = 0

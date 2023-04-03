from loader import dp
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton

click = 0

@dp.message_handler()
async def all_commands(message: Message):
    global click
    if message.text == str(click):
        click += 1
        push_clicker = ReplyKeyboardMarkup(resize_keyboard=True)
        btn_push = KeyboardButton(text=f'{click}') # 1
        push_clicker.add(btn_push)
        if click % 10 == 0:
            await message.answer(f'{message.from_user.first_name}, уже {click} раз нажмякал!', reply_markup=push_clicker)
        else:
            await message.answer(click, reply_markup=push_clicker)
    else:
        await message.answer(f'{message.from_user.first_name}, смотри что поймал - '
                            f'{message.text}')
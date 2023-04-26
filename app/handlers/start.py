from aiogram.types import Message
from loader import dp

@dp.message_handler(commands=['start'])
async def cmd_start(message: Message):
    user_tg_id = message.from_user.id
    await dp.bot.send_message(message.from_user.id, text=user_tg_id)
from aiogram.types import Message
from aiogram.dispatcher import FSMContext
from loader import dp

@dp.message_handler(commands=['start'])
async def cmd_start(message: Message):
    tg_id = message.from_user.id
    await dp.bot.send_message(tg_id, text='Hi')
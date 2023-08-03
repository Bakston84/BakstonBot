from aiogram.types import Message, CallbackQuery
from loader import dp

from keyboards import sort_keyboard

@dp.message_handler(commands=['start'])
async def cmd_start(message: Message):
    tg_id = message.from_user.id
    data = [('test1', 'test2'), ('test3', 'test4')]
    await dp.bot.send_message(tg_id, 'Привет', reply_markup=sort_keyboard(data))

@dp.callback_query_handler(lambda call: True)
async def add_form_user(callback: CallbackQuery):
    tg_id = callback.from_user.id
    data = callback.data.split(':')
    await dp.bot.send_message(tg_id, data[1])

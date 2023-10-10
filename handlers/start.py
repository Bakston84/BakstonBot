from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher import FSMContext
from loader import dp
from bot_keyboards import callback_data, main_menu, games_menu

@dp.message_handler(commands=['start'])
async def cmd_start(message: Message):
    tg_id = message.from_user.id
    await dp.bot.send_message(tg_id, text='Меню:', reply_markup=main_menu)

@dp.callback_query_handler(callback_data.filter(name='app_games'))
async def call_app_games(callback: CallbackQuery):
    tg_id = callback.from_user.id
    await dp.bot.send_message(tg_id, text='Выбери игру', reply_markup=games_menu)
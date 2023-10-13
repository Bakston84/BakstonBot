from aiogram.types import Message, CallbackQuery
from loader import dp
from bot_keyboards import callback_data, main_menu, games_menu
from bot_db import user_bot, durak_cards

@dp.message_handler(commands=['start'])
async def cmd_start(message: Message):
    tg_id = message.from_user.id
    await dp.bot.send_message(tg_id, text='Меню:', reply_markup=main_menu)

@dp.callback_query_handler(callback_data.filter(name='app_games'))
async def call_app_games(callback: CallbackQuery):
    tg_id = callback.from_user.id
    if not user_bot.find_user(tg_id):
        data = dict(tg_id = tg_id,
                    durak_id = 0,
                    durak_position = 0)
        user_bot.add_user(data)
        data = dict(tg_id = tg_id,
                    deck = None)
        durak_cards.add_user_cards(data)
    await dp.bot.send_message(tg_id, text='Выбери игру', reply_markup=games_menu)
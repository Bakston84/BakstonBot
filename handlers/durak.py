from aiogram.types import Message, CallbackQuery
from loader import dp
from bot_keyboards import callback_data
from data import deck


@dp.callback_query_handler(callback_data.filter(name='g_durak'))
async def call_g_durak(callback: CallbackQuery):
    tg_id = callback.from_user.id
    await dp.bot.send_message(tg_id, text='Тасую колоду')
    await dp.bot.send_message(tg_id, text='Раздаю карты')
    cards = deck.create_deck()
    print(cards)

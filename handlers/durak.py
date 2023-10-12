from aiogram.types import Message, CallbackQuery
from loader import dp
from bot_keyboards import callback_data, open_durak_games
from data import deck
from bot_db import game_durak, user_bot


@dp.callback_query_handler(callback_data.filter(name='g_durak'))
async def call_g_durak(callback: CallbackQuery):
    tg_id = callback.from_user.id
    # Проверяем открытые сессии по tg_id
    user_game = game_durak.find_durak_tg_id(dict(admin_id = tg_id,
                                                 status = 'open'))
    # Если сессии по tg_id есть, то закрываем их и обнуляем пользователя
    if user_game:
        for u in user_game:
            data = dict(durak_id = u[0],
                        status = 'close')
            game_durak.update_durak_status(data)
            data = dict(tg_id = tg_id,
                        durak_id = 0,
                        durak_position = 0)
            user_bot.update_user(data)
    # ищем открытые сессии других пользователей:
    other_user = game_durak.find_durak_status(status='open')
    if other_user:
        await dp.bot.send_message(tg_id, text='Найдены открытые сессии:', reply_markup=open_durak_games(other_user))

    # cards = deck.create_deck()
    # data = dict(deck=str(cards),
    #             admin_id = tg_id,
    #             status='open')
    # game_durak.add_durak(data)

    #     data = dict(durak_id = game_durak.find_durak_tg_id(tg_id)[0],
    #                 status = 'close')
    #     game_durak.update_durak_status(data)

    # if not game_durak.find_durak_status(status='open'):
    #     cards = deck.create_deck()
    #     data = dict(deck=str(cards),
    #                 admin_id = tg_id,
    #                 status='open')
    #     game_durak.add_durak(data)  

    # cards = deck.create_deck()
    # data = dict(deck=str(cards),
    #             admin_id = tg_id,
    #             status='open')
    # game_durak.add_durak(data)

        # data = game_durak.find_durak_tg_id(admin_id=tg_id)
        # game_durak.update_durak_status(dict(durak_id = data[0],
        #                                     status = 'close'))
        # print('Сессия создана ', data)
    # else:
    #     if not game_durak.find_durak_status(status='open'):
    #         cards = deck.create_deck()
    #         data = dict(deck=str(cards),
    #                     admin_id = tg_id,
    #                     status='open')
    #         game_durak.add_durak(data)  
    #     else:
    #         await dp.bot.send_message(tg_id, text='Найдены открытые сессии:')
from aiogram import executor
from handlers import dp
from bot_db import user_bot, game_durak, durak_cards

async def on_start(_):
    try:
        user_bot.create_table_users()
        game_durak.create_table_durak()
        durak_cards.create_table_durak_cards()
        print('DB BOT connection... OK!')
    except:
        print('DB BOT connection... FAILURE!')
    print('BOT start... OK!')
    
executor.start_polling(dp, skip_updates=True, on_startup=on_start)
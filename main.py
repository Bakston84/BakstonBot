from aiogram import executor
from Handlers import dp
from Data import create_user_table

import os

async def on_start(_):

    try:
        create_user_table()
        print('DB connection... OK!')

    except:
        print('DB connection... FAILURE!')

    print('BOT start... OK!')

executor.start_polling(dp, skip_updates=True, on_startup=on_start)
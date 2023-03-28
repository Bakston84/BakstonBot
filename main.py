from aiogram import executor
from Handlers import dp

import os

async def on_start(_):
    print('Start Bot!')

executor.start_polling(dp, skip_updates=True, on_startup=on_start)
from aiogram import executor
from app import dp

async def on_start(_):
    print('BOT start... OK!')
executor.start_polling(dp, skip_updates=True, on_startup=on_start)
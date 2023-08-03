from aiogram import executor
from handlers import dp

async def on_start(_):
    print('BOT start... OK!')
executor.start_polling(dp, skip_updates=True, on_startup=on_start)
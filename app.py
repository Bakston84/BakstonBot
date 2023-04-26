from aiogram import executor
from loader import dp

async def on_start(_):
    # try:
    #     print('DB connection... OK!')
    # except:
    #     print('DB connection... FAILURE!')
    print('BOT start... OK!')

executor.start_polling(dp, skip_updates=True, on_startup=on_start)
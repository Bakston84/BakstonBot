from aiogram import Bot, Dispatcher
from aiogram import executor
from config_reader import config

bot = Bot(token = config.bot_token.get_secret_value())
dp = Dispatcher(bot)

async def on_start(_):
    print('Start Bot!')

executor.start_polling(dp, skip_updates=True, on_startup=on_start)
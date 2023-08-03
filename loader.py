from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram import Bot, Dispatcher
from data.config_reader import config

storage = MemoryStorage()
bot = Bot(token = config.bot_token.get_secret_value())
dp = Dispatcher(bot, storage=storage)
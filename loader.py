from aiogram import Bot, Dispatcher
from config_reader import config

import os

bot = Bot(token = config.bot_token.get_secret_value())
dp = Dispatcher(bot)
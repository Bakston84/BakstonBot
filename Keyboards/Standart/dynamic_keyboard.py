from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, Message

def games_keyboard(message: Message):
    kb_games = ReplyKeyboardMarkup(resize_keyboard=True)
    btn_clicker = KeyboardButton(text='/clicker')
    btn_back = KeyboardButton(text='Назад')
    kb_games.add(btn_clicker, btn_back)
    return kb_games

def clicker_keyboard(message: Message):
    kb_clicker = ReplyKeyboardMarkup(resize_keyboard=True)
    btn_click = KeyboardButton(text='0')
    kb_clicker.add(btn_click)
    return kb_clicker
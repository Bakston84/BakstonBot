from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb_main = ReplyKeyboardMarkup(resize_keyboard=True)

btn_start = KeyboardButton(text = '/start')
btn_help = KeyboardButton(text = '/help')
btn_location = KeyboardButton(text='Локация', request_location=True)
btn_phone = KeyboardButton(text='Телефон', request_contact=True)
btn_games = KeyboardButton(text='Игры')

kb_main.add(btn_start, btn_help)
kb_main.add(btn_location, btn_phone)
kb_main.add(btn_games)
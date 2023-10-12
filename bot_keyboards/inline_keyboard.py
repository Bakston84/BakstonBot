from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from .call_back import callback_data

main_menu = InlineKeyboardMarkup(row_width=1)
games_menu = InlineKeyboardMarkup(row_width=1)

games_button = InlineKeyboardButton(text='Игры', callback_data=callback_data.new(name='app_games'))
g_durak = InlineKeyboardButton(text='Дурак', callback_data=callback_data.new(name='g_durak'))

main_menu.row(games_button)
games_menu.row(g_durak)

def open_durak_games(data):
    open_sessions = InlineKeyboardMarkup(row_width=1)
    for i in data:
        open_sessions.row(InlineKeyboardButton(text=str(f'Сессия {i[0]}'), callback_data=callback_data.new(name=str(f'durak_session_{i[0]}'))))
    open_sessions.row(InlineKeyboardButton(text='Создать сессию', callback_data=callback_data.new(name='add_durak_session')))
    return open_sessions
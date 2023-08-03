from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from .call_back import main_keyboard_data

def sort_keyboard(data):
    sort_kb = InlineKeyboardMarkup(row_width=1)
    for i in data:
        sort_kb.row(InlineKeyboardButton(text=f'{i[0]}',
                                         callback_data=main_keyboard_data.new(data1=i[0], data2=i[1])))
    return sort_kb
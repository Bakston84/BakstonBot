import sqlite3
from config_reader import config

PATH = 'Data/db_user.db'

connect = sqlite3.connect(PATH)
cursor = connect.cursor()

def create_user_table():
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (user_id INTEGER PRIMARY KEY AUTOINCREMENT, tg_id INTEGER, last_name VARCHAR, first_name VARCHAR, comment VARCHAR)''')
    connect.commit()

def add_new_user(new_user: tuple):
    cursor.execute('''INSERT INTO users (tg_id, last_name, first_name, comment) VALUES (?, ?, ?, ?)''', new_user)
    connect.commit()

def find_user_tg_id(tg_id: tuple):
    find = cursor.execute('''SELECT tg_id FROM users WHERE tg_id = ?''', tg_id).fetchone()
    return find
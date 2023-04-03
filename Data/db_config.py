import sqlite3
from config_reader import config

# PATH = 'Data/db_user.db'

connect = sqlite3.connect(path = config.path.get_secret_value())
cursor = connect.cursor()
def create_user_table():
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (user_id INTEGER PRIMARY KEY AUTOINCREMENT, name VARCHAR, tg_id INTEGER, comment VARCHAR)''')
    connect.commit()



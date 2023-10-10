from bot_db import db_bot

class UserBot:
    def create_table_users(self):
        sql = '''CREATE TABLE IF NOT EXISTS users (
        tg_id INTEGER PRIMARY KEY)'''
        db_bot.__init__
        db_bot.execute(sql, commit=True)

user_bot = UserBot()
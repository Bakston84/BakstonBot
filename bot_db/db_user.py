from bot_db import db_bot

class UserBot:
    def create_table_users(self):
        sql = '''CREATE TABLE IF NOT EXISTS users (
        tg_id INTEGER PRIMARY KEY,
        durak_id INTEGER,
        durak_position INTEGER)'''
        db_bot.__init__
        db_bot.execute(sql, commit=True)

    def add_user(self, data:dict):
        parameters = (data.get('tg_id'),
                      data.get('durak_id'),
                      data.get('durak_position'))     
        sql = '''INSERT INTO users (tg_id, durak_id, durak_position) VALUES (?, ?, ?)'''
        db_bot.execute(sql, parameters, commit=True)

    def find_user(self, tg_id):
        parameters = (tg_id, )
        sql = '''SELECT * FROM users WHERE tg_id = ?'''
        return db_bot.execute(sql, parameters, fetchone=True)
    
    def update_user(self, data:dict):
        parameters = (data.get('durak_id'),
                      data.get('durak_position'),
                      data.get('tg_id'))
        sql = '''UPDATE users SET durak_id = ?, durak_position = ? WHERE tg_id = ?'''
        db_bot.execute(sql, parameters, commit=True)

user_bot = UserBot()
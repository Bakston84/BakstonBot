from bot_db import db_bot

class GameDurak:
    def create_table_durak(self):
        sql = '''CREATE TABLE IF NOT EXISTS durak (
        durak_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        deck VARCHAR,
        admin_id INTEGER,
        status VARCHAR)'''
        db_bot.__init__
        db_bot.execute(sql, commit=True)

    def add_durak(self, data:dict):
        parameters = (data.get('deck'),
                      data.get('admin_id'),
                      data.get('status'))
        sql = '''INSERT INTO durak (deck, admin_id, status) VALUES (?, ?, ?)'''
        db_bot.execute(sql, parameters, commit=True)

    def find_durak(self, durak_id):
        parameters = (durak_id, )
        sql = '''SELECT * FROM durak WHERE durak_id = ?'''
        return db_bot.execute(sql, parameters, fetchone=True)

    def find_durak_status(self, status):
        parameters = (status, )
        sql = '''SELECT * FROM durak WHERE status = ?'''
        return db_bot.execute(sql, parameters, fetchall=True)
    
    def find_durak_tg_id(self, data:dict):
        parameters = (data.get('admin_id'),
                      data.get('status'))
        sql = '''SELECT * FROM durak WHERE admin_id = ? AND status = ?'''
        return db_bot.execute(sql, parameters, fetchall=True)
    
    def update_durak_status(self, data:dict):
        parameters = (data.get('status'),
                      data.get('durak_id'))
        sql = '''UPDATE durak SET status = ? WHERE durak_id = ?'''
        db_bot.execute(sql, parameters, commit=True)

    def update_durak(self, data:dict):
        parameters = (data.get('deck'),
                      data.get('status'),
                      data.get('durak_id'))
        sql = '''UPDATE durak SET deck = ?, status = ? WHERE durak_id = ?'''
        db_bot.execute(sql, parameters, commit=True)

game_durak = GameDurak()
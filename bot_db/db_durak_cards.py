from bot_db import db_bot

class DurakCards:
    def create_table_durak_cards(self):
        sql = '''CREATE TABLE IF NOT EXISTS cards (
        tg_id INTEGER PRIMARY KEY,
        deck VARCHAR)'''
        db_bot.__init__
        db_bot.execute(sql, commit=True)

    def add_user_cards(self, data:dict):
        parameters = (data.get('tg_id'),
                      data.get('deck'))
        sql = '''INSERT INTO cards (tg_id, deck) VALUES (?, ?)'''
        db_bot.execute(sql, parameters, commit=True)

    def find_cards(self, tg_id):
        parameters = (tg_id, )
        sql = '''SELECT * FROM cards WHERE tg_id = ?'''
        return db_bot.execute(sql, parameters, fetchone=True)

    def update_user_cards(self, data:dict):
        parameters = (data.get('deck'),
                      data.get('tg_id'))
        sql = '''UPDATE cards SET deck = ? WHERE tg_id = ?'''
        db_bot.execute(sql, parameters, commit=True)


durak_cards = DurakCards()
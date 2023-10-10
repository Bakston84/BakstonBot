import sqlite3

class DataBase:
    def __init__(self, dp_path: str = 'bot_db/db_bot.db'):
        self.db_path = dp_path 

    @property
    def connection(self):
        return sqlite3.connect(self.db_path)
    
    def execute(self, sql: str, parameters: tuple = tuple(), fetchone = False, fetchall = False, commit = False):
        connection = self.connection
        cursor = connection.cursor()
        data = None
        cursor.execute(sql, parameters)
        if commit:
            connection.commit()
        if fetchone:
            data = cursor.fetchone()
        if fetchall:
            data = cursor.fetchall()
        connection.close()
        return data

db_bot = DataBase()
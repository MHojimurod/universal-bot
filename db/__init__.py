import sqlite3
from sqlite3.dbapi2 import Connection


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


class Db(Connection):
    def __init__(self, path: str):
        self.db = sqlite3.connect(path, check_same_thread=False)
        self.db.row_factory = dict_factory
        self.exec("""CREATE TABLE IF NOT EXISTS users   (
	"id"	INTEGER NOT NULL UNIQUE,
	"chat_id"	INTEGER NOT NULL UNIQUE,
	"language" INTEGER NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
	);""")

    def create_user(self, chat_id: int, language: int):
        self.exec(f"INSERT INTO users (chat_id, language)  VALUES (%s, %s)" % (chat_id, language))

    @property
    def cur(self): return self.db.cursor()

    def exec(self, sql: str, *args, **kwargs):
        res = self.cur.execute(sql, *args, **kwargs).fetchall()
        self.db.commit()
        return res
    def get_user(self, chat_id: int):
        users = self.exec(f"SELECT * FROM users WHERE chat_id={chat_id}")
        if len(users) > 0:
            return users[0]
        return None

import sqlite3
from sqlite3.dbapi2 import Connection


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


class Db(Connection):
    def __init__(self, path:str):
        super().__init__(path, check_same_threads=False)
        self.row_factory = dict_factory
        


    
    @property
    def cur(self): return self.db.cursor()

    def exec(self, sql:str, *args, **kwargs):
        return self.cur.execute(sql, *args, **kwargs).fetchall()
import sqlite3
from sqlite3 import Error
import os as os


def CreateConnection(db_file):
    global conn
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        conn.close()

if __name__=='__main__':
    path = os.path.abspath(__file__)
    directory = os.path.split(path)[0]
    dbname = "pythonsqlite.db"
    database = os.path.join(directory, dbname)
    CreateConnection(database)

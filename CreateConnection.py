import sqlite3
from sqlite3 import Error

def ConnectDB(db_file):
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
    return None

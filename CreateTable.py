from CreateConnection import ConnectDB
import sqlite3
import os as os

def CreateTable(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

path = os.path.abspath(__file__)
directory = os.path.split(path)[0]
dbname = "pythonsqlite.db"
database = os.path.join(directory, dbname) 

def main():
    music = '''CREATE TABLE IF NOT EXISTS music(id integer primary key, name text NOT NULL, artist text NOT NULL, audio blob, identified integer default 0);'''
    conn = ConnectDB(database)
    if conn is not None:
        CreateTable(conn, music)
    else:
        print("Error")    

def UpdateTable(identity, identified):
    conn = ConnectDB(database)
    cursor = conn.cursor()
    update = "update music set identified = ? where id = ?"
    param = (identity, identified)
    cursor.execute(update, param)
    conn.commit()
    
def ClearTable():
    conn = ConnectDB(database)
    cursor = conn.cursor()
    delete = '''DELETE FROM music'''
    cursor.execute(delete)
    conn.commit()
    clear = "Table Cleared"
    return clear

if __name__=='__main__':
    main()
    

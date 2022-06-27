'''
Example method:
def getObjectSelection(json):
    #Create ObjectSelection table if it doesn't exist
    with open('sql/ObjectSelection.sql') as f:
        conn = get_db_connection()
        conn.executescript(f.read())
        conn.commit()
        conn.close()
    conn = get_db_connection()

    #Insert any new objects into ObjectSelection
    for object in json:
        if object['createable'] == True:
            conn.execute('INSERT INTO ObjectSelection SELECT ?,?,false WHERE ? NOT IN (SELECT ObjectName FROM ObjectSelection)',(object['name'],object['label'],object['name']))
    conn.commit()
    conn.close()

'''
import sqlite3


def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn



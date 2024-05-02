import sqlite3
from sqlite3 import Error

conn = None
try:
    conn = sqlite3.connect("database.sqlite")
    conn_core = sqlite3.connect("core.sqlite")
except Error as e:
    print(e)
finally:
    if conn:
        conn.close()
    if conn_core:
        conn_core.close()

files = ["key.txt", "tenor.txt", "openai.txt"]
for file in files:
    try:
        tmp = open(file, "x")
    except FileExistsError:
        pass

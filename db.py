import sqlite3
from datetime import datetime

def log(user_id: int, first_name:str , request_time: str):
    
    conn = sqlite3.connect('logs.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        INSERT INTO logs (user_id, first_name, request_time)
        VALUES (?, ?, ?)
    ''', (user_id, first_name, request_time))

    conn.commit()
    conn.close()

def init_db():
    conn = sqlite3.connect('logs.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id TEXT NOT NULL,
            first_name TEXT NOT NULL,
            request_time TEXT NOT NULL
        )
    ''')

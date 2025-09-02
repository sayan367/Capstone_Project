import sqlite3

DB_NAME = "library.db"

def get_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn

def create_table():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS BOOKS (
            BOOK_ID INTEGER PRIMARY KEY AUTOINCREMENT,
            TITLE TEXT NOT NULL,
            AUTHOR TEXT NOT NULL,
            ISBN TEXT UNIQUE
        )
    """)
    conn.commit()
    conn.close()
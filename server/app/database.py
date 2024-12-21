import sqlite3
from app.config import settings


conn = sqlite3.connect(settings.database_url, check_same_thread=False)
cursor = conn.cursor()


def create_tables():
    cursor.execute(
        """
    CREATE TABLE IF NOT EXISTS posts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        subtitle TEXT,
        content TEXT,
        base64_image TEXT
    )
    """
    )

    cursor.execute(
        """
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL,
        role TEXT NOT NULL CHECK (role IN ('admin', 'author'))
    )
    """
    )
    conn.commit()


create_tables()  # Create tables on startup


def get_db():
    try:
        yield cursor, conn
    finally:
        pass

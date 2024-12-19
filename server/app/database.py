import sqlite3
import os
from app.config import settings

DATABASE_URL = os.environ.get("DATABASE_URL", "file:./blog.db")
conn = sqlite3.connect(DATABASE_URL, check_same_thread=False)
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


def create_initial_admin(hash_password):
    cursor.execute("SELECT COUNT(*) FROM users")
    user_count = cursor.fetchone()[0]

    if user_count == 0:
        if not settings.admin_username or not settings.admin_password:
            print(
                "ADMIN_USERNAME and ADMIN_PASSWORD environment variables must be set to create the initial admin user."
            )
            return

        hashed_password = hash_password(settings.admin_password)
        try:
            cursor.execute(
                """
                INSERT INTO users (username, password, role)
                VALUES (?, ?, ?)
            """,
                (settings.admin_username, hashed_password, "admin"),
            )
            conn.commit()
            print(f"Admin user '{settings.admin_username}' created.")
        except sqlite3.Error as e:
            conn.rollback()
            print(f"Error creating initial admin user: {e}")
    else:
        print("Users table already exists, skipping admin user creation.")


create_tables()  # Create tables on startup


def get_db():
    try:
        yield cursor, conn
    finally:
        pass

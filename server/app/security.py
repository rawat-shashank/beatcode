import hashlib
import secrets
import sqlite3
from fastapi import Depends, HTTPException, status
from app.models.users import User
from app.database import get_db


SALT_LENGTH = 16  # Recommended length for salt


async def get_current_user(username: str, password: str, db: tuple = Depends(get_db)):
    cursor, _ = db
    try:
        cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
        row = cursor.fetchone()
        if row:
            stored_hashed_password = row[2]  # Get the stored hashed password
            if verify_password(password, stored_hashed_password):
                user = User(id=row[0], username=row[1], role=row[3])
                return user
            else:
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Incorrect username or password",
                )
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect username or password",
            )
    except sqlite3.Error as e:  # noqa: F821
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Database error: {e}",
        )


def hash_password(password: str) -> str:
    """Hashes a password using a random salt and SHA256."""
    salt = secrets.token_bytes(SALT_LENGTH)
    salted_password = salt + password.encode("utf-8")
    hashed_password = hashlib.sha256(salted_password).hexdigest()
    return f"{salt.hex()}${hashed_password}"  # Store salt and hash


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verifies a plain password against a stored hash."""
    try:
        salt_hex, stored_hash = hashed_password.split("$")
        salt = bytes.fromhex(salt_hex)
        salted_password = salt + plain_password.encode("utf-8")
        computed_hash = hashlib.sha256(salted_password).hexdigest()
        return computed_hash == stored_hash
    except (ValueError, IndexError):
        return False  # Handle invalid hash format


async def require_admin(user: User = Depends(get_current_user)):  # Existing function
    if not user or user.role != "admin":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Insufficient privileges"
        )
    return user

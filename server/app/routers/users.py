import sqlite3
from fastapi import APIRouter, HTTPException, status, Depends
from typing import List
from ..models.users import User
from ..database import get_db
from ..security import require_admin, hash_password

router = APIRouter(prefix="/users", tags=["users"])


@router.post(
    "/",
    response_model=User,
    status_code=status.HTTP_201_CREATED,
    dependencies=[Depends(require_admin)],
)
async def create_user(user: User, db: tuple = Depends(get_db)):
    cursor, conn = db
    try:
        hashed_password = hash_password(user.password)  # Hash password before storing
        cursor.execute(
            """
            INSERT INTO users (username, password, role)
            VALUES (?, ?, ?)
        """,
            (user.username, hashed_password, user.role),
        )
        conn.commit()
        user.id = cursor.lastrowid
        return user
    except sqlite3.IntegrityError:
        conn.rollback()
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Username already exists"
        )
    except sqlite3.Error as e:
        conn.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Database error: {e}",
        )


@router.get("/", response_model=List[User], dependencies=[Depends(require_admin)])
async def get_all_users(db: tuple = Depends(get_db)):
    cursor, _ = db
    try:
        cursor.execute("SELECT * FROM users")
        rows = cursor.fetchall()
        users = [
            User(id=row[0], username=row[1], password="*** (hashed)", role=row[3])
            for row in rows
        ]  # Mask password
        return users
    except sqlite3.Error as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Database error: {e}",
        )


@router.get("/{user_id}", response_model=User, dependencies=[Depends(require_admin)])
async def get_user(user_id: int, db: tuple = Depends(get_db)):
    cursor, _ = db
    try:
        cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
        row = cursor.fetchone()
        if row:
            user = User(
                id=row[0], username=row[1], password="*** (hashed)", role=row[3]
            )  # Mask password
            return user
        else:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
            )
    except sqlite3.Error as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Database error: {e}",
        )

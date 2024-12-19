import sqlite3
from fastapi import APIRouter, HTTPException, status, Depends
from typing import List
from ..models.posts import Post
from ..database import get_db
from ..security import require_admin

router = APIRouter(prefix="/posts", tags=["posts"])

@router.post("/", response_model=Post, status_code=status.HTTP_201_CREATED)
async def create_post(post: Post, db: tuple = Depends(get_db)):
    cursor, conn = db
    try:
        cursor.execute("""
            INSERT INTO posts (title, subtitle, content, base64_image)
            VALUES (?, ?, ?, ?)
        """, (post.title, post.subtitle, post.content, post.base64_image))
        conn.commit()
        post.id = cursor.lastrowid
        return post
    except sqlite3.Error as e:
        conn.rollback()
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Database error: {e}")

@router.get("/", response_model=List[Post])
async def get_all_posts(db: tuple = Depends(get_db)):
    cursor, conn = db
    try:
        cursor.execute("SELECT * FROM posts")
        rows = cursor.fetchall()
        posts = [Post(id=row[0], title=row[1], subtitle=row[2], content=row[3], base64_image=row[4]) for row in rows]
        return posts
    except sqlite3.Error as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Database error: {e}")

@router.get("/{post_id}", response_model=Post)
async def get_post(post_id: int, db: tuple = Depends(get_db)):
    cursor, conn = db
    try:
        cursor.execute("SELECT * FROM posts WHERE id = ?", (post_id,))
        row = cursor.fetchone()
        if row:
            post = Post(id=row[0], title=row[1], subtitle=row[2], content=row[3], base64_image=row[4])
            return post
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")
    except sqlite3.Error as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Database error: {e}")

@router.put("/{post_id}", response_model=Post)
async def update_post(post_id: int, post: Post, db: tuple = Depends(get_db)):
    cursor, conn = db
    try:
        cursor.execute("""
            UPDATE posts SET title = ?, subtitle = ?, content = ?, base64_image = ?
            WHERE id = ?
        """, (post.title, post.subtitle, post.content, post.base64_image, post_id))
        conn.commit()
        if cursor.rowcount == 0:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")
        post.id = post_id
        return post
    except sqlite3.Error as e:
        conn.rollback()
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Database error: {e}")

@router.delete("/{post_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_post(post_id: int, db: tuple = Depends(get_db)):
    cursor, conn = db
    try:
        cursor.execute("DELETE FROM posts WHERE id = ?", (post_id,))
        conn.commit()
        if cursor.rowcount == 0:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")
    except sqlite3.Error as e:
        conn.rollback()
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Database error: {e}")
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from ..database import get_db
from ..schemas.posts import PostCreate, PostUpdate, PostSchema
from ..models.posts import Post, InputConstraint, Example
from ..models.topics import Topic

router = APIRouter(prefix="/posts", tags=["posts"])


@router.post("/", response_model=PostSchema, status_code=status.HTTP_201_CREATED)
def create_post(post: PostCreate, db: Session = Depends(get_db)):
    db_post = Post(
        url=post.url,
        title=post.title,
        description=post.description,
        difficulty=post.difficulty,
    )
    if post.input_constraints:
        db_post.input_constraints = [
            InputConstraint(**ic.model_dump(), post=db_post) for ic in post.input_constraints
        ]
    if post.examples:
        db_post.examples = [Example(**ex.model_dump(), post=db_post) for ex in post.examples]
    if post.topics:
        db_post.topics = db.query(Topic).filter(Topic.id.in_(post.topics)).all()
    db.add(db_post)
    try:
        db.commit()
        db.refresh(db_post)
        return db_post
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=f"Error creating post: {e}")


@router.get("/", response_model=List[PostSchema])
def read_posts(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(Post).offset(skip).limit(limit).all()


@router.get("/{post_id}", response_model=PostSchema)
def read_post(post_id: int, db: Session = Depends(get_db)):
    post = db.query(Post).filter(Post.id == post_id).first()
    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Post not found"
        )
    return post


@router.put("/{post_id}", response_model=PostSchema)
def update_post(post_id: int, post_update: PostUpdate, db: Session = Depends(get_db)):
    db_post = db.query(Post).filter(Post.id == post_id).first()
    if not db_post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Post not found"
        )

    for key, value in post_update.model_dump(exclude_unset=True).items():
        if key == "input_constraints":
            db_post.input_constraints.clear()
            if value:
                db_post.input_constraints.extend(
                    [InputConstraint(**ic.dict(), post=db_post) for ic in value]
                )
        elif key == "examples":
            db_post.examples.clear()
            if value:
                db_post.examples.extend(
                    [Example(**ex.dict(), post=db_post) for ex in value]
                )
        elif key == "topics":
            db_post.topics = db.query(Topic).filter(Topic.id.in_(value)).all()
        else:
            setattr(db_post, key, value)
    try:
        db.commit()
        db.refresh(db_post)
        return db_post
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=f"Error updating post: {e}")


@router.delete("/{post_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(post_id: int, db: Session = Depends(get_db)):
    post = db.query(Post).filter(Post.id == post_id).first()
    if post:
        db.delete(post)
        try:
            db.commit()
            return
        except Exception as e:
            db.rollback()
            raise HTTPException(status_code=500, detail=f"Error deleting post: {e}")
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")

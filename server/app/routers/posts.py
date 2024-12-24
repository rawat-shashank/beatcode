from fastapi import APIRouter, HTTPException, status, Depends
from typing import List
from sqlmodel import Session, select
from sqlalchemy.orm import selectinload

from ..models.posts import Post, PostCreate
from ..models.topics import Topic
from ..database import get_session


# Define the database engine (assuming the connection string is in get_db)
# engine = create_engine(get_session())

router = APIRouter(prefix="/posts", tags=["posts"])


@router.post("/", response_model=Post, status_code=status.HTTP_201_CREATED)
async def create_post(post_create: PostCreate, db: Session = Depends(get_session)):
    try:
        
        post = Post(
            url=post_create.url,
            title=post_create.title,
            description=post_create.description,
            difficulty=post_create.difficulty,
            input_constraints=post_create.input_constraints,
            examples=post_create.examples,
        )
        for topic_id in post_create.topics:
            db_topic = db.get(Topic, topic_id)
            if db_topic:
                post.topics.append(db_topic)

        print("---> ")
        print("---> ", post)
        print("---> ")

        db.add(post)
        db.commit()
        db.refresh(post)
        return post
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Database error: {str(e)}",
        )


@router.get("/", response_model=List[Post])
async def get_all_posts(db: Session = Depends(get_session)):
    posts = db.exec(select(Post).options(selectinload(Post.topics)))
    return posts


@router.get("/{post_id}", response_model=Post)
async def get_post(post_id: int, db: Session = Depends(get_session)):
    post = db.get(Post, post_id)
    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Post not found"
        )
    return post


@router.put("/{post_id}", response_model=Post)
async def update_post(post_id: int, post: Post, db: Session = Depends(get_session)):
    existing_post = db.get(Post, post_id)
    if not existing_post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Post not found"
        )

    for field, value in post.model_dump().items():
        setattr(existing_post, field, value)

    db.commit()
    db.refresh(existing_post)
    return existing_post


@router.delete("/{post_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_post(post_id: int, db: Session = Depends(get_session)):
    post = db.get(Post, post_id)
    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Post not found"
        )

    db.delete(post)
    db.commit()
    return post

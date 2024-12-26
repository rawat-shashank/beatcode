from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from ..database import get_db
from ..models.topics import Topic
from ..schemas.topics import TopicCreate, TopicSchema

router = APIRouter(prefix="/topics", tags=["topics"])


@router.post("/", response_model=TopicSchema, status_code=status.HTTP_201_CREATED)
def create_topic(topic: TopicCreate, db: Session = Depends(get_db)):
    db_topic = Topic(**topic.model_dump())
    db.add(db_topic)
    try:
        db.commit()
        db.refresh(db_topic)
        return db_topic
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=f"Error creating topic: {e}")


@router.get("/", response_model=List[TopicSchema])
def read_topics(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(Topic).offset(skip).limit(limit).all()


@router.get("/{topic_id}", response_model=TopicSchema)
def read_topic(topic_id: int, db: Session = Depends(get_db)):
    topic = db.query(Topic).filter(Topic.id == topic_id).first()
    if not topic:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Topic not found"
        )
    return topic


@router.put("/{topic_id}", response_model=TopicSchema)
def update_topic(
    topic_id: int, topic_update: TopicCreate, db: Session = Depends(get_db)
):
    db_topic = db.query(Topic).filter(Topic.id == topic_id).first()
    if not db_topic:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Topic not found"
        )
    for key, value in topic_update.model_dump(exclude_unset=True).items():
        setattr(db_topic, key, value)
    try:
        db.commit()
        db.refresh(db_topic)
        return db_topic
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=f"Error updating topic: {e}")


@router.delete("/{topic_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_topic(topic_id: int, db: Session = Depends(get_db)):
    topic = db.query(Topic).filter(Topic.id == topic_id).first()
    if topic:
        db.delete(topic)
        try:
            db.commit()
            return
        except Exception as e:
            db.rollback()
            raise HTTPException(status_code=500, detail=f"Error deleting topic: {e}")
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Topic not found")

@router.get("/{topic_id}/posts", status_code=status.HTTP_200_OK)
def get_topic_posts(topic_id: int, db: Session = Depends(get_db)):
    topic = db.query(Topic).filter(Topic.id == topic_id).first()
    posts = []
    if topic:
        posts = topic.posts
    return posts

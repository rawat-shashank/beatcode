from fastapi import APIRouter, HTTPException, status, Depends
from typing import List
from sqlmodel import Session, select

from ..models.topics import Topic, TopicCreate
from ..models.posts import Post
from ..database import get_session


# Define the database engine (assuming the connection string is in get_db)
# engine = create_engine(get_session())

router = APIRouter(prefix="/topics", tags=["topics"])


@router.post("/", response_model=Topic, status_code=status.HTTP_201_CREATED)
async def create_topic(topic_create: TopicCreate, db: Session = Depends(get_session)):
    try:
        topic = Topic(topic=topic_create.topic)
        db.add(topic)
        db.commit()
        db.refresh(topic)
        return topic
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Database error: {str(e)}",
        )


@router.get("/", response_model=List[Topic])
async def get_all_topics(db: Session = Depends(get_session)):
    topics = db.exec(select(Topic))
    return topics


@router.get("/{topic_id}", response_model=Topic)
async def get_topic(topic_id: int, db: Session = Depends(get_session)):
    topic = db.get(Topic, topic_id)
    if not topic:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Topic not found"
        )
    return topic


@router.put("/{topic_id}", response_model=Topic)
async def update_topic(
    topic_id: int, topic_create: TopicCreate, db: Session = Depends(get_session)
):
    existing_topic = db.get(Topic, topic_id)
    if not existing_topic:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Topic not found"
        )

    for field, value in topic_create.model_dump().items():
        setattr(existing_topic, field, value)

    db.commit()
    db.refresh(existing_topic)
    return existing_topic


@router.delete("/{topic_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_topic(topic_id: int, db: Session = Depends(get_session)):
    topic = db.get(Topic, topic_id)
    if not topic:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Topic not found"
        )

    db.delete(topic)
    db.commit()
    return topic


@router.get("/{topic_id}/posts", response_model=List[Post])
async def get_posts_by_topic(topic_id: int, db: Session = Depends(get_session)):
    topic = db.exec(select(Topic).filter(Topic.id == topic_id)).first()
    if not topic:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Topic not found"
        )
    return topic.posts

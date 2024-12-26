# # from fastapi import APIRouter, HTTPException, status, Depends
# # from typing import List
# # from sqlmodel import Session, select
# #
# # from ..models.topics import Topic, TopicCreate
# # from ..models.posts import Post
# # from ..database import get_session
# #
# #
# # # Define the database engine (assuming the connection string is in get_db)
# # # engine = create_engine(get_session())
# #
# # router = APIRouter(prefix="/topics", tags=["topics"])
# #
# #
# # @router.post("/", response_model=Topic, status_code=status.HTTP_201_CREATED)
# # async def create_topic(topic_create: TopicCreate, db: Session = Depends(get_session)):
# #     try:
# #         topic = Topic(topic=topic_create.topic)
# #         db.add(topic)
# #         db.commit()
# #         db.refresh(topic)
# #         return topic
# #     except Exception as e:
# #         raise HTTPException(
# #             status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
# #             detail=f"Database error: {str(e)}",
# #         )
# #
# #
# # @router.get("/", response_model=List[Topic])
# # async def get_all_topics(db: Session = Depends(get_session)):
# #     topics = db.exec(select(Topic))
# #     return topics
# #
# #
# # @router.get("/{topic_id}", response_model=Topic)
# # async def get_topic(topic_id: int, db: Session = Depends(get_session)):
# #     topic = db.get(Topic, topic_id)
# #     if not topic:
# #         raise HTTPException(
# #             status_code=status.HTTP_404_NOT_FOUND, detail="Topic not found"
# #         )
# #     return topic
# #
# #
# # @router.put("/{topic_id}", response_model=Topic)
# # async def update_topic(
# #     topic_id: int, topic_create: TopicCreate, db: Session = Depends(get_session)
# # ):
# #     existing_topic = db.get(Topic, topic_id)
# #     if not existing_topic:
# #         raise HTTPException(
# #             status_code=status.HTTP_404_NOT_FOUND, detail="Topic not found"
# #         )
# #
# #     for field, value in topic_create.model_dump().items():
# #         setattr(existing_topic, field, value)
# #
# #     db.commit()
# #     db.refresh(existing_topic)
# #     return existing_topic
# #
# #
# # @router.delete("/{topic_id}", status_code=status.HTTP_204_NO_CONTENT)
# # async def delete_topic(topic_id: int, db: Session = Depends(get_session)):
# #     topic = db.get(Topic, topic_id)
# #     if not topic:
# #         raise HTTPException(
# #             status_code=status.HTTP_404_NOT_FOUND, detail="Topic not found"
# #         )
# #
# #     db.delete(topic)
# #     db.commit()
# #     return topic
# #
# #
# # @router.get("/{topic_id}/posts", response_model=List[Post])
# # async def get_posts_by_topic(topic_id: int, db: Session = Depends(get_session)):
# #     topic = db.exec(select(Topic).filter(Topic.id == topic_id)).first()
# #     if not topic:
# #         raise HTTPException(
# #             status_code=status.HTTP_404_NOT_FOUND, detail="Topic not found"
# #         )
# #     return topic.posts


# from typing import List

# from fastapi import APIRouter, Depends, HTTPException, status
# from sqlalchemy.orm import Session

# from app.models import Topic
# from app.schemas import topics

# from ..database import get_db

# router = APIRouter(prefix="/topics", tags=["topics"])


# @router.post("/", response_model=topics.Topic, status_code=status.HTTP_201_CREATED)
# def create_topic(topic: topics.TopicCreate, db: Session = Depends(get_db)):
#     db_topic = db.query(Topic).filter(Topic.topic == topic.topic).first()
#     if db_topic:
#         raise HTTPException(status_code=400, detail="Topic already exists")
#     db_topic = Topic(**topic.model_dump())
#     db.add(db_topic)
#     db.commit()
#     db.refresh(db_topic)
#     return db_topic


# @router.get("/", response_model=List[topics.Topic])
# def read_topics(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#     topics = db.query(Topic).offset(skip).limit(limit).all()
#     return topics


# @router.get("/{topic_id}", response_model=topics.Topic)
# def read_topic(topic_id: int, db: Session = Depends(get_db)):
#     db_topic = db.query(Topic).filter(Topic.id == topic_id).first()
#     if db_topic is None:
#         raise HTTPException(status_code=404, detail="Topic not found")
#     return db_topic


# @router.put("/{topic_id}", response_model=topics.Topic)
# def update_topic(
#     topic_id: int, topic: topics.TopicUpdate, db: Session = Depends(get_db)
# ):
#     db_topic = db.query(Topic).filter(Topic.id == topic_id).first()
#     if db_topic is None:
#         raise HTTPException(status_code=404, detail="Topic not found")
#     for var, value in vars(topic).items():
#         if value is not None:
#             setattr(db_topic, var, value)
#     db.commit()
#     db.refresh(db_topic)
#     return db_topic


# @router.delete("/{topic_id}", status_code=status.HTTP_204_NO_CONTENT)
# def delete_topic(topic_id: int, db: Session = Depends(get_db)):
#     db_topic = db.query(Topic).filter(Topic.id == topic_id).first()
#     if db_topic is None:
#         raise HTTPException(status_code=404, detail="Topic not found")
#     db.delete(db_topic)
#     db.commit()
#     return


from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

# You MUST define these elsewhere (database setup, models, schemas)
# I am ONLY showing the route logic and direct db interaction
from ..database import get_db
from ..models.topics import Topic
from ..schemas.topics import TopicCreate, TopicSchema

router = APIRouter(prefix="/topics", tags=["topics"])


@router.post("/", response_model=TopicSchema, status_code=status.HTTP_201_CREATED)
def create_topic(topic: TopicCreate, db: Session = Depends(get_db)):
    db_topic = Topic(**topic.dict())
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
    for key, value in topic_update.dict(exclude_unset=True).items():
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

from typing import TYPE_CHECKING, List
from sqlmodel import SQLModel, Field, Relationship

if TYPE_CHECKING:
    from .posts import Post


class PostTopicLink(SQLModel, table=True):
    post_id: int | None = Field(default=None, foreign_key="posts.id", primary_key=True)
    topic_id: int | None = Field(
        default=None, foreign_key="topics.id", primary_key=True
    )


class TopicCreate(SQLModel):
    topic: str = Field(
        unique=True, max_length=255, description="Topic to identify problem type"
    )


class Topic(TopicCreate, table=True):
    __tablename__ = "topics"

    id: int | None = Field(default=None, primary_key=True, index=True)
    posts: List["Post"] = Relationship(
        back_populates="topics", link_model=PostTopicLink
    )

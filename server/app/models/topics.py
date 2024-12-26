# from sqlalchemy import Column, Integer, String
# from sqlalchemy.orm import relationship
# from ..models import BaseModel

# # class PostTopicLink(SQLModel, table=True):
# #     post_id: int | None = Field(default=None, foreign_key="posts.id", primary_key=True)
# #     topic_id: int | None = Field(
# #         default=None, foreign_key="topics.id", primary_key=True
# #     )


# class Topic(BaseModel):
#     __tablename__ = "topics"
#     id = Column(Integer, primary_key=True, index=True)
#     topic = Column(String, unique=True, index=True, nullable=False)
#     posts = relationship("Post", secondary="post_topic_link", back_populates="topics")


from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from . import Base

post_topic_link = Table(
    "post_topic_link",
    Base.metadata,
    Column("post_id", Integer, ForeignKey("posts.id"), primary_key=True),
    Column("topic_id", Integer, ForeignKey("topics.id"), primary_key=True),
)


class Topic(Base):
    __tablename__ = "topics"
    id = Column(Integer, primary_key=True, index=True)
    topic = Column(String, unique=True)
    posts = relationship("Post", secondary=post_topic_link, back_populates="topics")

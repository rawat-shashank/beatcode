from sqlalchemy import Column, Integer, String, Enum, ForeignKey
from sqlalchemy.orm import relationship
from . import Base
from enum import Enum as PyEnum


class Difficulty(PyEnum):
    Easy = "Easy"
    Medium = "Medium"
    Hard = "Hard"


class Example(Base):
    __tablename__ = "examples"
    id = Column(Integer, primary_key=True, index=True)
    post_id = Column(Integer, ForeignKey("posts.id"))
    input = Column(String)
    output = Column(String)
    explanation = Column(String, nullable=True)
    post = relationship("Post", back_populates="examples")


class InputConstraint(Base):
    __tablename__ = "input_constraints"
    id = Column(Integer, primary_key=True, index=True)
    post_id = Column(Integer, ForeignKey("posts.id"))
    constraint = Column(String)
    post = relationship("Post", back_populates="input_constraints")


class Post(Base):
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True, index=True)
    url = Column(String, unique=True, index=True)
    title = Column(String)
    description = Column(String)
    difficulty = Column(Enum(Difficulty))
    input_constraints = relationship(
        "InputConstraint", back_populates="post", cascade="all, delete-orphan"
    )
    examples = relationship(
        "Example", back_populates="post", cascade="all, delete-orphan"
    )
    topics = relationship("Topic", secondary="post_topic_link", back_populates="posts")

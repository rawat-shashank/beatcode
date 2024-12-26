# from typing import List, Any, Optional
# from sqlmodel import SQLModel, Field, Column, JSON, Relationship
# from enum import Enum
#
# from app.models.topics import Topic, PostTopicLink
#
#
# class Difficulty(str, Enum):
#     Easy = "Easy"
#     Meidum = "Meidum"
#     Hard = "Hard"
#
#
# class Example(SQLModel):
#     input: Any = Field(description="Input values for the example")
#     output: Any = Field(description="Expected output for the given input")
#     explanation: str | None = Field(
#         None, description="Explanation of why the output is correct"
#     )
#
#
# class InputConstraint(SQLModel):
#     constraint: str = Field(
#         default=None, description="Limits on the size or values of the input"
#     )
#
#
# class PostBase(SQLModel):
#     url: str = Field(unique=True, description="The URL of the LeetCode problem")
#     title: str = Field(..., description="A concise name summarizing the problem")
#     description: str = Field(
#         ..., description="A clear and detailed explanation of the problem"
#     )
#     difficulty: Difficulty = Field(default=None)
#     input_constraints: List[InputConstraint] | None = Field(sa_column=Column(JSON))
#     examples: List[Example] | None = Field(sa_column=Column(JSON))
#
#     def __post_load__(self):
#         if self.examples:
#             self.examples = [Example(**example_dict) for example_dict in self.examples]
#         if self.input_constraints:
#             self.input_constraints = [
#                 InputConstraint(**input_constraint_dict)
#                 for input_constraint_dict in self.input_constraints
#             ]
#
#     def __pre_dump__(self):
#         if self.examples:
#             self.examples = [example.model_dump() for example in self.examples]
#         if self.input_constraints:
#             self.input_constraints = [
#                 input_constraint.model_dump()
#                 for input_constraint in self.input_constraints
#             ]
#
#
# class PostCreate(PostBase):
#     topics: List[int] = []
#
#
# class Post(PostBase, table=True):
#     __tablename__ = "posts"
#
#     id: int = Field(primary_key=True, index=True)
#     topics: List[Topic] = Relationship(back_populates="posts", link_model=PostTopicLink)


# from sqlalchemy import Column, Integer, String, JSON, Enum, ForeignKey
# from sqlalchemy.orm import relationship
# from sqlalchemy.ext.declarative import declarative_base
# from typing import List, Optional
# import enum

# Base = declarative_base()


# class Difficulty(enum.Enum):
#     Easy = "Easy"
#     Medium = "Medium"  # Corrected typo
#     Hard = "Hard"


# class Example(Base):
#     __tablename__ = "examples"
#     id = Column(Integer, primary_key=True, index=True)
#     post_id = Column(Integer, ForeignKey("posts.id"))
#     input = Column(JSON)
#     output = Column(JSON)
#     explanation = Column(String, nullable=True)


# class InputConstraint(Base):
#     __tablename__ = "input_constraints"
#     id = Column(Integer, primary_key=True, index=True)
#     post_id = Column(Integer, ForeignKey("posts.id"))
#     constraint = Column(String)


# class Post(Base):
#     __tablename__ = "posts"

#     id = Column(Integer, primary_key=True, index=True)
#     url = Column(String, unique=True, index=True)
#     title = Column(String)
#     description = Column(String)
#     difficulty = Column(Enum(Difficulty))
#     input_constraints = relationship("InputConstraint", back_populates="post")
#     examples = relationship("Example", back_populates="post")


# class PostTopicLink(Base):
#     __tablename__ = "post_topic_link"
#     post_id = Column(Integer, ForeignKey("posts.id"), primary_key=True)
#     topic_id = Column(Integer, ForeignKey("topics.id"), primary_key=True)


from sqlalchemy import Column, Integer, String, JSON, Enum, ForeignKey, Table
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
    input = Column(JSON)
    output = Column(JSON)
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

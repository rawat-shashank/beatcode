from typing import List, Any, Optional
from sqlmodel import SQLModel, Field, Column, JSON, Relationship
from enum import Enum

from app.models.topics import Topic, PostTopicLink


class Difficulty(str, Enum):
    Easy = "Easy"
    Meidum = "Meidum"
    Hard = "Hard"


class Example(SQLModel):
    input: Any = Field(description="Input values for the example")
    output: Any = Field(description="Expected output for the given input")
    explanation: str | None = Field(
        None, description="Explanation of why the output is correct"
    )


class InputConstraint(SQLModel):
    constraint: str = Field(
        default=None, description="Limits on the size or values of the input"
    )


class PostBase(SQLModel):
    url: str = Field(unique=True, description="The URL of the LeetCode problem")
    title: str = Field(..., description="A concise name summarizing the problem")
    description: str = Field(
        ..., description="A clear and detailed explanation of the problem"
    )
    difficulty: Difficulty = Field(default=None)
    input_constraints: List[InputConstraint] | None = Field(sa_column=Column(JSON))
    examples: List[Example] | None = Field(sa_column=Column(JSON))

    def __post_load__(self):
        if self.examples:
            self.examples = [Example(**example_dict) for example_dict in self.examples]
        if self.input_constraints:
            self.input_constraints = [
                InputConstraint(**input_constraint_dict)
                for input_constraint_dict in self.input_constraints
            ]

    def __pre_dump__(self):
        if self.examples:
            self.examples = [example.model_dump() for example in self.examples]
        if self.input_constraints:
            self.input_constraints = [
                input_constraint.model_dump()
                for input_constraint in self.input_constraints
            ]


class PostCreate(PostBase):
    topics: List[int] = []


class Post(PostBase, table=True):
    __tablename__ = "posts"

    id: int = Field(primary_key=True, index=True)
    topics: List[Topic] = Relationship(back_populates="posts", link_model=PostTopicLink)

from typing import List, Optional
from pydantic import BaseModel
from enum import Enum as PyEnum

from .topics import TopicSchema

class Difficulty(str, PyEnum):  # Fix: Using str enum for schemas
    Easy = "Easy"
    Medium = "Medium"
    Hard = "Hard"


class ExampleCreate(BaseModel):
    input: str
    output: str
    explanation: Optional[str] = None


class InputConstraintCreate(BaseModel):
    constraint: str


class PostCreate(BaseModel):
    url: str
    title: str
    description: str
    difficulty: Difficulty
    input_constraints: Optional[List[InputConstraintCreate]] = None
    examples: Optional[List[ExampleCreate]] = None
    topics: Optional[List[int]] = None


class PostUpdate(BaseModel):
    url: Optional[str] = None
    title: Optional[str] = None
    description: Optional[str] = None
    difficulty: Optional[Difficulty] = None
    input_constraints: Optional[List[InputConstraintCreate]] = None
    examples: Optional[List[ExampleCreate]] = None
    topics: Optional[List[int]] = None


class PostSchema(BaseModel):
    id: int
    url: str
    title: str
    description: str
    difficulty: Difficulty
    input_constraints: Optional[List[InputConstraintCreate]] = None
    examples: Optional[List[ExampleCreate]] = None
    topics: Optional[List[TopicSchema]] = None

    class Config:
        from_attributes = True

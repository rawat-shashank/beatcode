from pydantic import BaseModel, Field
from typing import Optional

class Post(BaseModel):
    id: Optional[int] = None
    url: str = Field(..., min_length=1, max_length=255)
    title: str = Field(..., min_length=1, max_length=255)
    problem_statement: str = Field(None)
    examples: list[any] | None = Field(None, list[any]),

    content: Optional[str] = None
    base64_image: Optional[str] = None
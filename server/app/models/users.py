from pydantic import BaseModel, Field
from typing import Optional


class User(BaseModel):
    id: Optional[int] = None
    username: str = Field(..., min_length=3, max_length=50)
    password: str = Field(..., min_length=8)
    role: str = Field(..., pattern="^(admin|author)$")  # Use pattern instead of regex


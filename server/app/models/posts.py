from pydantic import BaseModel, Field
from typing import Optional

class Post(BaseModel):
    id: Optional[int] = None
    title: str = Field(..., min_length=1, max_length=255)
    subtitle: Optional[str] = Field(None, max_length=255)
    content: Optional[str] = None
    base64_image: Optional[str] = None
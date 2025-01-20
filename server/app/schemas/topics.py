from pydantic import BaseModel


class TopicCreate(BaseModel):
    topic: str


class TopicSchema(BaseModel):
    id: int
    topic: str

    class Config:
        from_attributes = True

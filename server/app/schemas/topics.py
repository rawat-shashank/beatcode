# from typing import Annotated, Optional
# from datetime import datetime
# from pydantic import BaseModel, constr


# class TopicBase(BaseModel):
#     topic: Annotated[str, constr(min_length=3, max_length=255)]


# class TopicCreate(TopicBase):
#     pass


# class TopicUpdate(TopicBase):
#     pass


# class TopicInDBBase(TopicBase):
#     id: int
#     created_at: datetime
#     updated_at: Optional[datetime] = None

#     class Config:
#         from_attributes = True


# class Topic(TopicInDBBase):
#     pass


from pydantic import BaseModel


class TopicCreate(BaseModel):
    topic: str


class TopicSchema(BaseModel):
    id: int
    topic: str

    class Config:
        from_attributes = True

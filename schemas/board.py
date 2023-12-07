import datetime
from pydantic import BaseModel
from .post import PostReadsDto


class BoardCreateDto(BaseModel):
    subject: str
    description: str


class BoardReadDto(BaseModel):
    id: int
    subject: str
    description: str
    create_date: datetime.datetime
    posts: list[PostReadsDto]

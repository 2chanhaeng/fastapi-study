import datetime
from pydantic import BaseModel


class BoardCreateDto(BaseModel):
    subject: str
    description: str


class BoardReadDto(BaseModel):
    id: int
    subject: str
    description: str
    create_date: datetime.datetime

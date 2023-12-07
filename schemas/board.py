import datetime

from pydantic import BaseModel


class BoardCreateDto(BaseModel):
    subject: str
    description: str


class BoardResponseDto(BaseModel):
    id: int
    subject: str
    description: str
    create_date: datetime.datetime

from uuid import UUID
import datetime

from pydantic import BaseModel


class BoardCreateDto(BaseModel):
    subject: str
    description: str


class BoardResponseDto(BaseModel):
    id: UUID
    subject: str
    description: str
    create_date: datetime.datetime

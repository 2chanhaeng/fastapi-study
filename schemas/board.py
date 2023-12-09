import datetime

from pydantic import BaseModel, field_validator

from .post import PostReadsDto


class BoardCreateDto(BaseModel):
    subject: str
    description: str

    @field_validator("subject")
    def subject_must_not_be_empty(cls, v: str):
        if v.strip() == "":
            raise ValueError("must not be empty")
        return v

    @field_validator("description")
    def description_must_not_be_empty(cls, v: str):
        if v.strip() == "":
            raise ValueError("must not be empty")
        return v


class BoardCreatedDto(BaseModel):
    subject: str


class BoardReadDto(BaseModel):
    id: int
    subject: str
    description: str
    create_date: datetime.datetime
    posts: list[PostReadsDto]

import datetime

from pydantic import BaseModel, field_validator


class PostCreateDto(BaseModel):
    subject: str
    content: str

    @field_validator("subject")
    def subject_must_not_be_empty(cls, v: str):
        if v.strip() == "":
            raise ValueError("must not be empty")
        return v

    @field_validator("content")
    def content_must_not_be_empty(cls, v: str):
        if v.strip() == "":
            raise ValueError("must not be empty")
        return v

    def __repr__(self) -> str:
        return f"<PostCreateDto subject={self.subject} content={self.content}>"


class PostCreatedDto(BaseModel):
    id: int


class PostReadsDto(BaseModel):
    id: int
    subject: str


class PostReadDto(BaseModel):
    id: int
    subject: str
    content: str
    create_date: datetime.datetime
    board_id: int

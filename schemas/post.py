import datetime
from pydantic import BaseModel, field_validator


class PostCreateDto(BaseModel):
    subject: str
    content: str
    board_id: int

    @field_validator("subject")
    def subject_must_not_be_empty(cls, v):
        if v == "":
            raise ValueError("must not be empty")
        return v

    @field_validator("content")
    def content_must_not_be_empty(cls, v):
        if v == "":
            raise ValueError("must not be empty")
        return v

    @field_validator("board_id")
    def board_id_must_be_positive(cls, v):
        if v <= 0:
            raise ValueError("wrong board id")
        return v


class PostReadsDto(BaseModel):
    id: int
    subject: str


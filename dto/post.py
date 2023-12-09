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

    def __str__(self) -> str:
        return f"DTO to create post about '{self.subject}'"

    def __repr__(self) -> str:
        return (
            f"PostCreateDto(subject={repr(self.subject)}, "
            f"content={repr(self.content)})"
        )


class PostCreatedDto(BaseModel):
    id: int

    def __str__(self) -> str:
        return f"DTO of created post( {self.id} )"

    def __repr__(self) -> str:
        return f"PostCreatedDto(id={repr(self.id)})"


class PostReadsDto(BaseModel):
    id: int
    subject: str

    def __str__(self) -> str:
        return f"DTO of posts( {self.id} ) about '{self.subject}'"

    def __repr__(self) -> str:
        return f"PostReadsDto(id={repr(self.id)}, subject={repr(self.subject)})"


class PostReadDto(BaseModel):
    id: int
    subject: str
    content: str
    create_date: datetime.datetime
    board_id: int

    def __str__(self) -> str:
        return (
            f"DTO of post( {self.id} ) "
            f"about '{self.subject}' "
            f"in board( {self.board_id} )"
            f"created at {self.create_date}"
        )

    def __repr__(self) -> str:
        return (
            f"PostReadDto(id={repr(self.id)}, "
            f"subject={repr(self.subject)}, "
            f"content={repr(self.content)}, "
            f"create_date={repr(self.create_date)}, "
            f"board_id={repr(self.board_id)})"
        )

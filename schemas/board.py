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

    def __str__(self) -> str:
        return f"DTO to create board about '{self.subject}'"

    def __repr__(self) -> str:
        return (
            f"BoardCreateDto(subject={repr(self.subject)}, "
            f"description={repr(self.description)})"
        )


class BoardCreatedDto(BaseModel):
    subject: str

    def __str__(self) -> str:
        return f"DTO of created board about '{self.subject}'"

    def __repr__(self) -> str:
        return f"BoardCreatedDto(subject={repr(self.subject)})"


class BoardReadDto(BaseModel):
    id: int
    subject: str
    description: str
    create_date: datetime.datetime
    posts: list[PostReadsDto]

    def __str__(self) -> str:
        return (
            f"DTO of board( {self.id} ) "
            f"about '{self.subject}' "
            f"created at {self.create_date}"
        )

    def __repr__(self) -> str:
        return (
            f"BoardReadDto(id={repr(self.id)}, "
            f"subject={repr(self.subject)}, "
            f"description={repr(self.description)}, "
            f"create_date={repr(self.create_date)}, "
            f"posts={repr(self.posts)})"
        )

from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from database import Base


class Board(Base):
    __tablename__ = "board"

    id = Column(Integer, primary_key=True, autoincrement=True)
    subject = Column(String, nullable=False, unique=True)
    description = Column(Text)
    create_date = Column(
        DateTime(timezone=True), nullable=False, server_default=func.now()
    )

    def __repr__(self):
        return f"<Board {self.subject} created as {self.create_date}>"


class Post(Base):
    __tablename__ = "post"

    id = Column(Integer, primary_key=True, autoincrement=True)
    subject = Column(String, nullable=False)
    content = Column(Text, nullable=False)
    create_date = Column(
        DateTime(timezone=True), nullable=False, server_default=func.now()
    )
    board_id = Column(Integer, ForeignKey("board.id"))
    post = relationship(Board, backref="posts")

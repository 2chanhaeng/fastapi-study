from sqlalchemy import Column, String, Integer, Text, DateTime, ForeignKey, UUID
from sqlalchemy.orm import relationship
from database import Base
from models.board import Board


class Post(Base):
    __tablename__ = "post"

    id = Column(UUID, primary_key=True)
    subject = Column(String, nullable=False)
    content = Column(Text, nullable=False)
    create_date = Column(DateTime, nullable=False)
    board_id = Column(Integer, ForeignKey(Board.id))
    question = relationship(Board, backref="posts")

from sqlalchemy import Column, String, Text, DateTime, UUID
from database import Base


class Board(Base):
    __tablename__ = "board"

    id = Column(UUID, primary_key=True)
    subject = Column(String, nullable=False, unique=True)
    description = Column(Text)
    create_date = Column(DateTime, nullable=False)

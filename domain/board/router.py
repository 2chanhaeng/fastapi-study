from datetime import datetime
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from database import get_db
from models import Board
from schemas.board import BoardCreateDto, BoardReadDto

router = APIRouter(
    prefix="/board",
)


@router.get("/", response_model=list[str])
def reads(db: Session = Depends(get_db)):
    boards = db.query(Board).order_by(Board.subject.asc()).all()
    return [board.subject for board in boards]


@router.get("/{board_subject}", response_model=BoardReadDto)
def read(subject: str, db: Session = Depends(get_db)):
    board = db.query(Board).filter(Board.subject == subject).first()
    if board is None:
        raise HTTPException(status_code=404, detail="Board not found")
    return board


@router.post("/")
def create(board: BoardCreateDto, db: Session = Depends(get_db)):
    try:
        subject = board.subject
        if db.query(Board).filter(Board.subject == subject).first():
            raise HTTPException(status_code=400, detail="Board already exists")
        b = Board(
            subject=subject,
            description=board.description,
            create_date=datetime.now(),
        )
        db.add(b)
        db.commit()
        return {"message": True}
    except Exception as e:
        print(e)
        raise HTTPException(status_code=400)

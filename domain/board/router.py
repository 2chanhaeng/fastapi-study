from fastapi import APIRouter, HTTPException
from database import SessionLocal
from models import Board

router = APIRouter(
    prefix="/board",
)


@router.get("/")
def reads():
    db = SessionLocal()
    boards = db.query(Board).order_by(Board.create_date.desc()).all()
    db.close()
    return boards


@router.get("/{board_subject}")
def read(board_subject: str):
    with SessionLocal() as db:
        board = db.query(Board).filter(Board.subject == board_subject).first()
        if board is None:
            raise HTTPException(status_code=404, detail="Board not found")
        return board


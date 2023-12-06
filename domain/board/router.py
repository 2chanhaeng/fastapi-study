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


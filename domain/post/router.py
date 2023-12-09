from datetime import datetime

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import get_db
from dto.board import BoardReadDto
from dto.post import PostCreatedDto, PostCreateDto, PostReadDto
from models import Board, Post
from utils.post import specify_post

router = APIRouter(
    prefix="/{subject}",
)


@router.post("", response_model=PostCreatedDto)
def create_post(subject: str, post: PostCreateDto, db: Session = Depends(get_db)):
    board = db.query(Board).filter(Board.subject == subject).first()
    if board is None:
        raise HTTPException(status_code=404, detail="Board not found")
    try:
        p = Post(
            subject=post.subject,
            content=post.content,
            board_id=board.id,
            create_date=datetime.now(),
        )
        db.add(p)
        db.commit()
        return p
    except Exception as e:
        print(e)
        raise HTTPException(status_code=400)


@router.get("/{post_id}", response_model=PostReadDto)
def read_post(subject: str, post_id: int, db: Session = Depends(get_db)):
    post = specify_post(subject, post_id, db)
    return post


@router.delete("/{post_id}", response_model=PostCreatedDto)
def delete_post(subject: str, post_id: int, db: Session = Depends(get_db)):
    post = specify_post(subject, post_id, db)
    db.delete(post)
    db.commit()
    return {"id": post.id}


@router.get("", response_model=BoardReadDto)
def read_board(subject: str, db: Session = Depends(get_db)):
    board = db.query(Board).filter(Board.subject == subject).first()
    if board is None:
        raise HTTPException(status_code=404, detail="Board not found")
    return board

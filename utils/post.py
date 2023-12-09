from fastapi import HTTPException
from sqlalchemy.orm import Session

from models import Board, Post


def specify_post(subject: str, post_id: int, db: Session):
    post = db.get(Post, post_id)
    if post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    board = db.get(Board, post.board_id)
    if board is None or board.subject != subject:  # type: ignore
        raise HTTPException(status_code=404, detail="Post not found")
    return post

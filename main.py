from enum import Enum

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from domain.board.router import router as board_router

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class LoonaSubUnit(str, Enum):
    third = "third"
    oec = "oec"
    yyxy = "yyxy"


@app.get("/items/{item_id}")
async def read_item(item_id: LoonaSubUnit):
    match item_id:
        case LoonaSubUnit.third:
            return {"item_id": item_id, "subunit": "LOONA 1/3"}
        case LoonaSubUnit.oec:
            return {"item_id": item_id, "subunit": "LOONA Odd Eye Circle"}
        case LoonaSubUnit.yyxy:
            return {"item_id": item_id, "subunit": "LOONA yyxy"}
        case _:
            return {"item_id": item_id, "subunit": "LOONA"}


@app.get("/query")
async def read_query(
    string: str = "default", integer: int = 0, optional: str | None = None
):
    return {"string": string, "integer": integer, "optional": optional}


app.include_router(board_router)

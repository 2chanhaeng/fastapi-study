from enum import Enum
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


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

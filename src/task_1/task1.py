from src.task_1.Dictionary import *
from fastapi import APIRouter

router = APIRouter()
d = Dictionary()
@router.post("/newentry")
async def task1(
        key: str|None = None,
        value: str|None = None
):
    if key and value:
        d.newentry(key.strip().lower(), value)
        return {"message":f"Added {key} -> {value} to dictionary"}
    return {"message":"no key or value provided"}

@router.get("/look")
async def lookup(key:str):
    return {"message":f"{d.look(key.strip().lower()) or f'No entry for {key.strip()}'}"}
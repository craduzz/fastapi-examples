from fastapi import FastAPI, routing
from src.task_1 import task1
from src.task_2 import task2
from src.task_3 import task3

app = FastAPI()

app.include_router(task1.router,prefix='/task1')
app.include_router(task2.router,prefix='/task2')
app.include_router(task3.router,prefix='/task3')
@app.get("/")
async def root():
    return {"Available endpoints": {
        "/health": "Health check",
        "/task1": ["GET /task1/look, Gets the data stored from a key", "POST /task1/newentry, Adds a new entry to the dictionary"],
        "/task2": ["GET, /task2, Gets the total price of the items and taxes (must pass the items and taxes as query parameters, costs in the body)"],
        "/task3": ["GET, /task3, Joins the letters of the words in the query parameter"]
    }}

@app.get("/health")
async def health():
    return {"status": "ok",
            "message": "EPAM tasks"}


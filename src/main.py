from fastapi import FastAPI, routing

app = FastAPI()

@app.get("/health")
async def health():
    return {"status": "ok",
            "message": "EPAM tasks"}
#app.add_route()
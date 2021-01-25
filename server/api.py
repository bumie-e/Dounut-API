from fastapi import FastAPI
from server.routes import router as DonutRouter

app = FastAPI()

@app.get("/", tags=["Root"])
async def read_root() -> dict:
    return {"message": "Get your doughnuts"}

app.include_router(DonutRouter, prefix="/doughnuts")
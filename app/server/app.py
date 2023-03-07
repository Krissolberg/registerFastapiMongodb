from fastapi import FastAPI

from app.server.routes.guest import router as GuestRouter

app = FastAPI()

app.include_router(GuestRouter, tags=["Guest"], prefix="/guest")


@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to this fantastic app!"}
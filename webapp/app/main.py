from fastapi import FastAPI
from app.routers import game, user

app = FastAPI(title="GraphRace API")

app.include_router(game.router, prefix="/game")
app.include_router(user.router, prefix="/user")

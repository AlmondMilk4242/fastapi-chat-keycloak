# main.py
from fastapi import FastAPI
from app import config
from app.models.chat import Base as Thread, Message, create_tables
from app.database import database, engine
from app.routers.routes import router as routes_router
from app.routers.chat import router as chat_router

app = FastAPI()

@app.on_event("startup")
async def startup():
    await database.connect()
    create_tables(engine)

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

app.include_router(routes_router)
app.include_router(chat_router)

# main.py
from fastapi import FastAPI
from app import config
from app.models import Base, create_tables
from app.database import database, engine
from app.routes import router

app = FastAPI()

@app.on_event("startup")
async def startup():
    await database.connect()
    create_tables(engine)

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

app.include_router(router)
# app/routes.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.auth.security import get_current_user
from app.database import SessionLocal
import uuid

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/token_content", tags=["token"])
async def get_token_content(current_user=Depends(get_current_user)):
    return {"token_content": current_user}
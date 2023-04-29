# app/routes.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.models.kanban_box import get_all_kanban_boxes, get_user_kanban_boxes
from app.security import get_current_user
from app.database import SessionLocal
import uuid

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/kanban_boxes", tags=["kanban_boxes"])
async def get_kanban_box_titles(current_user=Depends(get_current_user), db: Session = Depends(get_db)):
    kanban_boxes = get_all_kanban_boxes(db)
    return {"titles": [box.title for box in kanban_boxes]}

@router.get("/token_content", tags=["token"])
async def get_token_content(current_user=Depends(get_current_user)):
    return {"token_content": current_user}

@router.get("/kanban_boxes/user", tags=["kanban_boxes"])
async def get_user_kanban_box_titles(current_user=Depends(get_current_user), db: Session = Depends(get_db)):
    user_id = uuid.UUID(current_user["sub"])
    kanban_boxes = get_user_kanban_boxes(db, user_id)
    return {"titles": [box.title for box in kanban_boxes]}

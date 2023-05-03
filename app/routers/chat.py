# app/routers/chat.py
from app.database import SessionLocal
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException
from typing import List
from uuid import UUID
from ..auth.auth import authenticate_user
from ..models.chat import Thread, Message
from ..schemas.chat import ThreadCreate, ThreadOut, MessageCreate, Message
from ..service.chat.chat import create_thread, get_threads, delete_thread, create_message, get_messages


# Add other necessary imports, e.g. for your database session management

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Thread endpoints
@router.post("/threads", response_model=ThreadOut)
async def create_thread_endpoint(thread: ThreadCreate, token: dict = Depends(authenticate_user), db: Session = Depends(get_db)):
    user_id1 = token["sub"]
    new_thread = create_thread(db, thread, user_id1)
    return ThreadOut.from_model(new_thread)

@router.get("/threads", response_model=List[ThreadOut])
async def get_threads_endpoint(token: dict = Depends(authenticate_user), db: Session = Depends(get_db)):
    user_id = token["sub"]
    threads = await get_threads(db, user_id)
    return [ThreadOut.from_model(thread) for thread in threads]

@router.delete("/threads/{thread_id}")
async def delete_thread_endpoint(thread_id: UUID, token: dict = Depends(authenticate_user), db: Session = Depends(get_db)):
    user_id = token["sub"]
    deleted = delete_thread(db, thread_id, user_id)
    if deleted:
        return {"detail": "Thread deleted successfully"}
    raise HTTPException(status_code=403, detail="Unauthorized to delete thread")

@router.post("/messages", response_model=Message)
async def send_message(message: MessageCreate, token: dict = Depends(authenticate_user), db: Session = Depends(get_db)):
    sender_id = token["sub"]
    new_message = create_message(db, message, sender_id)
    return Message.from_model(new_message)

@router.get("/messages/{thread_id}", response_model=List[Message])
async def get_messages_endpoint(thread_id: UUID, token: dict = Depends(authenticate_user), db: Session = Depends(get_db)):
    user_id = token["sub"]
    messages = get_messages(db, thread_id, user_id)
    if messages is not None:
        return [Message.from_model(message) for message in messages]
    raise HTTPException(status_code=403, detail="Unauthorized to view messages in thread")

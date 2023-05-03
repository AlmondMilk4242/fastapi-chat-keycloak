# app/service/chat.py
from sqlalchemy.orm import Session
from app.models.chat import Thread, Message
from app.schemas.chat import ThreadCreate, Thread, MessageCreate, Message
from datetime import datetime


def create_thread(db: Session, chat: ThreadCreate, created_by: str):
    thread_in_db = Thread(
        user_id1=created_by,
        user_id2=chat.user_id2
    )
    db.add(thread_in_db)
    db.commit()
    db.refresh(thread_in_db)
    return thread_in_db
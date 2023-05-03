# app/service/chat.py
from sqlalchemy.orm import Session
from app.models.chat import Thread as ThreadModel, Message as MessageModel
from app.schemas.chat import ThreadCreate, ThreadOut, MessageCreate, Message
from datetime import datetime
from uuid import UUID

def create_thread(db: Session, thread: ThreadCreate, user_id1: str):
    thread_in_db = ThreadModel(user_id1=user_id1, user_id2=thread.user_id2)
    db.add(thread_in_db)
    db.commit()
    db.refresh(thread_in_db)
    return thread_in_db


async def get_threads(db: Session, user_id: str):
    threads = db.query(ThreadModel).filter((ThreadModel.user_id1 == user_id) | (ThreadModel.user_id2 == user_id)).all()
    return threads

def delete_thread(db: Session, thread_id: UUID, user_id: str):
    thread = db.query(ThreadModel).filter(ThreadModel.id == thread_id).first()
    if thread and (thread.user_id1 == user_id or thread.user_id2 == user_id):
        db.delete(thread)
        db.commit()
        return True
    return False

def create_message(db: Session, message: MessageCreate, sender_id: str):
    message_model = MessageModel(sender_id=sender_id, **message.dict())
    db.add(message_model)
    db.commit()
    db.refresh(message_model)
    return message_model


def get_messages(db: Session, thread_id: UUID, user_id: str):
    thread = db.query(ThreadModel).filter(ThreadModel.id == thread_id).first()
    if thread and (thread.user_id1 == user_id or thread.user_id2 == user_id):
        messages = db.query(MessageModel).filter(MessageModel.thread_id == thread_id).order_by(MessageModel.timestamp).all()
        return messages
    return None


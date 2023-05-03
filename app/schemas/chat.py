# app/achemas/schemas.py
from pydantic import BaseModel, UUID4
from typing import List
from uuid import uuid4
from uuid import UUID
from datetime import datetime
from ..models.chat import Message as MessageModel

class ThreadOut(BaseModel):
    id: UUID4
    user_id1: str
    user_id2: str

    @classmethod
    def from_model(cls, thread_model):
        return cls(id=thread_model.id, user_id1=thread_model.user_id1, user_id2=thread_model.user_id2)

class ThreadCreate(BaseModel):
    user_id2: str

class Thread(ThreadCreate):
    id: UUID4 = uuid4()

class MessageCreate(BaseModel):
    thread_id: UUID4
    content: str

class Message(BaseModel):
    id: UUID
    thread_id: UUID
    content: str
    sender_id: str
    timestamp: datetime

    class Config:
        orm_mode = True

    @classmethod
    def from_model(cls, model: MessageModel) -> "Message":
        return cls(
            id=model.id,
            thread_id=model.thread_id,
            content=model.content,
            sender_id=model.sender_id,
            timestamp=model.timestamp,
        )
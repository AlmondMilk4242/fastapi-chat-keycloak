# app/achemas/schemas.py
from pydantic import BaseModel, UUID4
from typing import List
from uuid import uuid4

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

class Message(MessageCreate):
    id: UUID4 = uuid4()

    @classmethod
    def from_model(cls, message_model):
        return cls(
            id=message_model.id,
            thread_id=message_model.thread_id,
            content=message_model.content,
        )



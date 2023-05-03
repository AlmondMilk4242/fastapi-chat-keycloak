# app/achemas/schemas.py
from pydantic import BaseModel, UUID4
from typing import List
from uuid import uuid4

class ThreadCreate(BaseModel):
    user_id2: str

class Thread(ThreadCreate):
    id: UUID4 = uuid4()

class MessageCreate(BaseModel):
    thread_id: UUID4
    sender_id: str
    content: str
    timestamp: str

class Message(MessageCreate):
    id: UUID4 = uuid4()


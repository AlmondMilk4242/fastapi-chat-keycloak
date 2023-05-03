# app/routers/chat.py
from app.database import SessionLocal
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends
from typing import List
from uuid import UUID
from ..auth.auth import authenticate_user
from ..models.chat import Thread, Message
from ..schemas.chat import ThreadCreate, Thread, MessageCreate, Message
from ..service.chat.chat import create_thread



# Add other necessary imports, e.g. for your database session management

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Thread endpoints
@router.post("/threads", response_model=Thread)
async def create_thread(thread: ThreadCreate, token: dict = Depends(authenticate_user), db: Session = Depends(get_db)):
    # Get the authenticated user's Keycloak ID from the token
    user_id1 = token["sub"]

    # Create a new thread with the authenticated user's Keycloak ID and the other user's ID
    new_thread = Thread(user_id1=user_id1, user_id2=thread.user_id2)

    # Add logic to save the new thread to your database
    # new_thread = create_thread(db, thread, user_id1)

    return new_thread

@router.get("/threads", response_model=List[Thread])
async def get_threads(token: dict = Depends(authenticate_user)):
    # Add logic to retrieve threads for the authenticated user based on their Keycloak ID
    pass

@router.delete("/threads/{thread_id}")
async def delete_thread(thread_id: UUID, token: dict = Depends(authenticate_user)):
    # Add logic to delete a thread if the authenticated user is one of the participants (based on their Keycloak ID)
    pass

# Message endpoints
@router.post("/messages", response_model=Message)
async def send_message(message: Message, token: dict = Depends(authenticate_user)):
    # Add logic to create a new message using the authenticated user's Keycloak ID
    pass

@router.get("/messages/{thread_id}", response_model=List[Message])
async def get_messages(thread_id: UUID, token: dict = Depends(authenticate_user)):
    # Add logic to retrieve messages for the authenticated user based on their Keycloak ID
    pass

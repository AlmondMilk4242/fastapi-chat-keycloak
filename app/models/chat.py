# app/models/chat.py
from sqlalchemy import Column, String, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func
import uuid

Base = declarative_base()

class Thread(Base):
    __tablename__ = "threads"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id1 = Column(String, nullable=False)  # Keycloak user ID
    user_id2 = Column(String, nullable=False)  # Keycloak user ID

class Message(Base):
    __tablename__ = "messages"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    thread_id = Column(UUID(as_uuid=True), nullable=False)
    sender_id = Column(String, nullable=False)  # Keycloak user ID
    content = Column(String, nullable=False)
    timestamp = Column(DateTime, default=func.now())

def create_tables(engine):
    Base.metadata.create_all(bind=engine)
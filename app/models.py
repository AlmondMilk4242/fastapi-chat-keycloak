# app/models.py
from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session
import uuid


# Add this function to app/models.py
def get_all_kanban_boxes(db: Session):
    return db.query(KanbanBox).all()

def get_user_kanban_boxes(db: Session, user_id: uuid.UUID):
    return db.query(KanbanBox).filter(KanbanBox.user_id == user_id).all()

Base = declarative_base()

class KanbanBox(Base):
    __tablename__ = "kanban_box"

    id = Column(Integer, primary_key=True)
    user_id = Column(UUID(as_uuid=True), nullable=False, default=uuid.uuid4, unique=True)
    title = Column(String(100), nullable=False)
    description = Column(Text)
    status = Column(String(50), nullable=False)

def create_tables(engine):
    Base.metadata.create_all(bind=engine)
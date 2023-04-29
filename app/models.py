# app/models.py
from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session

# Add this function to app/models.py
def get_all_kanban_boxes(db: Session):
    return db.query(KanbanBox).all()

Base = declarative_base()

class KanbanBox(Base):
    __tablename__ = "kanban_box"

    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    description = Column(Text)
    status = Column(String(50), nullable=False)

def create_tables(engine):
    Base.metadata.create_all(bind=engine)
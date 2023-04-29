# app/database.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from databases import Database
from app import config

database = Database(config.DATABASE_URL)
engine = create_engine(config.DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

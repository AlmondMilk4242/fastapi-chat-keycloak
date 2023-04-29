# main.py
from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from pydantic import BaseModel
import requests
from databases import Database
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from app import config
from app.models import Base, create_tables
import logging
# main.py
import json
from typing import Dict, Any
from fastapi import APIRouter
from app.models import get_all_kanban_boxes
from fastapi import Depends, Header
from sqlalchemy.orm import Session
from jose.constants import ALGORITHMS

def validate_jwt(token: str):
    try:
        payload = jwt.decode(
            token,
            get_keycloak_public_key(),
            algorithms=[ALGORITHMS.RS256],
            options={"verify_signature": True, "verify_aud": False}
        )
        return payload
    except JWTError as e:
        raise HTTPException(status_code=401, detail=str(e))

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_current_user(token: str = Header(None), db: Session = Depends(get_db)):
    if not token:
        raise HTTPException(status_code=401, detail="No token provided")

    jwt_payload = validate_jwt(token)
    return jwt_payload


def get_keycloak_public_key() -> Dict[str, Any]:
    jwks_response = requests.get(KEYCLOAK_JWKS_URL)
    jwks = jwks_response.json()
    return json.loads(jwks["keys"][0]["x5c"][0])


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


app = FastAPI()  # Add this line to create the FastAPI instance

# Database setup
database = Database(config.DATABASE_URL)
engine = create_engine(config.DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Keycloak setup
KEYCLOAK_JWKS_URL = config.KEYCLOAK_JWKS_URL

# Your existing code

Base = declarative_base()

@app.on_event("startup")
async def startup():
    await database.connect()

    # Create the kanban_box table if it doesn't exist
    print("Base.metadata: ", Base.metadata)
    print("Tables: ", Base.metadata.tables)
    create_tables(engine)  # Use the function from app.models

    # Check if the table is created
    table_names = engine.table_names()
    print("Table names: ", table_names)

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

router = APIRouter()

@router.get("/kanban_boxes", tags=["kanban_boxes"])
async def get_kanban_box_titles(current_user=Depends(get_current_user), db: Session = Depends(get_db)):
    kanban_boxes = get_all_kanban_boxes(db)
    return {"titles": [box.title for box in kanban_boxes]}

app.include_router(router)
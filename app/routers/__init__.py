from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.service.org_service import create_organization
from app.schemas.organization_schema import OrganizationCreate
from app.security import get_current_user
from app.database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/organizations", tags=["organizations"])
async def create_new_organization(
    organization: OrganizationCreate,
    current_user=Depends(get_current_user),
    db: Session = Depends(get_db)
):
    user_id = current_user["sub"]
    organization_in_db = create_organization(db, organization, user_id)
    return organization_in_db

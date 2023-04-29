# app/routers/organization.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.service.org_service import create_organization
from app.schemas.organization_schema import OrganizationCreate
from app.security import get_current_user
from app.database import SessionLocal
from app.service import org_service
from app.service.org_service import get_user_organizations, create_organization_member
from app.schemas.organization_schema import OrganizationMemberCreate

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
    organization_in_db = org_service.create_organization(db, organization, user_id)
    return organization_in_db

@router.get("/organizations/user", tags=["organizations"])
async def get_user_organizations_endpoint(current_user=Depends(get_current_user), db: Session = Depends(get_db)):
    user_id = current_user["sub"]
    organizations = get_user_organizations(db, user_id)
    return {"organizations": [ {key: value for key, value in organization.__dict__.items() if key != '_sa_instance_state'} for organization in organizations ]}

@router.post("/organization_members", tags=["organization_members"])
async def create_organization_member_endpoint(
    organization_member: OrganizationMemberCreate,
    current_user=Depends(get_current_user),
    db: Session = Depends(get_db)
):
    user_id = current_user["sub"]
    new_member = create_organization_member(db, organization_member, user_id)
    return {"member": new_member}


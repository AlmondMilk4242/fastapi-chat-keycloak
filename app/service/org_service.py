# app/service/organization_service.py
from sqlalchemy.orm import Session
from app.models.organization import Organization, OrganizationMember, OrganizationNotification
from datetime import datetime
from app.schemas.organization_schema import OrganizationCreate, OrganizationMemberCreate

def get_all_organizations(db: Session):
    return db.query(Organization).all()

def create_organization(db: Session, organization: OrganizationCreate, created_by: str):
    organization_in_db = Organization(
        organization_name=organization.organization_name,
        created_by=created_by,
        created_at=datetime.utcnow()
    )
    db.add(organization_in_db)
    db.commit()
    db.refresh(organization_in_db)
    return organization_in_db

def get_all_organization_members(db: Session, organization_id: int):
    return db.query(OrganizationMember).filter(OrganizationMember.organization_id == organization_id).all()

def add_organization_member(db: Session, member: OrganizationMember):
    db.add(member)
    db.commit()
    db.refresh(member)
    return member

def get_all_organization_notifications(db: Session, organization_member_id: int):
    return db.query(OrganizationNotification).filter(OrganizationNotification.organization_member_id == organization_member_id).all()

def create_organization_notification(db: Session, notification: OrganizationNotification):
    db.add(notification)
    db.commit()
    db.refresh(notification)
    return notification

def get_user_organizations(db: Session, user_id: str):
    return db.query(Organization).filter(Organization.created_by == user_id).all()

def create_organization_member(db: Session, member: OrganizationMemberCreate, added_by: str):
    member_in_db = OrganizationMember(
        organization_id=member.organization_id,
        member_name=member.member_name,
        added_by=added_by,
        created_at=datetime.utcnow()
    )
    db.add(member_in_db)
    db.commit()
    db.refresh(member_in_db)
    return member_in_db

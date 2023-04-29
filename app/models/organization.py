from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
import datetime

Base = declarative_base()

# Organization model
class Organization(Base):
    __tablename__ = "organization"

    id = Column(Integer, primary_key=True)
    organization_name = Column(String, nullable=False)
    created_by = Column(String, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.datetime.utcnow)

    members = relationship("OrganizationMember", back_populates="organization")


# OrganizationMember model
class OrganizationMember(Base):
    __tablename__ = "organization_member"

    id = Column(Integer, primary_key=True)
    organization_id = Column(Integer, ForeignKey("organization.id"), nullable=False)
    member_name = Column(String, nullable=False)
    added_by = Column(String, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.datetime.utcnow)

    organization = relationship("Organization", back_populates="members")
    notifications = relationship("OrganizationNotification", back_populates="member")


# OrganizationNotification model
class OrganizationNotification(Base):
    __tablename__ = "organization_notification"

    id = Column(Integer, primary_key=True)
    organization_member_id = Column(Integer, ForeignKey("organization_member.id"), nullable=False)
    read = Column(Boolean, default=False)
    created_at = Column(DateTime, nullable=False, default=datetime.datetime.utcnow)

    member = relationship("OrganizationMember", back_populates="notifications")


def create_tables(engine):
    Base.metadata.create_all(bind=engine)

from pydantic import BaseModel

class OrganizationCreate(BaseModel):
    organization_name: str

class OrganizationMemberCreate(BaseModel):
    organization_id: int
    member_name: str

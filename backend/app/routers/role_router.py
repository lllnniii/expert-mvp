from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.services.role_service import RoleService
from app.schemas.role import RoleResponse, RoleCreate

router = APIRouter(
    prefix="/api/roles",
    tags=["roles"]
)

@router.get("", response_model=List[RoleResponse], status_code=status.HTTP_200_OK)
def get_roles(db: Session = Depends(get_db)):
    service = RoleService(db)
    return service.get_all_roles()

@router.get("/{role_name}", response_model=RoleResponse, status_code=status.HTTP_200_OK)
def get_role_by_name(role_name: str, db: Session = Depends(get_db)):
    service = RoleService(db)
    return service.get_by_name(role_name)

@router.post("", response_model=RoleResponse, status_code=status.HTTP_201_CREATED)
def create_role(role: RoleCreate, db: Session = Depends(get_db)):
    service = RoleService(db)
    return service.create_role(role)

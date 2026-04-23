from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from typing import List
from backend.app.models.roles import Roles
from backend.app.repositories.role_repository import RoleRepository
from backend.app.schemas.role import RoleCreate, RoleResponse
from fastapi import HTTPException, status

class RoleService:
    def __init__(self, db : Session):
        self.repository = RoleRepository(db)

    def get_all_roles(self) -> List[RoleResponse]:
        roles = self.repository.get_all()
        return [RoleResponse.model_validate(r) for r in roles]

    def get_by_name(self, name: str) -> RoleResponse:
        role = self.repository.get_by_name(name)
        if not role:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Role '{name}' not found")
        return RoleResponse.model_validate(role)

    def create_role(self, data: RoleCreate) -> RoleResponse:
        existing = self.repository.get_by_name(data.name)
        if existing:
            raise HTTPException(status_code=400,
                detail="This role already exists")
        try:
            role = self.repository.create_role(data)
            return RoleResponse.model_validate(role)
        except IntegrityError:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                detail="Role with this data already exists or violates constraints"
            )
        except HTTPException  as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"An unexpected error occurred: {str(e)}"
            )
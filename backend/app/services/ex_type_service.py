from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from typing import List
from backend.app.models.expertise_types import ExpertiseTypes
from backend.app.repositories.ex_type_repository import ExpertiseTypeRepository
from backend.app.schemas.expertise_type import ExpertiseTypeResponse, ExpertiseTypeCreate
from fastapi import HTTPException, status

class ExpertiseTypeService:
    def __init__(self, db : Session):
        self.repository = ExpertiseTypeRepository(db)

    def get_all_types(self) -> List[ExpertiseTypeResponse]:
        types = self.repository.get_all()
        return [ExpertiseTypeResponse.model_validate(t) for t in types]

    def get_by_name(self, name: str) -> ExpertiseTypeResponse:
        type = self.repository.get_by_name(name)
        if not type:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Type '{name}' not found")
        return ExpertiseTypeResponse.model_validate(type)

    def create_type(self, data: ExpertiseTypeCreate) -> ExpertiseTypeResponse:
        existing = self.repository.get_by_name(data.name)
        if existing:
            raise HTTPException(status_code=400,
                detail="This type already exists")
        try:
            type = self.repository.create_type(data)
            return ExpertiseTypeResponse.model_validate(type)
        except IntegrityError:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                detail="Type with this data already exists or violates constraints"
            )
        except HTTPException  as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"An unexpected error occurred: {str(e)}"
            )
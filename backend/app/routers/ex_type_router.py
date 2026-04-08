from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import List
from ..database import get_db
from ..services.ex_type_service import ExpertiseTypeService
from ..schemas.expertise_type import ExpertiseTypeResponse, ExpertiseTypeCreate

router = APIRouter(
    prefix="/api/expertise_type",
    tags=["expertise_type"],
)

@router.get("", response_model=List[ExpertiseTypeResponse], status_code=status.HTTP_200_OK)
def get_type(db: Session = Depends(get_db)):
    service = ExpertiseTypeService(db)
    return service.get_all_types()

@router.get("/{type_name}", response_model=ExpertiseTypeResponse, status_code=status.HTTP_200_OK)
def get_type_by_name(type_name: str, db: Session = Depends(get_db)):
    service = ExpertiseTypeService(db)
    return service.get_by_name(type_name)

@router.post("", response_model=ExpertiseTypeResponse, status_code=status.HTTP_201_CREATED)
def create_type(type: ExpertiseTypeCreate, db: Session = Depends(get_db)):
    service = ExpertiseTypeService(db)
    return service.create_type(type)


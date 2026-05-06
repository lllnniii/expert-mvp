from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.services.object_service import ObjectService
from app.schemas.object import ObjectResponse, ObjectUpdate, ObjectCreate

router = APIRouter(
    prefix="/api/objects",
    tags=["objects"]
)

@router.get("", response_model=List[ObjectResponse], status_code=status.HTTP_200_OK)
def get_objects(db: Session = Depends(get_db)):
    service = ObjectService(db)
    return service.get_all_objects()

@router.get("/{object_id}", response_model=ObjectResponse, status_code=status.HTTP_200_OK)
def get_object_by_id(object_id: int, db: Session = Depends(get_db)):
    service = ObjectService(db)
    return service.get_object_by_id(object_id)

@router.get("/by-name/{name}", response_model= ObjectResponse, status_code=status.HTTP_200_OK)
def get_object_by_name(name: str, db: Session = Depends(get_db)):
    service = ObjectService(db)
    return service.get_object_by_name(name)

@router.get("/by-client/{client_id}", response_model= List[ObjectResponse], status_code=status.HTTP_200_OK)
def get_object_by_client_id(client_id: int, db: Session = Depends(get_db)):
    service = ObjectService(db)
    return service.get_objects_by_client(client_id)

@router.get("/by-category/{category}", response_model= List[ObjectResponse], status_code=status.HTTP_200_OK)
def get_object_by_category_id(category: str, db: Session = Depends(get_db)):
    service = ObjectService(db)
    return service.get_objects_by_category(category)

@router.post("", response_model=ObjectResponse, status_code=status.HTTP_201_CREATED)
def create_object(data : ObjectCreate,db: Session = Depends(get_db)):
    service = ObjectService(db)
    return service.create_object(data)

@router.patch("/{object_id}", response_model=ObjectResponse, status_code=status.HTTP_200_OK)
def update_object_by_id(object_id: int, data: ObjectUpdate, db: Session = Depends(get_db)):
    service = ObjectService(db)
    return service.update_object(object_id, data)

@router.delete("/{object_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_object_by_id(object_id: int, db: Session = Depends(get_db)):
    service = ObjectService(db)
    return service.delete_object(object_id)
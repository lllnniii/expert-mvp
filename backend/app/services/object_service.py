from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from typing import List, Optional
from ..repositories.object_repository import ObjectRepository
from ..repositories.client_repositories import ClientRepository
from ..schemas.object import ObjectResponse, ObjectCreate, ObjectUpdate, ObjectListResponses
from fastapi import HTTPException,status

class ObjectService:
    def __init__(self, db: Session):
        self.object_repository = ObjectRepository(db)
        self.client_repository = ClientRepository(db)

    def get_all_objects(self) -> List[ObjectResponse]:
        objects = self.object_repository.get_all()
        object_response = [ObjectResponse.model_validate(obj) for obj in objects]
        return object_response

    def get_object_by_id(self, object_id: int ) -> ObjectResponse:
        db_object = self.object_repository.get_by_object_id(object_id)
        if not db_object:
            raise HTTPException(status_code=404,
                                detail=f"Object with {object_id} was not found")
        return ObjectResponse.model_validate(db_object)

    def get_objects_by_client(self, client_id: int) -> List[ObjectResponse]:
        objects = self.object_repository.get_by_client_id(client_id)
        object_responses = [ObjectResponse.model_validate(obj) for obj in objects]
        return object_responses

    def get_object_by_name(self, object_name: str) -> ObjectResponse:
        db_object = self.object_repository.get_by_object_name(object_name)
        if not db_object:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Объект с именем '{object_name}' не найден")
        return ObjectResponse.model_validate(db_object)

    def get_objects_by_category(self, category: str) -> List[ObjectResponse]:
        objects = self.object_repository.get_by_opos_category(category)
        object_responses = [ObjectResponse.model_validate(obj) for obj in objects]
        return object_responses

    def create_object(self, object_data: ObjectCreate) -> ObjectResponse:
        client = self.client_repository.get_by_client_id(object_data.client_id)
        if not client:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Client with id {object_data.client_id} does not exist")

        existing = self.object_repository.get_by_object_name(object_data.object_name)
        if existing:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Object with name '{object_data.object_name}' already exists")
        try:
            db_object = self.object_repository.create_object(object_data)
            return ObjectResponse.model_validate(db_object)
        except IntegrityError:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                detail="Database integrity violation")
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Error creating object: {str(e)}")

    def update_object(self, object_id: int, object_data: ObjectUpdate) -> ObjectResponse:
        updated_object = self.object_repository.update_object(object_id, object_data)
        if not updated_object:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Object with id {object_id} not found")
        return ObjectResponse.model_validate(updated_object)

    def delete_object(self, object_id: int) -> None:
        success = self.object_repository.delete_object(object_id)
        if not success:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Object with id {object_id} not found")
        return None

from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from typing import List
from backend.app.models.clients import Clients
from backend.app.repositories.client_repositories import ClientRepository
from backend.app.schemas.client import ClientResponse, ClientCreate, ClientUpdate
from fastapi import HTTPException, status

class ClientService:
    def __init__(self, db : Session):
        self.repository = ClientRepository(db)

    def get_all_clients(self) -> List[ClientResponse]:
        clients = self.repository.get_all()
        return [ClientResponse.model_validate(cl) for cl in clients]

    def get_client_by_id(self, client_id: int ) -> ClientResponse:
        client = self.repository.get_by_client_id(client_id)
        if not client:
            raise HTTPException(status_code=404,
                                detail=f"Client with {client_id} was not found")
        return ClientResponse.model_validate(client)

    def get_client_by_name(self, client_name: str) -> ClientResponse:
        client = self.repository.get_by_client_name(client_name)
        if not client:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Client with name '{client_name}' not found")
        return ClientResponse.model_validate(client)

    def create_client(self, client_data: ClientCreate) -> ClientResponse:
        existing = self.repository.get_by_client_name(client_data.client_name)
        if existing:
            raise HTTPException(status_code=400,
                detail="Client name already taken")
        try:
            client = self.repository.create_client(client_data)
            return ClientResponse.model_validate(client)
        except IntegrityError:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                detail="Client with this data already exists or violates constraints"
            )
        except HTTPException as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"An unexpected error occurred: {str(e)}"
            )

    def update_client(self, client_id: int, client_data: ClientUpdate) -> ClientResponse:
        updated_client = self.repository.update_client(client_id, client_data)
        if not updated_client:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Client with id {client_id} not found")
        return ClientResponse.model_validate(updated_client)

    def delete_client(self, client_id: int) -> None:
        success = self.repository.delete_client(client_id)
        if not success:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Client with id {client_id} not found")
        return None
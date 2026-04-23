from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import List
from backend.app.database import get_db
from backend.app.services.client_service import ClientService
from backend.app.schemas.client import ClientResponse, ClientUpdate, ClientCreate

router = APIRouter(
    prefix="/api/clients",
    tags=["clients"]
)

@router.get("", response_model=List[ClientResponse], status_code=status.HTTP_200_OK)
def get_clients(db: Session = Depends(get_db)):
    service = ClientService(db)
    return service.get_all_clients()

@router.get("/{client_id}", response_model=ClientResponse, status_code=status.HTTP_200_OK)
def get_client_by_id(client_id: int, db: Session = Depends(get_db)):
    service = ClientService(db)
    return service.get_client_by_id(client_id)

@router.get("/by-name/{name}", response_model= ClientResponse, status_code=status.HTTP_200_OK)
def get_client_by_name(name: str, db: Session = Depends(get_db)):
    service = ClientService(db)
    return service.get_client_by_name(name)

@router.post("", response_model=ClientResponse, status_code=status.HTTP_201_CREATED)
def create_client(data : ClientCreate,db: Session = Depends(get_db)):
    service = ClientService(db)
    return service.create_client(data)

@router.patch("/{client_id}", response_model=ClientResponse, status_code=status.HTTP_200_OK)
def update_client_by_id(client_id: int, data: ClientUpdate, db: Session = Depends(get_db)):
    service = ClientService(db)
    return service.update_client(client_id, data)

@router.delete("/{client_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_client_by_id(client_id: int, db: Session = Depends(get_db)):
    service = ClientService(db)
    return service.delete_client(client_id)
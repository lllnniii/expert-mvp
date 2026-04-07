from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import List
from ..database import get_db
from ..services.client_service import ClientService
from ..schemas.client import ClientResponse

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
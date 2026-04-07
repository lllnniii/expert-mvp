from sqlalchemy.orm import Session
from sqlalchemy import func, select
from typing import List, Optional
from ..models.clients import Clients
from ..schemas.client import ClientCreate, ClientUpdate

class ClientRepository():
    def __init__(self, db: Session):
        self.db = db

    def get_all(self) -> List[Clients]:
        result = self.db.execute(select(Clients))
        return list(result.scalars().all())

    def get_by_client_id(self, client_id: int) -> Optional[Clients]:
        slct = select(Clients).where(Clients.client_id == client_id)
        result = self.db.execute(slct)
        return result.scalars().first()

    def get_by_client_name(self, client_name: str) -> Optional[Clients]:
        slct = select(Clients).where(
            func.lower(Clients.client_name) == client_name.lower())
        result = self.db.execute(slct)
        return result.scalars().first()

    def create_client(self, client_data : ClientCreate) -> Clients:
        db_client = Clients(**client_data.model_dump())
        self.db.add(db_client)
        try:
            self.db.commit()
            self.db.refresh(db_client)
            return db_client
        except Exception:
            self.db.rollback()
            raise

    def update_client(self, client_id: int, client_data: ClientUpdate) -> Optional[Clients]:
        db_client = self.get_by_client_id(client_id)
        if not db_client:
            return None
        update_data = client_data.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_client, key, value)
        try:
            self.db.commit()
            self.db.refresh(db_client)
            return db_client
        except Exception:
            self.db.rollback()
            raise

    def delete_client(self, client_id: int):
        db_client = self.get_by_client_id(client_id)
        if not db_client:
            return False
        try:
            self.db.delete(db_client)
            self.db.commit()
            return True
        except Exception:
            self.db.rollback()
            raise
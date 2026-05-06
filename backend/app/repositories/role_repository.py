from sqlalchemy.orm import Session
from sqlalchemy import func, select
from typing import List, Optional
from app.models.roles import Roles
from app.schemas.role import RoleCreate

class RoleRepository():
    def __init__(self, db: Session):
        self.db = db

    def get_all(self) -> List[Roles]:
        result = self.db.execute(select(Roles))
        return list(result.scalars().all())

    def get_by_name(self, name: str) -> Optional[Roles]:
        slct = select(Roles).where(
            func.lower(Roles.name) == name.lower())
        result = self.db.execute(slct)
        return result.scalars().first()

    def create_role(self, data : RoleCreate) -> Roles:
        db_role = Roles(**data.model_dump())
        self.db.add(db_role)
        self.db.commit()
        self.db.refresh(db_role)
        return db_role
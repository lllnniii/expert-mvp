from sqlalchemy.orm import Session
from sqlalchemy import func, select
from typing import List, Optional
from app.models.expertise_types import ExpertiseTypes
from app.schemas.expertise_type import ExpertiseTypeCreate, ExpertiseTypeUpdate

class ExpertiseTypeRepository():
    def __init__(self, db: Session):
        self.db = db

    def get_all(self) -> List[ExpertiseTypes]:
        result = self.db.execute(select(ExpertiseTypes))
        return list(result.scalars().all())

    def get_by_name(self, name: str) -> Optional[ExpertiseTypes]:
        slct = select(ExpertiseTypes).where(
            func.lower(ExpertiseTypes.name) == name.lower())
        result = self.db.execute(slct)
        return result.scalars().first()

    def create_type(self, data : ExpertiseTypeCreate) -> ExpertiseTypes:
        db_role = ExpertiseTypes(**data.model_dump())
        self.db.add(db_role)
        self.db.commit()
        self.db.refresh(db_role)
        return db_role

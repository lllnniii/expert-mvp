from sqlalchemy.orm import Session, joinedload
from sqlalchemy import func, select
from typing import List, Optional
from ..models.objects import Objects
from ..schemas.object import ObjectCreate, ObjectUpdate

class ObjectRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_all(self) -> List[Objects]:
        stmt = (select(Objects).options(joinedload(Objects.client)))
        result = self.db.execute(stmt)
        return list(result.scalars().all())

    def get_by_object_id(self, object_id: int) -> Optional[Objects]:
        slct = ((select(Objects).
                where(Objects.object_id == object_id)).
                options(joinedload(Objects.client)))
        result = self.db.execute(slct)
        return result.scalars().first()

    def get_by_client_id(self, client_id: int) -> List[Objects]:
        slct = (select(Objects).where(Objects.client_id == client_id))
        result = self.db.execute(slct)
        return list(result.scalars().all())

    def get_by_object_name(self, object_name: str) -> Optional[Objects]:
        slct = (select(Objects).
                where(func.lower(Objects.object_name) == object_name.lower()).
                options(joinedload(Objects.client)))
        result = self.db.execute(slct)
        return result.scalars().first()

    def get_by_opos_category(self, opos_category: str) -> List[Objects]:
        slct = select(Objects).where(
            func.lower(Objects.opos_category) == opos_category.lower()
        )
        result = self.db.execute(slct)
        return list(result.scalars().all())

    def create_object(self, object_data : ObjectCreate) -> Objects:
        db_object = Objects(**object_data.model_dump())
        self.db.add(db_object)
        self.db.commit()
        self.db.refresh(db_object)
        return db_object

    def update_object(self, object_id: int, object_data: ObjectUpdate) -> Optional[Objects]:
        db_object = self.get_by_object_id(object_id)
        if not db_object:
            return None
        update_data = object_data.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_object, key, value)
        self.db.commit()
        self.db.refresh(db_object)
        return db_object

    def delete_object(self, object_id: int):
        db_object = self.get_by_object_id(object_id)
        if not db_object:
            return False
        try:
            self.db.delete(db_object)
            self.db.commit()
            return True
        except Exception:
            self.db.rollback()
            raise

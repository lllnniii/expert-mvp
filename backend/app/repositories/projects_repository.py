from sqlalchemy.orm import Session, joinedload
from sqlalchemy import func, select
from typing import List, Optional
from app.models.projects import Projects
from app.schemas.project import ProjectCreate, ProjectUpdate

class ProjectRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_all(self) -> List[Projects]:
        stmt = (select(Projects).options(joinedload(Projects.objects),
                                         joinedload(Projects.employees),
                                         joinedload(Projects.expertise_types)))
        result = self.db.execute(stmt)
        return list(result.scalars().all())

    def get_by_project_id(self, project_id: int) -> Optional[Projects]:
        slct = ((select(Projects).
                where(Projects.project_id == project_id)).
                options(joinedload(Projects.objects),
                        joinedload(Projects.employees),
                        joinedload(Projects.expertise_types)))
        result = self.db.execute(slct)
        return result.scalars().first()

    def get_by_object(self, object_id: int) -> List[Projects]:
        slct = (select(Projects).where(Projects.object_id == object_id).
                options(joinedload(Projects.objects),
                        joinedload(Projects.employees),
                        joinedload(Projects.expertise_types)))
        result = self.db.execute(slct)
        return list(result.scalars().all())

    def get_by_exp_type(self, expertise_type_id: int) -> List[Projects]:
        slct = (select(Projects).where(Projects.expertise_type_id == expertise_type_id).
                options(joinedload(Projects.objects),
                        joinedload(Projects.employees),
                        joinedload(Projects.expertise_types)))
        result = self.db.execute(slct)
        return list(result.scalars().all())

    def get_by_project_name(self, project_name: str) -> Optional[Projects]:
        slct = (select(Projects).
                where(func.lower(Projects.name) == project_name.lower()).
                options(joinedload(Projects.objects),
                        joinedload(Projects.employees),
                        joinedload(Projects.expertise_types)))
        result = self.db.execute(slct)
        return result.scalars().first()

    def create_project(self, project_data : ProjectCreate) -> Projects:
        db_project = Projects(**project_data.model_dump())
        self.db.add(db_project)
        self.db.commit()
        self.db.refresh(db_project)
        return self.get_by_project_id(db_project.project_id)

    def update_project(self, project_id: int, project_data: ProjectUpdate) -> Optional[Projects]:
        db_project = self.get_by_project_id(project_id)
        if not db_project:
            return None
        update_data = project_data.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_project, key, value)
        self.db.commit()
        self.db.refresh(db_project)
        return db_project

    def delete_project(self, project_id: int):
        db_project = self.get_by_project_id(project_id)
        if not db_project:
            return False
        try:
            self.db.delete(db_project)
            self.db.commit()
            return True
        except Exception:
            self.db.rollback()
            raise
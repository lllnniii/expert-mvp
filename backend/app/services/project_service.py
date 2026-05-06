from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from typing import List, Optional
from app.repositories.projects_repository import ProjectRepository
from app.repositories.object_repository import ObjectRepository
from app.repositories.employee_repository import EmployeeRepository
from app.repositories.ex_type_repository import ExpertiseTypeRepository
from app.schemas.project import ProjectResponse, ProjectCreate, ProjectUpdate
from fastapi import HTTPException,status

class ProjectService:
    def __init__(self, db: Session):
        self.repo = ProjectRepository(db)
        self.employee_repository = EmployeeRepository(db)
        self.expertise_type_repository = ExpertiseTypeRepository(db)
        self.object_rep= ObjectRepository(db)

    def get_all(self) -> List[ProjectResponse]:
        projects = self.repo.get_all()
        project_response = [ProjectResponse.model_validate(pr) for pr in projects]
        return project_response

    def get_project_by_id(self, project_id: int ) -> ProjectResponse:
        db_project = self.repo.get_by_project_id(project_id)
        if not db_project:
            raise HTTPException(status_code=404,
                                detail=f"Project with {project_id} was not found")
        return ProjectResponse.model_validate(db_project)

    def get_proj_by_obj(self, object_id: int) -> List[ProjectResponse]:
        projects = self.repo.get_by_object(object_id)
        project_response = [ProjectResponse.model_validate(pr) for pr in projects]
        return project_response

    def get_proj_by_exp(self, expertise_id: int) -> List[ProjectResponse]:
        projects = self.repo.get_by_exp_type(expertise_id)
        project_response = [ProjectResponse.model_validate(pr) for pr in projects]
        return project_response

    def get_proj_by_name(self, project_name: str) -> ProjectResponse:
       db_proj = self.repo.get_by_project_name(project_name)
       if not db_proj:
           raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                               detail=f"Project with {project_name} was not found")
       return ProjectResponse.model_validate(db_proj)

    def create_project(self, project_data: ProjectCreate) -> ProjectResponse:
        obbject = self.object_rep.get_by_object_id(project_data.object_id)
        employee = self.employee_repository.get_by_employee_id(project_data.employee_id)
        expertise_type = self.expertise_type_repository.get_by_id(project_data.expertise_type_id)
        if not obbject:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Object with id {project_data.object_id} does not exist")
        if not employee:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Employee with id {project_data.employee_id} does not exist")
        if not expertise_type:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Expertise type with id {project_data.expertise_type_id} does not exist")

        existing = self.repo.get_by_project_name(project_data.name)
        if existing:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Project with name '{project_data.name}' already exists")
        try:
            db_projects = self.repo.create_project(project_data)
            return ProjectResponse.model_validate(db_projects)
        except IntegrityError:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                detail="Database integrity violation")
        except HTTPException  as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Error creating project: {str(e)}")

    def update_project(self, project_id: int, project_data: ProjectUpdate) -> ProjectResponse:
        updated_project = self.repo.update_project(project_id, project_data)
        if not updated_project:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                detail=f"project with id {project_id} not found")
        return ProjectResponse.model_validate(updated_project)

    def delete_project(self, project_id: int) -> None:
        success = self.repo.delete_project(project_id)
        if not success:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                detail=f"project with id {project_id} not found")
        return None

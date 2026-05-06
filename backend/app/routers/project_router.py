from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.services.project_service import ProjectService
from app.schemas.project import ProjectResponse, ProjectCreate, ProjectUpdate

router = APIRouter(
    prefix="/api/projects",
    tags=["projects"]
)

@router.get("", response_model=List[ProjectResponse], status_code=status.HTTP_200_OK)
def get_projects(db: Session = Depends(get_db)):
    service = ProjectService(db)
    return service.get_all()

@router.get("/{project_id}", response_model=ProjectResponse, status_code=status.HTTP_200_OK)
def get_project_by_id(project_id: int, db: Session = Depends(get_db)):
    service = ProjectService(db)
    return service.get_project_by_id(project_id)

@router.get("/by-name/{name}", response_model= ProjectResponse, status_code=status.HTTP_200_OK)
def get_project_by_name(name: str, db: Session = Depends(get_db)):
    service = ProjectService(db)
    return service.get_proj_by_name(name)

@router.get("/by-object/{object_id}", response_model= List[ProjectResponse], status_code=status.HTTP_200_OK)
def get_project_by_object_id(object_id: int, db: Session = Depends(get_db)):
    service = ProjectService(db)
    return service.get_proj_by_obj(object_id)

@router.get("/by-expertise-type/{expertise_id}", response_model= List[ProjectResponse], status_code=status.HTTP_200_OK)
def get_project_by_expertise_id(expertise_id: int, db: Session = Depends(get_db)):
    service = ProjectService(db)
    return service.get_proj_by_exp(expertise_id)

@router.post("", response_model=ProjectResponse, status_code=status.HTTP_201_CREATED)
def create_project(data : ProjectCreate,db: Session = Depends(get_db)):
    service = ProjectService(db)
    return service.create_project(data)

@router.patch("/{project_id}", response_model=ProjectResponse, status_code=status.HTTP_200_OK)
def update_project_by_id(project_id: int, data: ProjectUpdate, db: Session = Depends(get_db)):
    service = ProjectService(db)
    return service.update_project(project_id, data)

@router.delete("/{project_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_project_by_id(project_id: int, db: Session = Depends(get_db)):
    service = ProjectService(db)
    return service.delete_project(project_id)
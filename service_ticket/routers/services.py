from fastapi import APIRouter, Depends, status, HTTPException
from .. import schemas, database, models
from typing import List
from sqlalchemy.orm import Session
from . import oauth2

router = APIRouter(
    prefix="/service",
    tags=['services']
)

get_db = database.get_db

@router.get("/", status_code= status.HTTP_200_OK, response_model= List[schemas.ShowService])
def all(db: Session= Depends(get_db), current_user: schemas.User= Depends(oauth2.get_current_user)):
    services = db.query(models.Service).all()
    return services

@router.post("/", status_code= status.HTTP_201_CREATED)
def create(request: schemas.Service, db: Session= Depends(get_db), current_user: schemas.User= Depends(oauth2.get_current_user)):
    new_service = models.Service(main_issue=request.main_issue, sub_issue=request.sub_issue, priority= request.priority, comment= request.comment, user_id= 1)
    # db.add(new_service)
    db.commit()
    db.refresh(new_service)
    return new_service

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def destroy(id, db: Session= Depends(get_db), current_user: schemas.User= Depends(oauth2.get_current_user)):
    service = db.query(models.Service).filter(models.Service.id == id)
    if not service.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f"Service with id {id} not found")
    service.delete(synchronize_session=False)
    db.commit()
    return {"detail": "Successfully deleted"}

@router.get("/{id}", status_code= status.HTTP_200_OK, response_model= schemas.ShowService)
def show(id: int, db: Session = Depends(get_db), current_user: schemas.User= Depends(oauth2.get_current_user)):
    service = db.query(models.Service).filter(models.Service.id == id).first()
    if not service:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail=f"Service with id {id} is not available")
    return service
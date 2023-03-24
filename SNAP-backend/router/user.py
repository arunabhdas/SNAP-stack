import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from typing import List
from fastapi import APIRouter, Depends, status, HTTPException, Response

import schemas, database, models
from sqlalchemy.orm import Session
from hashing import Hash

router = APIRouter(
    tags = ['Users']
)
###############################################################################
## User

@router.post('/user', response_model=schemas.ShowUser)
def create_user(request: schemas.User, db: Session = Depends(database.get_db)):
    new_user = models.User(name = request.name, email = request.email, password = Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.put('/user/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id, request: schemas.User, db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.id == id)
    if not user.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id {id} not found")
    user.update({'name': request.name, 'email': request.email, 'password': request.password})
    db.commit()
    return {'detail': f"User with id {id} was updated"}

@router.get('/users', response_model=List[schemas.ShowUser])
def get_users(db: Session = Depends(database.get_db)):
   users = db.query(models.User).all()
   return users

@router.get('/user/{id}', response_model=schemas.ShowUser)
def get_user(id:int, db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id {id} is not available")
    return user

###############################################################################

import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from typing import List
from fastapi import APIRouter, Depends, status, HTTPException, Response

import schemas, database, models
from sqlalchemy.orm import Session

router = APIRouter()

@router.post('/blogpost', status_code=status.HTTP_201_CREATED, tags=['posts'])
def create(request: schemas.Post, db: Session = Depends(database.get_db)):
    new_post = models.Post(title=request.title, body=request.body, author_id=request.author_id)
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post

@router.delete('/blogpost/{id}', status_code=200, tags=['posts'])
def destroy(id, db: Session = Depends(database.get_db)):
    post = db.query(models.Post).filter(models.Post.id == id)
    if not post.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id {id} not found")
    post.delete(synchronize_session=False)
    db.commit()
    return {'detail': f"Post with id {id} was deleted"}

@router.put('/blogpost/{id}', status_code=status.HTTP_202_ACCEPTED, tags=['posts'])
def update(id, request: schemas.Post, db: Session = Depends(database.get_db)):
    post = db.query(models.Post).filter(models.Post.id == id)
    if not post.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id {id} not found")
    post.update({'title': request.title, 'body': request.body})
    db.commit()
    return {'detail': f"Post with id {id} was updated"}

@router.get('/blogposts', response_model=List[schemas.ShowPost], tags=['posts'])
def get_posts(db: Session = Depends(database.get_db)):
   posts = db.query(models.Post).all()
   return posts

@router.get('/blogpost/{id}', status_code=200, response_model=schemas.ShowPost, tags=['posts'])
def read_post(id, response: Response, db: Session = Depends(database.get_db)):
    post = db.query(models.Post).filter(models.Post.id == id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id {id} is not available")
    return post

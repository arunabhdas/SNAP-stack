from fastapi import FastAPI, Depends, Response, status, HTTPException
from schemas import Post
from typing import List

import models, schemas
from database import SessionLocal, engine
from sqlalchemy.orm import Session
from hashing import Hash

models.Base.metadata.create_all(bind=engine)

###############################################################################
app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get('/')
def index():
    return 'hello'

###############################################################################
@app.post('/blogpost', status_code=status.HTTP_201_CREATED, tags=['posts'])
def create(request: schemas.Post, db: Session = Depends(get_db)):
    new_post = models.Post(title=request.title, body=request.body, author_id=request.author_id)
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post

@app.delete('/blogpost/{post_id}', status_code=200, tags=['posts'])
def destroy(post_id, db: Session = Depends(get_db)):
    post = db.query(models.Post).filter(models.Post.id == post_id)
    if not post.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id {post_id} not found")
    post.delete(synchronize_session=False)
    db.commit()
    return {'detail': f"Post with id {post_id} was deleted"}

@app.put('/blogpost/{id}', status_code=status.HTTP_202_ACCEPTED, tags=['posts'])
def update(id, request: schemas.Post, db: Session = Depends(get_db)):
    post = db.query(models.Post).filter(models.Post.id == id)
    if not post.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id {id} not found")
    post.update({'title': request.title, 'body': request.body})
    db.commit()
    return {'detail': f"Post with id {id} was updated"}

@app.get('/blogposts', response_model=List[schemas.ShowPost], tags=['posts'])
def get_posts(db: Session = Depends(get_db)):
   posts = db.query(models.Post).all()
   return posts

@app.get('/blogpost/{id}', status_code=200, response_model=schemas.ShowPost, tags=['posts'])
def read_post(id, response: Response, db: Session = Depends(get_db)):
    post = db.query(models.Post).filter(models.Post.id == id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id {id} is not available")
    return post

###############################################################################

@app.post('/user', response_model=schemas.ShowUser, tags=['users'])
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    new_user = models.User(name = request.name, email = request.email, password = Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@app.get('/users', response_model=List[schemas.ShowUser], tags=['users'])
def get_users(db: Session = Depends(get_db)):
   users = db.query(models.User).all()
   return users

@app.get('/user/{id}', response_model=schemas.ShowUser, tags=['users'])
def get_user(id:int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id {id} is not available")
    return user

###############################################################################



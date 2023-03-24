from typing import List
from pydantic import BaseModel

class BasePost(BaseModel):
    title: str
    body: str
    author_id: int

class Post(BasePost):
    class Config():
        orm_mode = True

class User(BaseModel):
    name: str
    email: str
    password: str

class User(BaseModel):
    name: str
    email: str
    password: str

class ShowUser(BaseModel):
    id: int
    name: str
    email: str
    posts: List[Post] = []
    class Config():
        orm_mode = True

class ShowPost(BaseModel):
    id: int
    title: str
    body: str
    author: ShowUser
    class Config():
        orm_mode = True

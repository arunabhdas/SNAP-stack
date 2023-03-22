from pydantic import BaseModel

class Post(BaseModel):
    title: str
    body: str

class User(BaseModel):
    name: str
    email: str
    password: str


class ShowPost(BaseModel):
    id: int
    title: str
    body: str
    class Config():
        orm_mode = True

class User(BaseModel):
    name: str
    email: str
    password: str

class ShowUser(BaseModel):
    id: int
    name: str
    email: str
    class Config():
        orm_mode = True

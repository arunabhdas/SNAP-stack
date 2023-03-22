from pydantic import BaseModel

class Post(BaseModel):
    title: str
    body: str

class User(BaseModel):
    name: str
    email: str
    password: str


class ShowPost(Post):
    title: str
    body: str
    class Config():
        orm_mode = True

from pydantic import BaseModel
from typing import List

# Article inside user display
class Article(BaseModel):
    title : str
    content : str
    published : bool

class UserBase(BaseModel):
    username: str
    email : str
    password: str


class UserDisplay(BaseModel):
    username: str
    email : str
    # items : List[Article] = []
    class Config():
        orm_mode = True

# User inside article display
class User(BaseModel):
    id : int
    username: str
    class Config():
        orm_mode = True

class ArticleBase(BaseModel):
    title : str
    content : str
    published : bool
    creator_id : int

class ArticleDisplay(BaseModel):
    title : str
    content : str
    published : bool
    user : User

    class Config():
        orm_mode = True
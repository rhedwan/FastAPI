from fastapi import FastAPI
from enum import Enum
from typing import Optional

app = FastAPI()

@app.get('/')
def index():
    return {"message":"Hello World"}

""" @app.get('/blog/all')
def get_all_blog():
    return "All blogs" """

# making query parameters
@app.get('/blog/all')
def get_all_blog(page = 1, page_size: Optional[int] = 2):
    return {
        "message":f"All {page_size} blogs on page {page}"
    }


# making query and path parameters
@app.get('/blog/{id}/comments/{comment_id}')
def get_comment_blog(id: int, comment_id: int, valid:bool= True, \
    username: Optional[str]=None):
    return {
        "message" : f"blog_id {id}, comment_id {comment_id}, valid {valid} username {username}"
    }

class BlogType(str, Enum):
    short = 'short'
    long = 'long'
    story = 'story'


@app.get('/blog/type/{type}')
def get_blog_type(type: BlogType):
    return {"message":f"The blog type is {type.value}"}

@app.get('/blog/{id}')
def get_blog(id:int):
    return {"message":f"Blog with an ID {id}"}


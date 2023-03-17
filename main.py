from fastapi import FastAPI, status, Response
from enum import Enum
from typing import Optional

app = FastAPI()

@app.get('/', tags=['blog'])
def index():
    return {"message":"Hello World"}

""" @app.get('/blog/all')
def get_all_blog():
    return "All blogs" """

# making query parameters
@app.get('/blog/all', tags=['blog'])
def get_all_blog(page = 1, page_size: Optional[int] = 2):
    return {
        "message":f"All {page_size} blogs on page {page}"
    }


# making query and path parameters
@app.get('/blog/{id}/comments/{comment_id}', tags=['blog', 'comment'])
def get_comment_blog(id: int, comment_id: int, valid:bool= True, \
    username: Optional[str]=None):
    return {
        "message" : f"blog_id {id}, comment_id {comment_id}, valid {valid} username {username}"
    }

class BlogType(str, Enum):
    short = 'short'
    long = 'long'
    story = 'story'


@app.get('/blog/type/{type}', tags=['blog'])
def get_blog_type(type: BlogType):
    return {"message":f"The blog type is {type.value}"}

@app.get('/blog/{id}', status_code=status.HTTP_200_OK, tags=['blog'])
def get_blog(id:int, response: Response):
    if id > 6:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {
            "message": f"Blog {id} not found"
        }
    return {"message":f"Blog with an ID {id}"}


from fastapi import APIRouter, status, Response
from enum import Enum
from typing import Optional

router = APIRouter(prefix='/blog', tags=['blog'])

""" @app.get('/blog/all')
def get_all_blog():
    return "All blogs" """

# making query parameters
@router.get('/all', summary="Retrieve all blogs",
description="This api call, stimulate get all blogs",
response_description="The list of available blogs")
def get_all_blog(page = 1, page_size: Optional[int] = 2):
    return {
        "message":f"All {page_size} blogs on page {page}"
    }


# making query and path parameters
@router.get('/{id}/comments/{comment_id}', tags=['comment'])
def get_comment_blog(id: int, comment_id: int, valid:bool= True, \
    username: Optional[str]=None):

    """
    Stimulate retrieve all comments
    """
    return {
        "message" : f"blog_id {id}, comment_id {comment_id}, valid {valid} username {username}"
    }

class BlogType(str, Enum):
    short = 'short'
    long = 'long'
    story = 'story'


@router.get('/type/{type}')
def get_blog_type(type: BlogType):
    return {"message":f"The blog type is {type.value}"}

@router.get('/{id}', status_code=status.HTTP_200_OK)
def get_blog(id:int, response: Response):
    if id > 6:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {
            "message": f"Blog {id} not found"
        }
    return {"message":f"Blog with an ID {id}"}


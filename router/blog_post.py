from fastapi import APIRouter, Query, Body
from pydantic import BaseModel
from typing import Optional , List

router = APIRouter(prefix='/blog', tags=['blog'])

class BlogModel(BaseModel):
    title: str
    content: str
    number_comment: int
    publish: Optional[bool]


@router.post('/new/{id}')
def create_blog(blog:BlogModel, id:int, version:int= 2):
    return {
        "id": id,
        "version": version,
        "data": blog
    }

@router.post('/new/{id}/comment')
def create_comment(blog:BlogModel,
 id=int, comment_id:int = Query(None,
 title="Id of the comment",
 description="Some random string",
 alias="commentId"),
 content:str =Body(..., min_length=10,
 regex="^[a-z\s]*$"),
 v:Optional[List[str]] = Query(None)):
    return{
        "data": blog,
        "id": id,
        "comment_id" : comment_id,
        "content": content,
        "version": v
    }






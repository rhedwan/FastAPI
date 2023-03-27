from fastapi import APIRouter, Depends
from schemas import ArticleBase, ArticleDisplay
from sqlalchemy.orm.session import Session
from db.database import get_db
from db import db_article
from typing import List


router = APIRouter(
    prefix="/article", tags=["article"]
)

@router.post("/")
def create_article(request: ArticleBase, db:Session = Depends(get_db)):
    return db_article.create_article(db, request)

@router.get("/{id}/article", response_model=ArticleDisplay)
def get_article(id: int, db:Session = Depends(get_db)):
    return db_article.get_article(db, id)
from fastapi import APIRouter , Depends
from schemas import UserBase, UserDisplay
from sqlalchemy.orm.session import Session
from db.database import get_db
from db import db_user
from typing import List

router = APIRouter(
    prefix="/user", tags=["user"]
)

# Create User
@router.post("/", response_model=UserDisplay)
def create_user(request: UserBase, db:Session = Depends(get_db)):
    return db_user.create_user(db, request)

# Read All Users
@router.get("/users", response_model=List[UserDisplay])
def create_user(db:Session = Depends(get_db)):
    return db_user.get_all_users(db)

# Read User
@router.get("/{id}", response_model=UserDisplay)
def create_user(id: int, db:Session = Depends(get_db)):
    return db_user.get_user(db, id)
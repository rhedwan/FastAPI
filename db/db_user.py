from sqlalchemy.orm.session import Session
from schemas import UserBase
from db.models import DBUser

def create_user(db:Session, request: UserBase):
    new_user = DBUser (
        username = request.username,
        email = request.email,
        password =
    )
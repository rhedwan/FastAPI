from fastapi.security import OAuth2PasswordBearer

oauth_schema = OAuth2PasswordBearer(
    tokenUrl="token"
)
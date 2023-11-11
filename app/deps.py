from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt
from pydantic import ValidationError
from model import TokenPayload, UserAuth
from singleton import db
from config import config

reuseable_oauth = OAuth2PasswordBearer(
    tokenUrl="/login",
    scheme_name="JWT"
)


async def get_current_user(token: str = Depends(reuseable_oauth)) -> UserAuth:
    try:
        payload = jwt.decode(
            token, config.JWT_SECRET_KEY, algorithms=[config.ALGORITHM]
        )
        token_data = TokenPayload(**payload)
    except (jwt.JWTError, ValidationError):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Could not validate credentials",
        )
    user = db.user_storage.get(token_data.sub)
    return user
    

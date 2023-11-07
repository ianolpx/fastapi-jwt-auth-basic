from typing import Union, Any
from datetime import datetime, timedelta
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from utils import (
    ALGORITHM,
    JWT_SECRET_KEY,
)
from jose import jwt
from pydantic import ValidationError
from model import TokenPayload, SystemUser
from singleton import db

reuseable_oauth = OAuth2PasswordBearer(
    tokenUrl="/login",
    scheme_name="JWT"
)


async def get_current_user(token: str = Depends(reuseable_oauth)):
    try:
        print('token', token)
        payload = jwt.decode(
            token, JWT_SECRET_KEY, algorithms=[ALGORITHM]
        )
        token_data = TokenPayload(**payload)
        print('token_data', token_data)

    except (jwt.JWTError, ValidationError):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Could not validate credentials",
        )
    print('sub', token_data.sub)
    # user = db.user_storage.get(token_data.sub)
    # user = db.user_storage[token_data.sub]
    return {'user': token_data.sub,
    'type': 'test',
    'loc': 'test',
    'msg': 'test'}
    # return SystemUser(**user)

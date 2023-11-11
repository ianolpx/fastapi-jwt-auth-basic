"""Main module for FastAPI app"""
from uuid import uuid4
from fastapi import FastAPI, status, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordRequestForm

import uvicorn
from model import UserOut, UserAuth, TokenSchema

from utils import (
  create_access_token,
  create_refresh_token,
  get_hashed_password,
  verify_password
)

from singleton import db
from deps import get_current_user

app = FastAPI(
  title="FastAPI - Auth example",
  description="FastAPI - Auth example using JWT",
  version="0.0.1"
)

# CORS
app.add_middleware(
  CORSMiddleware,
  allow_origins=["*"],
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"],
)


@app.get("/")
async def index():
    """
    Index route
    """
    return {"message": "Hello World"}


@app.post("/signup", summary="Create new user", response_model=UserOut)
async def create_user(data: UserAuth):
    """
    Create new user
    """
    user = db.user_storage.get(data.email)
    print(user)
    if user is not None:
        raise HTTPException(
            status_code=400,
            detail="Email already registered"
        )

    user = {
        'email': data.email,
        'password': get_hashed_password(data.password),
        'id': str(uuid4())
    }
    db.user_storage[data.email] = user
    return user


@app.post(
    "/login",
    summary="Create access and refresh tokens for user",
    response_model=TokenSchema)
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    """
    Create access and refresh tokens for user
    """
    user = db.user_storage.get(form_data.username)
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect email or password"
        )
    hashed_pass = user.get("password")
    if not verify_password(form_data.password, hashed_pass):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect email or password"
        )
    return {
        "access_token": create_access_token(form_data.username),
        "refresh_token": create_refresh_token(form_data.username)
    }


@app.get("/me", summary="Get current user", response_model=UserOut)
async def get_me(current_user: UserOut = Depends(get_current_user)):
    """
    Get current user
    """
    return {
        'id': uuid4(),
        'email': 'test'
    }

# Run app
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=3000, reload=True)

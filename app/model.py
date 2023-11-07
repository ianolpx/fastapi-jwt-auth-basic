"""
This file contains the schemas for the user model
"""
from uuid import UUID
from pydantic import BaseModel, Field


class User(BaseModel):
    """
    User schema
    """
    email: str
    age: int = None


class TokenSchema(BaseModel):
    """
    Token schema
    """
    access_token: str
    refresh_token: str


class TokenPayload(BaseModel):
    """
    Token payload schema
    """
    sub: str = None
    exp: int = None


class UserAuth(BaseModel):
    """
    User authentication schema
    """
    email: str = Field(..., description="user email")
    password: str = Field(
        ..., min_length=5, max_length=24, description="user password")


class UserOut(BaseModel):
    """
    User output schema
    """
    id: UUID
    email: str


class SystemUser(UserOut):
    """
    System user schema
    """
    password: str

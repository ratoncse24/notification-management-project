from typing import List
from pydantic import BaseModel


class UserBase(BaseModel):
    username: str


class UserCreate(UserBase):
    fullname: str
    password: str


class UserAuthenticate(UserBase):
    password: str


class User(UserBase):
    id: int

    class Config:
        orm_mode = True


class NotificationBase(BaseModel):
    notification_text: str


class NotificationInfo(NotificationBase):
    event: str


class Notification(NotificationInfo):
    id: int

    class Config:
        orm_mode = True


class Token(BaseModel):
    """
    - Token response schema
    """
    access_token: str
    refresh_token: str
    token_type: str


class AccessToken(BaseModel):
    """
    - Refresh access_token response schema
    """
    access_token: str



class RefreshToken(BaseModel):
    """
    - Refresh token input schema
    """
    refresh_token: str


class TokenData(BaseModel):
    username: str = None


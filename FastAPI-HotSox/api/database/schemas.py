from typing import List, Optional
from uuid import uuid4, UUID

from datetime import datetime, date
from pydantic import BaseModel, validator, Field


class SimplyTheUser(BaseModel):
    # id: int | None
    username: str | None
    # first_name: str | None
    # last_name: str | None
    email: str | None

    class Config:
        orm_mode = True


class SimplySock(BaseModel):
    # id: int | None
    info_name: str | None
    info_special: str | None

    class Config:
        orm_mode = True


################################################################
### Actual HotSox models                                      ##
################################################################


class MessageChat(BaseModel):
    # id: int | None
    other: SimplyTheUser | None = Field(..., alias="receiver")
    message: str | None
    sent_date: datetime | None
    seen_date: datetime | None

    class Config:
        orm_mode = True
        allow_population_by_field_name = True


class MessageMail(BaseModel):
    # id: int | None
    subject: str | None
    content: str | None
    sent_date: date | None

    class Config:
        orm_mode = True


class SockLikes(BaseModel):
    # id: int | None
    sock: SimplySock | None
    like: SimplySock | None
    dislike: SimplySock | None

    class Config:
        orm_mode = True


class SockProfilePicture(BaseModel):
    # id: int | None
    profile_picture: str | None
    # sock_id: str | None

    class Config:
        orm_mode = True


class ShowSock(BaseModel):
    id: int | None = Field(..., alias="id_sock")
    # user_id: int
    info_joining_date: date | None
    info_name: str | None
    info_about: str | None
    info_color: int | None
    info_fabric: int | None
    info_fabric_thickness: int | None
    info_brand: int | None
    info_type: int | None
    info_size: int | None
    info_age: int | None
    info_separation_date: date | None
    info_condition: str | None
    info_holes: str | None
    info_kilometers: str | None
    info_inoutdoor: str | None
    info_washed: str | None
    info_special: str | None
    profile_pictures: Optional[list[SockProfilePicture]]
    sock_likes: Optional[list[SockLikes]]

    class Config:
        orm_mode = True
        allow_population_by_field_name = True


class UserMatch(BaseModel):
    # id: int | None
    # user: Optional[SimplyTheUser]
    other: Optional[SimplyTheUser] = Field(..., alias="matched_with")
    unmatched: bool | None
    chatroom_uuid: UUID

    class Config:
        orm_mode = True
        allow_population_by_field_name = True


class UserProfilePicture(BaseModel):
    # id: int | None
    profile_picture: str | None
    # user_id: str | None

    class Config:
        orm_mode = True


# basic schema for user displaying
class ShowUser(BaseModel):
    id: int = Field(..., alias="id_user")
    username: str
    password: str
    first_name: str
    last_name: str
    email: str
    last_login: Optional[datetime]
    is_superuser: bool
    is_staff: bool
    is_active: bool
    date_joined: Optional[datetime]
    info_about: Optional[str]
    info_birthday: Optional[date]
    info_gender: Optional[int]
    location_city: Optional[str]
    location_latitude: Optional[float]
    location_longitude: Optional[float]
    notification: Optional[bool]
    social_instagram: Optional[str]
    social_facebook: Optional[str]
    social_twitter: Optional[str]
    social_spotify: Optional[str]
    profile_pictures: Optional[list[UserProfilePicture]]
    user_matches: Optional[list[UserMatch]]
    mail: Optional[list[MessageMail]]
    chat: Optional[list[MessageChat]]
    socks: Optional[list[ShowSock]]

    class Config:
        orm_mode = True
        allow_population_by_field_name = True


# basic schema for login
class Login(BaseModel):
    username: str
    password: str


# basic schema for JWT Token
class Token(BaseModel):
    access_token: str
    token_type: str


# basic schema for JWT Token
class TokenData(BaseModel):
    username: Optional[str] = None

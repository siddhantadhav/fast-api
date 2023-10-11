from pydantic import BaseModel
from typing import List

class Service(BaseModel):
    main_issue: str
    sub_issue: str
    priority: str
    comment: str

    class Config():
        orm_mode= True

class User(BaseModel):
    name: str
    email: str
    password: str

class ShowUser(BaseModel):
    name: str
    email: str
    services: List[Service]= []

    class Config():
        orm_mode= True

class ShowService(BaseModel):
    main_issue: str
    sub_issue: str
    priority: str
    creator: ShowUser
    class Config():
        orm_mode= True

class Login(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: str | None = None
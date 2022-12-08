from datetime import datetime

from typing import Optional

from pydantic import BaseModel,EmailStr

from pydantic.types import conint

class struc(BaseModel):
    name:str
    type:str
    reg:int
    sale:bool = True

class Creatpost(struc):
    pass   


class userRes(BaseModel):
    id:int
    email:EmailStr
    username:str
    created_at:datetime
    
    class Config:
        orm_mode = True

class Postres(BaseModel):
    id:int
    created_at:datetime
    name:str
    type:str
    owner_id:int
    owner_data:userRes

    class Config:
        orm_mode =True

class postout(BaseModel):
    Post:Postres
    votes:int


###to inherit data/fields from the main class struc  to avoid placing the data again
# class Postres(struc):
#     id:int
#     created_at:datetime
#     class Config:
#         orm_mode = True

class userCre(BaseModel):
    email:EmailStr
    username:str
    password:str


class UserLogin(BaseModel):
    email:EmailStr
    password:str

class Token(BaseModel):
    access_token:str
    token_type:str

class TokenData(BaseModel):
    id:Optional[str]=None
    
class Vote(BaseModel):
    post_id:int
    #to validate if the value is either of two values
    #for below dir is either 1 or less than 1
    dir:conint(le=1)




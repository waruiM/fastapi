from jose import JWTError,jwt
from datetime import datetime, timedelta
from fastapi import Depends, status, HTTPException
from fastapi.security import OAuth2PasswordBearer
from .config import settings

oauth2_schema =OAuth2PasswordBearer(tokenUrl="login")

from app.learn import schemas

#secret_key
#Algorithm
#experation time

SECRET_KEY = settings.secret_key
ALGORITHM = settings.algorithm
ACCESS_TOKEN_EXPIRE_MINUTES = settings.access_token_expire_minutes


##creating the access token
def create_access_token(data: dict):
    to_encode=data.copy()

    expire=datetime.utcnow()+timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

    to_encode.update({"exp":expire})

    encoded_jwt=jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)

    return encoded_jwt

def verify_access_token(token:str, credentials_exception):
    try:

        payload=jwt.decode(token,SECRET_KEY,algorithms=ALGORITHM)

        id:str=payload.get("user_id")
    #if id is not present
        if id is None:
            raise credentials_exception
        token_data =schemas.TokenData(id=id)
    except JWTError:
        raise credentials_exception

    return token_data


def get_current_user(token:str = Depends(oauth2_schema)):
    credentials_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="user credentails error",headers={"www.Authenticate":"Bearer"})

    return verify_access_token(token,credentials_exception)
    
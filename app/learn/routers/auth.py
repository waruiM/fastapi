from os import access
from fastapi import APIRouter, Depends,status, HTTPException,Response

from app.learn import models
from ..database import get_db
from sqlalchemy.orm import Session

from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from .. import schemas,utils,oath2

router= APIRouter(
    tags=["Authenticateion"]
)
@router.post("/login",status_code=status.HTTP_202_ACCEPTED,response_model=schemas.Token)

#def login(User_cred:schemas.UserLogin, db: Session=Depends(get_db) ):
#or 
#user login 
def login(User_cred:OAuth2PasswordRequestForm = Depends(),db :Session = Depends(get_db)):

    #user=db.query(models.user).filter(models.user.email==User_cred.email).first()
    user = db.query(models.user).filter(
        models.user.email == User_cred.username).first()
    
    #where data provided is wrong
    if not user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="User credentials provided are invalid")
    
    #password do not match
    if not utils.pass_ver(User_cred.password,user.password):
        raise HTTPException(
           status_code=status.HTTP_403_FORBIDDEN, detail="User credential not valid" 
        )
    #  create token
    # return token

#provide the different access endpoints for users
    access_token =oath2.create_access_token(data={"user_id":user.id})
    
    return {"access_token":access_token, "token_type":"bearer"}
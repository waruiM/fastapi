from .. import models,schemas, utils
from ..database import get_db
from sqlalchemy.orm import Session
from fastapi import status, Depends, HTTPException,APIRouter

router= APIRouter(
    prefix="/user",
    tags=['User']
)


### user
#1,creating user
@router.post('/',status_code=status.HTTP_201_CREATED,response_model=schemas.userRes)

def create_user(user: schemas.userCre, db:Session = Depends(get_db)):

# hash the password 

    hashed_password=utils.hash(user.password)
    user.password=hashed_password

    new_user = models.user(**user.dict())

    db.add(new_user)

    db.commit()
    db.refresh(new_user)

    return new_user
#2,getting user
@router.get('/{id}',status_code=status.HTTP_302_FOUND,response_model=schemas.userRes)
def spec_user(id:int,db:Session = Depends(get_db)):
    user=db.query(models.user).filter(models.user.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"user with id {id} does not exist")

    return user

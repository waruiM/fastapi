##password hashing
from passlib.context import CryptContext

##hashing algorithim to use
pwd_context =CryptContext(schemes=["bcrypt"],deprecated="auto")

def hash(password:str):
    return pwd_context.hash(password)

def pass_ver(plain_password,hashed_password):
    return pwd_context.verify(plain_password,hashed_password)
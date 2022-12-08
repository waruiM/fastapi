from enum import unique
from http import server
from wsgiref.simple_server import server_version
from sqlalchemy import Column,Integer,String, Boolean,ForeignKey
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text
from .database import Base
from sqlalchemy.orm import relationship


class Post(Base):
    __tablename__= "posts"

    id=Column(Integer,primary_key=True,nullable=False)

    name=Column(String,nullable=False)

    type=Column(String,nullable=False)

    reg=Column(Integer,nullable=False)
    
    sale=Column(Boolean, server_default='TRUE',nullable=False)

    created_at=Column(TIMESTAMP(timezone=True),nullable=False,server_default=text('now()'))

    owner_id=Column(Integer,ForeignKey("users.id",ondelete="CASCADE"),nullable=False)

    owner_data = relationship("users")


class user(Base):
    __tablename__ ='users'

    id= Column(Integer,nullable= False, primary_key=True)

    email =Column (String,nullable=False,unique= True)

    username= Column(String, nullable= False,unique =True)

    password = Column(String,nullable=False)

    created_at =Column(TIMESTAMP(timezone=True),nullable=False,server_default=text('now()'))

    phone_number=Column(Integer,nullable=False,unique= True)

class Votes(Base):
    __tablename__ = "Votes"
    post_id= Column(Integer,ForeignKey("posts.id",ondelete="CASCADE"),primary_key=True,nullable=False)

    user_id= Column(Integer,ForeignKey("users.id",ondelete="CASCADE"),primary_key=True,nullable=False)

# class list(Base):
#     __tablename__="wshlist"
#     wish_id=Column(Integer,primay_key=True,nullable=False)
#     post_id=Column(Integer,ForeignKey("post.id",ondelete="CASCADE"),primary_key=True,nullable=False)
#     user_id=Column(Integer,ForeignKey("users.id",ondelete="CASCADE"),primary_key=True,nullable=False)

   









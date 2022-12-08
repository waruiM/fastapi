from lib2to3.pytree import Base
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
###import psycopg2
###from psycopg2.extras import RealDictCursor
import time
from .config import settings



### connecting to database using sqlachamey

SQLALCHEMY_DATABASE_URL = f"postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}"

## old data
# SQLALCHEMY_DATABASE_URL = f"postgresql://postgres:mikeadmin@localhost:5432/fastapi(1)"
                           

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# getting a connection to database
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

####using psycopg2 driver to connect to our database



# while True:

# # connection to psycopg
#     try:
#         conn= psycopg2.connect(host='localhost',database='fastapi(1)', user='postgres',password='mikeadmin',
#         #provide column name with its value
#         cursor_factory= RealDictCursor)
        
#         # execute  sql statement
#         cursor=conn.cursor()

#         print('database connection succesful')
#         break

#     except Exception as error:
#         print('connecting to data base failed')
#         print('Error', error)
#         time.sleep(2)

# # ###
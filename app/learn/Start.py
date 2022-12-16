from fastapi import FastAPI
from . import  models
from .database import engine
from .routers import post,users,auth,vote
from .config import settings
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def main():
    return {"message": "Hello World"}


#print(settings.database_hostname)

###code to instract sqlalchemy to generte the tables on start up
##however a we have alembic it is not required
#models.Base.metadata.create_all(bind=engine)

#setting the domain
origins=['*']

app=FastAPI()

app.add_middleware(
    CORSMiddleware,

    allow_origins=[],
    allow_credentials=True,

    #setting the allowed methods to be run
    allow_methods=["*"],

    #setting the allowed http headers
    allow_headers=["*"],
)

# getting the data from the router file
app.include_router(post.router)
app.include_router(users.router)
app.include_router(auth.router)
app.include_router(vote.router)

@app.get("/")
def root():
    return{"message":"success"}
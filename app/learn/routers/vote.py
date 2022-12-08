from fastapi import Depends,HTTPException, status, APIRouter, Response, FastAPI
from .. import schemas,database,oath2,models
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/vote",
    tags=["vote"]
)
@router.post("/",status_code=status.HTTP_201_CREATED)
def vote(vote: schemas.Vote, db: Session=Depends(database.get_db), current_user:int = Depends(oath2.get_current_user)):

    post= db.query(models.Post).filter(models.Post.id == vote.post_id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id {vote.post_id} was not found")
            #check if the vote exists.
        #filter by vote(chech if vote exists)
        #secondcondition filter by user (check if the given user has already voted on the given post)
    vote_query=db.query(models.Votes).filter(models.Votes.post_id == vote.post_id,models.Votes.user_id == current_user.id)
    found_vote = vote_query.first()
    if (vote.dir ==1):
        if found_vote:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=f"You have already voted for this post{vote.post_id}")
        new_vote= models.Votes(post_id=vote.post_id,user_id=current_user.id)
        db.add(new_vote)
        db.commit()
        return{"message":"post has been liked"}
    else:
        #if the user returns 0 meaning they want to remove there like
        #if like does not exist
        #removing a like
        if not found_vote:
            raise HTTPException(status_code=status.HTTP_204_NO_CONTENT,detail=f"vote does not exist")

        vote_query.delete(synchronize_session=False)
        db.commit()
        return {"message": "like has been roled back for the post"}
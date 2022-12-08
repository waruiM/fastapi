from .. import schemas,models,utils,oath2
from ..database import get_db, engine
from sqlalchemy.orm import Session
from fastapi import FastAPI,status, Depends,APIRouter,HTTPException,Response
from typing import List, Optional
from sqlalchemy import func

router=APIRouter(
    prefix="/post",
    tags=['Posts']
)

#get all posts
#
@router.get("/",response_model = List [schemas.postout])
def st(db :Session=Depends(get_db),limit:int = 8,skip:int= 0, search: Optional[str]=""):

###getting only your posts
###def st(db :Session=Depends(get_db), current_user: int = Depends(oath2.get_current_user)):

    ##methode 1
    # cursor.execute("""Select * from yard""")
    # posts=cursor.fetchall()

    ##getting only your posts
    ##posts= db.query(models.Post).filter(models.Post.owner_id == current_user.id).all()
    

   

    ##join funcion in sqlalchemy
    ##creating the query to calculate the total number of votes a post gets
    
    result=db.query(models.Post, func.count(models.Votes.post_id).label("votes")).join(
        models.Votes,models.Votes.post_id == models.Post.id,isouter=True).group_by(models.Post.id).filter(
            models.Post.type.contains(search)).limit(limit).offset(skip).all()
    

    return result

  
#add a new post (post)
@router.post("/",status_code=status.HTTP_201_CREATED,response_model=schemas.Postres)
def st_pst(look:schemas.Creatpost,db: Session = Depends(get_db),user_id:int = Depends(oath2.get_current_user)):
    # ne_post=look.dict()
    # ne_post["id"]=randrange(3,1000)
    # data.append(ne_post)
    # print(ne_post)s
    ###method one
    # cursor.execute("""Insert into yard(name,type,reg,sale) values(%s,%s,%s,%s) returning *""",
    #               (look.Car_name,look.Car_type,look.Car_reg,look.Car_ins))
    # new_post=cursor.fetchone()
    #conn.commit()

    ###method  two
    print(user_id.id)
    
    new_post=models.Post(owner_id=user_id.id,**look.dict())


    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    
    return new_post



#get individual post
@router.get("/{id}",response_model=schemas.postout)
def gt_pst(id:int,db: Session = Depends(get_db),user_id:int = Depends(oath2.get_current_user)):

    ###
    # cursor.execute(""" select * from yard where id = %s """,(str(id)))
    # res=cursor.fetchone()
    res= db.query(models.Post, func.count(models.Votes.post_id).label("votes")).join(models.Votes,models.Votes.post_id==models.Post.id,isouter=True).group_by(models.Post.id).filter(models.Post.id == id).first()


    if res == None:
        raise HTTPException (status_code=status.HTTP_404_NOT_FOUND,detail=f"Post with id {id} does not exist")
    
    ###where posts are private
    # if res.owner_id != int(user_id.id):
    #     raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="You cannot view other peoples posts as yours are private")

    return res



#delete post
@router.delete('/{id}',status_code=status.HTTP_204_NO_CONTENT)
def del_pst(id:int,db: Session = Depends(get_db), consumer_id:int=Depends(oath2.get_current_user)):


    ###
    # cursor.execute("""DELETE FROM yard where id = %s returning * """, (str(id)))
    # delps=cursor.fetchone()
    # conn.commit()

    post_query=db.query(models.Post).filter(models.Post.id==id)
    post=post_query.first()

  
    if post == None:
        raise HTTPException (status_code=status.HTTP_404_NOT_FOUND,detail=f'post with id {id} doesnot exist')

    

    if post.owner_id != int(consumer_id.id):
        # print(type(post.owner_id,')(((((('))
        # print(type(consumer_id.id))
        # print(post.owner_id != consumer_id.id)
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="You do not have clearance to delete this post")
    else:
        post_query.delete(synchronize_session=False)
        db.commit()

        return Response(status_code=status.HTTP_204_NO_CONTENT)


# update post
@router.put('/{id}',response_model=schemas.Postres)

def upd_pst(id:int, des:schemas.Creatpost,db: Session = Depends(get_db),user_id:int=Depends(oath2.get_current_user)):

    # cursor.execute("""UPDATE yard SET name=%s ,type=%s,  reg=%s , sale=%s where id= %s returning *""",(yard.name,yard.type,yard.reg,yard.sale,(str(id))))
    # udps=cursor.fetchone()
    # conn.commit()

    udps_post=db.query(models.Post).filter(models.Post.id ==id)

    udps=udps_post.first()
    

    if udps == None:
        raise HTTPException (status_code=status.HTTP_404_NOT_FOUND,detail=f'post with id {id} doesnot exist')

    
    if udps.owner_id != int(user_id.id):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="You do not have clearance to update this post")
        

    udps_post.update(des.dict(),synchronize_session=False)

    db.commit()
    
    return udps_post.first()


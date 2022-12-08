from urllib import response
from fastapi import FastAPI,Response,status,HTTPException
from pydantic import BaseModel
from fastapi.params import Body
from random import randrange

tst=FastAPI()

#setting schema/validation
class req (BaseModel):
    title:str
    phone:int
    place:str
    tall:bool = True
    
my_post=[{"title":"GoodMorning","phone":123455984,"place":"outside","tall":True,"id":1},{"title":"it is day break","phone":109897898,"place":"home","tall":False,"id":2}]

# geting the id that matches to that post
def find_posts(id):
    for p in my_post:
        if p['id'] == id:
            return p

def fd_de(id):
    for i,x in enumerate(my_post):
        if x['id'] ==id:
            return i

#getting all posts
@tst.get('/')
def test():
    #statemnt printed in post man
    return{'message':my_post}

#creating a post
@tst.post('/data', status_code=status.HTTP_201_CREATED)
def prs(new_post:req):
    # print(new_post.title)
    # print(new_post.phone)
    print(new_post)
    print(new_post.dict())
    new_post1=new_post.dict()
    new_post1["id"]=randrange(0,1000)
    my_post.append(new_post1)

    return{'text':"Data added"}

# def inf(payload:dict=Body(...)):
#     print(payload)


####
@tst.get('/posts/latest')

def lat_post():
    ne_post=my_post[len(my_post)-1]

    return {'message':ne_post}


#get individual post
@tst.get("/posts/{id}")

def pst(id:int,response:Response):

    post=find_posts(id)
    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id {id} doesnot exist"
        )

    return{'post_detail':post}

#delete post
@tst.delete('/posts/{id}',status_code=status.HTTP_204_NO_CONTENT)
def del_po(id:int):
    inde = fd_de(id)
    if inde == None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Item with id: {id} doesn't exist"
        )

    my_post.pop(inde)

    return Response(status_code=status.HTTP_204_NO_CONTENT)


#update post
@tst.put('/posts/{id}')
def up_ps(id:int, post:req):

    # print(post)
    # return{'message':'Post updated'}

    inde = fd_de(id)

    if inde == None:

        raise HTTPException(

            status_code=status.HTTP_404_NOT_FOUND, detail=f"Item with id: {id} doesn't exist"
        )

    post_dict=post.dict()

    post_dict['id']=id

    my_post[inde]=post_dict

    print(my_post)
    

    return{'data': "Update succesful"}
    

    # for message in index:

    #     return{"message": index}
    

    # return{'data':post_dict}

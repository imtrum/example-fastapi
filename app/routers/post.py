from fastapi import FastAPI,Response, status,HTTPException, Depends, APIRouter
from typing import Optional,List
from .. import models, schemas
from sqlalchemy.orm import Session
from ..database import get_db  
from .. import oauth2
from sqlalchemy import func

router = APIRouter(
    prefix = "/posts", 
    tags = ['posts']
)



@router.get("/",response_model=List[schemas.PostOut])
def get_posts(db: Session = Depends(get_db),
            current_user: int  = Depends(oauth2.get_current_user), limit:int = 10, skip:int = 0, search:Optional[str]= ""):
    # cursor.execute("""SELECT * FROM """)
    #  = cursor.fetchall()
    
    posts = db.query(models.Post).filter(models.Post.title.contains(search)).limit(limit).offset(skip).all()
      
    result = db.query(models.Post, func.count(models.Post.id).label("votes")).join(
        models.Vote, models.Vote.post_id == models.Post.id, isouter = True).group_by(models.Post.id).filter(
            models.Post.title.contains(search)).limit(limit).offset(skip).all()
    
    return result

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.Post)
def create_posts(post: schemas.PostCreate, db: Session = Depends(get_db), current_user: int  = Depends(oauth2.get_current_user)):
    # cursor.execute("""INSERT INTO  (title, content,published) VALUES (%s, %s, %s) RETURNING *""",(post.title, post.content, post.published))
    # new_post = cursor.fetchone()
    # conn.commit()

    print(current_user)
    new_post = models.Post(**post.model_dump(),owner_id = current_user.id)

    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post

    
                   
@router.get("/{id}", response_model = schemas.Post)
def get_post(id: int, db: Session = Depends(get_db),current_user: int  = Depends(oauth2.get_current_user)):
    # cursor.execute("""SELECT * FROM  WHERE id = %s""",(str(id)))
    # post = cursor.fetchone()
    post = db.query(models.Post).filter(models.Post.id ==  id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id: {id} was not found")

    return post




@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_posts(id: int, db : Session = Depends(get_db),current_user: int  = Depends(oauth2.get_current_user)):
    # cursor.execute("""DELETE FROM  WHERE id = %s RETURNING *""",(str(id),))
    # deleted_post = cursor.fetchone()
    # conn.commit()
    post_query = db.query(models.Post).filter(models.Post.id == id)
    post = post_query.first()
    if  post== None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'post with id: {id} does not exists')
    if post.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail="Not authorized to perform that requested action")  
    post_query.delete(synchronize_session=False)
    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.put("/{id}",response_model = schemas.Post)
def update_post(id: int, post1: schemas.PostUpdate, db : Session = Depends(get_db),
                current_user: int  = Depends(oauth2.get_current_user)):

    # cursor.execute(
    #     """ UPDATE  SET title = %s, content = %s, published = %s WHERE id = %s RETURNING * """,
    #     (post.title, post.content, post.published, str(id)))
    # updated_post = cursor.fetchone()
    #conn.commit()

    post_query = db.query(models.Post).filter(models.Post.id == id)
    post = post_query.first()

    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f'post with id: {id} does not exists')
    
    if post.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail="Not authorized to perform that requested action")  
    
    post_query.update(post1.model_dump(), synchronize_session= False)
    db.commit()
    return post_query.first()
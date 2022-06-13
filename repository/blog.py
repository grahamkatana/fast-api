from db.database import get_db
from blog import Models, Schemas
from sqlalchemy.orm import Session
from fastapi import HTTPException, status
get_db = get_db()

def get_all(db: Session):
    blogs = db.query(Models.Blog).all()
    return blogs

def create_record(db: Session, request:Schemas.Blog):
    new_blog = Models.Blog(title=request.title, body=request.body, user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

def get_single_record(db: Session,id:int):
    blog = db.query(Models.Blog).filter(Models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Blog with id of {id} was not found")

    return blog

def destroy_record(db: Session, id:int):
    blog = db.query(Models.Blog).filter(Models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Blog with id of {id} was not found")
    else:
        blog.delete(synchronize_session=False)
        db.commit()
    return {'message': 'The blog was deleted'}

def update_record(db:Session, id:int,request:Schemas.Blog):
    blog = db.query(Models.Blog).filter(Models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Blog with id of {id} was not found")
    else:
        blog.update({'title': request.title, 'body': request.body})
        db.commit()
    return {'message': 'Updated'}

    

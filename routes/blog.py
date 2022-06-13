from fastapi import APIRouter
from typing import List
from fastapi import Depends,status
from blog import Schemas
from db.database import get_db
from blog.Schemas import User
from sqlalchemy.orm import Session
from repository.blog import get_all, create_record, get_single_record, destroy_record, update_record
from utils.oauth2 import get_current_user

router = APIRouter(
    prefix="/api/v1/blogs",
    tags=['Blogs']
)


@router.get('/', response_model=List[Schemas.ShowBlog])
def index(db: Session = Depends(get_db)):
    return get_all(db)


@router.post('/', status_code=status.HTTP_201_CREATED)
def create(request: Schemas.Blog, db: Session = Depends(get_db),current_user:User=Depends(get_current_user)):
    return create_record(db, request)


@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=Schemas.ShowBlog)
def show(id: int, db: Session = Depends(get_db),current_user:User=Depends(get_current_user)):
    return get_single_record(db, id)


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id, db: Session = Depends(get_db),current_user:User=Depends(get_current_user)):
    return destroy_record(db, id)


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id, request: Schemas.Blog, db: Session = Depends(get_db),current_user:User=Depends(get_current_user)):
    return update_record(db, id, request)

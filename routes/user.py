from fastapi import APIRouter
from fastapi import Depends, status
from blog import Schemas
from db.database import get_db
from sqlalchemy.orm import Session
from repository.user import create_new_user, get_single_user
from utils.oauth2 import get_current_user

router = APIRouter(
    prefix="/api/v1/users",
    tags=['Users']
)

@router.post('/', status_code=status.HTTP_201_CREATED, response_model=Schemas.ShowUser)
def create_user(request: Schemas.User, db: Session = Depends(get_db)):
    return create_new_user(db,request)
    


@router.get('/{id}', response_model=Schemas.ShowUser)
def get_user(id, db: Session = Depends(get_db),current_user:Schemas.User=Depends(get_current_user)):
    return get_single_user(db,id)
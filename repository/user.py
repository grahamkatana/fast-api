from fastapi import Depends,HTTPException, status
from blog import Schemas
from blog import Models
from db.database import get_db
from sqlalchemy.orm import Session
from utils.Hashing import Hashing
get_db = get_db()

def create_new_user(db: Session,request:Schemas.User):
    hashed_password = Hashing.hash_password(request.password)
    new_user = Models.User(
        name=request.name, email=request.email, password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def get_single_user(db: Session, id:int):
    user = db.query(Models.User).filter(Models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Blog with id of {id} was not found")
    return user

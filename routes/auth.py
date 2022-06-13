from fastapi import APIRouter,Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from blog import Models
from blog.Schemas import Login
from db.database import get_db
from sqlalchemy.orm import Session
from utils.Hashing import Hashing
from utils.token import create_access_token

router = APIRouter(
    prefix="/api/v1/login",
    tags=['Authentication']
)

@router.post('/')
def login(request:OAuth2PasswordRequestForm = Depends(), db:Session= Depends(get_db)):
    user = db.query(Models.User).filter(Models.User.email == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"User not found")
   
    if not Hashing.verify_password(request.password,user.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Invalid credentials given")

    #generate a jwt and return it
    # access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.email}
    )
    return {"access_token": access_token, "token_type": "bearer"}
    
    # return user
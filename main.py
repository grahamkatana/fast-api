from fastapi import FastAPI
from blog import Models
from db.database import engine, get_db
from routes import blog, user, auth

app = FastAPI()
Models.Base.metadata.create_all(engine)
app.include_router(auth.router)
app.include_router(blog.router)
app.include_router(user.router)

get_deb = get_db()

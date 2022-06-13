from fastapi import FastAPI,BackgroundTasks
from blog import Models
from db.database import engine, get_db
from routes import blog, user, auth
import os
from utils.emails import send_email_async


app = FastAPI()
Models.Base.metadata.create_all(engine)
app.include_router(auth.router)
app.include_router(blog.router)
app.include_router(user.router)

@app.get('/send-email/asynchronous')
async def send_email_asynchronous():
    await send_email_async('Greetings', 'graykatanakenny@gmail.com')
    return  'sent'


get_deb = get_db()

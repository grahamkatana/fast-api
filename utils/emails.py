from fastapi_mail import FastMail, MessageSchema, ConnectionConfig
from dotenv import load_dotenv
# load_dotenv('.env')
async def send_email_async(subject: str, email_to: str):
    conf = ConnectionConfig(
        MAIL_USERNAME="",
        MAIL_PASSWORD="",
        MAIL_FROM="",
        MAIL_PORT=465,
        MAIL_SERVER="y",
        MAIL_TLS=False,
        MAIL_SSL=True,
        USE_CREDENTIALS=True,
        VALIDATE_CERTS=True,
        TEMPLATE_FOLDER='./templates/emails'
    )

    message = MessageSchema(
        subject=subject,
        recipients=[email_to],
        body="Good morning",
        subtype='html',
    )

    fm = FastMail(conf)

    await fm.send_message(message, template_name='email.html')




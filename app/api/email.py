from fastapi import APIRouter, HTTPException
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig, MessageType
from pydantic import BaseModel, EmailStr
from typing import List, Dict, Any
from fastapi.responses import JSONResponse
from pathlib import Path
import os
from dotenv import load_dotenv

load_dotenv()

# class EmailSchema(BaseModel):
#     email: List[EmailStr]
#     body: Dict[str, Any]

conf = ConnectionConfig(
    MAIL_USERNAME=os.getenv("MAIL_USERNAME"),
    MAIL_PASSWORD=os.getenv("MAIL_PASSWORD"),
    MAIL_FROM=os.getenv("MAIL_FROM"),
    MAIL_PORT=587,
    MAIL_SERVER="smtp.gmail.com",
    MAIL_STARTTLS=True,
    MAIL_SSL_TLS=False,
    # USE_CREDENTIALS=True,
    VALIDATE_CERTS=False,
    TEMPLATE_FOLDER=Path(__file__).parent.parent / 'templates',
)

router = APIRouter()

@router.post("/send_invite")
async def send_invitation():
    recipients = os.getenv("RECIPIENT_EMAILS").split(",")  # Split the string into a list
    message = MessageSchema(
        subject="User Management API Documentation",
        recipients=recipients,
        template_body={"github_link": "https://github.com/aniketwdubey/FastAPI-Firestore-User-Management"},  # Add your GitHub link here
        subtype=MessageType.html,
        # attachments=[Path("/path/to/your/screenshot.png")],
    )
    fm = FastMail(conf)
    await fm.send_message(message, template_name="email_template.html")
    return JSONResponse(status_code=200, content={"message": "Email has been sent with the Firestore screenshot and GitHub link."})
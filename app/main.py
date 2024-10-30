from fastapi import FastAPI
from app.api import users
from app.api import email
# from app.utils.email import send_invite_email

app = FastAPI(title="User Management API")

# Include the user management router
app.include_router(users.router)
app.include_router(email.router)

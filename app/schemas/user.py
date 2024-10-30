from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    project_id: str

class UserResponse(UserCreate):
    user_id: str

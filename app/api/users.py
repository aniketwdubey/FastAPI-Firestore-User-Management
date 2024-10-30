from fastapi import APIRouter, HTTPException, BackgroundTasks
from app.schemas.user import UserCreate, UserResponse
from app.utils.firestore_crud import create_user, get_users, update_user, delete_user
# from app.utils.email import EmailSchema, send_invite_email

router = APIRouter()

@router.post("/add_users", response_model=UserResponse)
async def add_user(user: UserCreate):
    user_data = create_user(user)
    return user_data

@router.get("/get_users", response_model=list[UserResponse])
async def get_all_users():
    return get_users()

@router.patch("/update_users/{user_id}", response_model=UserResponse)
async def modify_user(user_id: str, user: UserCreate):
    updated_user = update_user(user_id, user)
    if not updated_user:
        raise HTTPException(status_code=404, detail="User not found")
    return updated_user

@router.delete("/delete_users/{user_id}")
async def remove_user(user_id: str):
    delete_user(user_id)
    return {"message": "User deleted successfully"}

# @router.post("/send_invite")
# async def send_invitation(background_tasks: BackgroundTasks):
#     email_data = EmailSchema(
#         email=["20010816@ycce.in"],
#         body={"first_name": "Fred", "last_name": "Fredsson"}
#     )
#     background_tasks.add_task(send_invite_email, email_data)
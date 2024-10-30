from pydantic import BaseModel, Field
from typing import Optional

class UserModel(BaseModel):
    id: Optional[str] = Field(None, alias="user_id")
    username: str
    email: str
    project_id: str

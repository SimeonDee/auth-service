from pydantic import BaseModel, EmailStr, ConfigDict
from typing import Optional
from app.core.user_roles import UserRoles


class BaseUser(BaseModel):
    email: EmailStr
    first_name: str
    middle_name: Optional[str] = ""
    last_name: str
    role: UserRoles = UserRoles.TEACHER
    is_active: bool = True


class UserCreate(BaseUser):
    password: str


class UserRead(BaseUser):
    # replaced orm_mode in Pydantic v2
    model_config = ConfigDict(from_attributes=True)
    id: int

    # deprecated in Pydantic v2
    # class Config:
    #     orm_mode = True


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"

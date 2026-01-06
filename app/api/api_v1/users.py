from fastapi import APIRouter, Depends
from app.schemas.user import UserRead
from app.deps import get_current_user
from typing import Annotated

router = APIRouter()


User_Dependency = Annotated[UserRead, Depends(get_current_user)]


@router.get("/me", response_model=UserRead)
async def read_own_user(current_user: User_Dependency):
    return current_user

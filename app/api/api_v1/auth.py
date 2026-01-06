from fastapi import APIRouter, Depends, HTTPException, status

from fastapi.security import OAuth2PasswordRequestForm
from app.deps import DB_Dendency
from app.schemas.user import UserCreate, UserRead, Token
from app.services.user_service import (
    create_user,
    authenticate_user,
    get_user_by_email,
)
from app.core.jwt import create_access_token

router = APIRouter()


@router.post("/register", response_model=UserRead)
async def register(user_in: UserCreate, db: DB_Dendency):
    existing = get_user_by_email(db, user_in.email)
    if existing:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered",
        )
    user = create_user(db, user_in)
    return user


@router.post("/token", response_model=Token)
async def login_for_access_token(
    db: DB_Dendency,
    form_data: OAuth2PasswordRequestForm = Depends(),
):
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect username or password",
        )
    access_token = create_access_token(str(user.id))
    return {"access_token": access_token, "token_type": "bearer"}

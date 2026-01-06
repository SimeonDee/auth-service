from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from typing import Annotated
from app.core.jwt import decode_access_token
from app.db.session import get_db
from app.services.user_service import get_user

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/token")

OAuth2_Dependency = Annotated[str, Depends(oauth2_scheme)]

DB_Dendency = Annotated[Session, Depends(get_db)]


async def get_current_user(
    token: OAuth2_Dependency,
    db: DB_Dendency,
):
    payload = decode_access_token(token)
    if not payload:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication",
        )
    user_id = int(payload.get("sub"))
    user = get_user(db, user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="User not found"
        )
    return user

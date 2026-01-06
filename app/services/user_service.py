from sqlalchemy import select
from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import UserCreate
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["sha256_crypt"], deprecated="auto")


def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def get_user_by_email(db: Session, email: str):
    q = select(User).where(User.email == email)
    res = db.execute(q)
    return res.scalars().first()


def get_user(db: Session, user_id: int):
    q = select(User).where(User.id == user_id)
    res = db.execute(q)
    return res.scalars().first()


def create_user(db: Session, user_in: UserCreate) -> User:
    # user = User(
    #     email=user_in.email,
    #     hashed_password=get_password_hash(user_in.password),
    # )
    user = User(
        **user_in.model_dump(exclude={"password"}),
        hashed_password=get_password_hash(user_in.password),
    )

    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def authenticate_user(db: Session, email: str, password: str):
    user = get_user_by_email(db, email)
    if not user:
        return None
    if not verify_password(password, user.hashed_password):
        return None
    return user

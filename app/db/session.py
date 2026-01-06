from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from app.core.config import settings


# For sync SQLAlchemy use the psycopg2 driver (requirements include
# psycopg2-binary). Convert common postgres:// URL to a SQLAlchemy
# compatible postgresql:// URL when necessary.
DATABASE_URL = settings.DATABASE_URL.replace("postgres://", "postgresql://")

engine = create_engine(
    DATABASE_URL,
    future=True,
    connect_args=(
        {
            "check_same_thread": False,
        }
        if "sqlite" in DATABASE_URL
        else {}
    ),
)

SessionLocal = sessionmaker(
    bind=engine, autoflush=False, autocommit=False, expire_on_commit=False
)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def create_all_tables():
    Base.metadata.create_all(bind=engine)


def drop_all_tables():
    Base.metadata.drop_all(bind=engine)


def recreate_all_tables():
    drop_all_tables()
    create_all_tables()

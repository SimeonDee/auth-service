import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from httpx import AsyncClient, ASGITransport
from asgi_lifespan import LifespanManager

from app.main import app
from app.db.session import Base, get_db


TEST_SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"


@pytest.fixture(scope="module")
def test_db_engine():
    engine = create_engine(
        TEST_SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
    )
    TestingSessionLocal = sessionmaker(bind=engine, autoflush=False)

    # create tables
    Base.metadata.create_all(bind=engine)

    yield engine, TestingSessionLocal

    Base.metadata.drop_all(bind=engine)
    engine.dispose()


@pytest.fixture(scope="module")
async def async_client(test_db_engine):
    engine, TestingSessionLocal = test_db_engine

    def override_get_db():
        db = TestingSessionLocal()
        try:
            yield db
        finally:
            db.close()

    # override the dependency
    app.dependency_overrides[get_db] = override_get_db

    async with LifespanManager(app):
        async with AsyncClient(
            transport=ASGITransport(app=app), base_url="http://test"
        ) as ac:
            yield ac

    app.dependency_overrides.pop(get_db, None)

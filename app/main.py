from fastapi import FastAPI
from app.api.api_v1 import auth, users
from app.core.config import settings


def create_app() -> FastAPI:
    app = FastAPI(title=settings.PROJECT_NAME)
    app.include_router(auth.router, prefix="/api/v1/auth", tags=["auth"])
    app.include_router(users.router, prefix="/api/v1/users", tags=["users"])

    @app.get("/health")
    async def health():
        return {"status": "ok"}

    return app


app = create_app()

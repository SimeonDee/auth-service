from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    PROJECT_NAME: str = "SAS School Management System - Auth Service"
    DEBUG: bool = False
    # Default to an in-memory sqlite DB for tests; override with env in prod
    DATABASE_URL: str = Field(
        "sqlite:///./my_test_db.db",
        json_schema_extra={"env": "DATABASE_URL"},
    )
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7  # 7 days
    JWT_SECRET: str = Field(
        "test_secret",
        json_schema_extra={"env": "JWT_SECRET"},
    )
    JWT_ALGORITHM: str = "HS256"

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()

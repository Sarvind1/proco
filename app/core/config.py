from typing import List
from pydantic_settings import BaseSettings
from pydantic import AnyHttpUrl, field_validator
import os

class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "Procurement System"
    
    # Environment
    ENVIRONMENT: str = "development"
    
    # CORS Configuration - with development defaults
    CORS_ORIGINS: List[str] = [
        "http://localhost:3000",
        "http://localhost:3001",
        "http://localhost:5173"
    ]

    @field_validator("CORS_ORIGINS", mode="before")
    @classmethod
    def assemble_cors_origins(cls, v: str | List[str]) -> List[str]:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, list):
            return v
        return []

    # Database - with SQLite default for development
    DATABASE_URL: str = "sqlite:///./test.db"

    # Amazon SP-API (optional in development)
    AMAZON_REFRESH_TOKEN: str = ""
    AMAZON_CLIENT_ID: str = ""
    AMAZON_CLIENT_SECRET: str = ""
    AMAZON_MARKETPLACE_ID: str = "ATVPDKIKX0DER"  # US marketplace default

    # Security
    SECRET_KEY: str = "your-secret-key-for-development-only-change-in-production"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    # Redis
    REDIS_URL: str = "redis://localhost:6379/0"

    # AWS Credentials (optional)
    AWS_ACCESS_KEY: str = ""
    AWS_SECRET_KEY: str = ""

    class Config:
        case_sensitive = True
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()

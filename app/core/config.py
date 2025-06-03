from typing import List
from pydantic_settings import BaseSettings
from pydantic import AnyHttpUrl, validator

class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "Procurement System"
    
    # CORS Configuration
    CORS_ORIGINS: List[AnyHttpUrl] = []

    @validator("CORS_ORIGINS", pre=True)
    def assemble_cors_origins(cls, v: str | List[str]) -> List[str] | str:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)

    # Database
    DATABASE_URL: str

    # Amazon SP-API
    AMAZON_REFRESH_TOKEN: str
    AMAZON_CLIENT_ID: str
    AMAZON_CLIENT_SECRET: str
    AMAZON_MARKETPLACE_ID: str = "ATVPDKIKX0DER"  # US marketplace default

    # Security
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    # Redis
    REDIS_URL: str

    # AWS Credentials
    AWS_ACCESS_KEY: str = ""
    AWS_SECRET_KEY: str = ""

    # Allowed Origins (for CORS, string list)
    ALLOWED_ORIGINS: List[str] = []

    @validator("ALLOWED_ORIGINS", pre=True)
    def assemble_allowed_origins(cls, v: str | List[str]) -> List[str] | str:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)

    class Config:
        case_sensitive = True
        env_file = ".env"

settings = Settings() 
from typing import List, Union
from pydantic import AnyHttpUrl, BaseSettings, validator


class Settings(BaseSettings):
    ENV: str = "unknown"
    PROJECT_NAME: str = "vapaus-backend"
    SIGNUP_VERIFY_EXPIRATION_HOURS: int = 2
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []

    @validator("BACKEND_CORS_ORIGINS", pre=True)
    def assemble_cors_origins(cls, v: Union[str, List[str]]) -> Union[List[str], str]:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)

    # use the in-memory postgre database
    DATABASE_URI: str = "postgresql://"

    class Config:
        case_sensitive = True
        env_file = ".env"


settings = Settings()

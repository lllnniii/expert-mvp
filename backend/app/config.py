from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "PromExpert_ais"
    debug: bool = True

    USE_SQLITE: bool = True

    DB_USER: str
    DB_PASSWORD: str
    DB_NAME: str
    DB_HOST: str
    DB_PORT: int = 5432

    cors_allowed_origins: str = "*"
    static_dir: str = "static"
    # SECRET_KEY: str
    # ALGORITHM: str = "HS256"
    # ACCESS_TOKEN_EXPIRE_MINUTES: int = 480

    @property
    def database_url(self) -> str:
        if self.USE_SQLITE:
            # SQLite создаст файл local_db.db в корне папки backend
            return "sqlite:///./local_db.db"

        return (
            f"postgresql://{self.DB_USER}:{self.DB_PASSWORD}"
            f"@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
        )

    class Config:
        env_file = ".env"

settings = Settings()

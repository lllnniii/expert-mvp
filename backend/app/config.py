from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "PromExpert_ais"
    debug: bool = True

    USE_SQLITE: bool = False

    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    POSTGRES_HOST: str
    POSTGRES_PORT: int = 5432

    JWT_SECRET : str
    JWT_EXPIRE_MINUTES: int
    REFRESH_EXPIRE_DAYS: int

    cors_allowed_origins: str = "*"
    static_dir: str = "static"


    @property
    def database_url(self) -> str:
        if self.USE_SQLITE:
            return "sqlite:///./local_db.db"
        return(
            f"postgresql://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_HOST}:"
            f"{self.POSTGRES_PORT}/{self.POSTGRES_DB}")

    class Config:
        env_file = ".env"

settings = Settings()

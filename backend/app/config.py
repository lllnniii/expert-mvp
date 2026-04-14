from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "PromExpert_ais"
    debug: bool = True

    USE_SQLITE: bool = True

    DB_USER: str
    DB_PASSWORD: str
    DB_NAME: str
    DB_HOST: str
    DB_PORT: int

    JWT_SECRET : str
    JWT_EXPIRE_MINUTES: int

    cors_allowed_origins: str = "*"
    static_dir: str = "static"


    @property
    def database_url(self) -> str:
        if self.USE_SQLITE:
            return "sqlite:///./local_db.db"
        return(
            f"postgresql://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}")
        # return (
        #     f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
        # )
    # def sqlalchemy_url(self) -> str:
    #     return (
    #         f"postgresql+psycopg2://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
    #     )


    class Config:
        env_file = ".env"

settings = Settings()

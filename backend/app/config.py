from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):
	app_name: str = "PromExpert_ais"
	debug: bool = True

	USE_SQLITE: bool = False

	POSTGRES_USER: Optional[str] = None
	POSTGRES_PASSWORD: Optional[str] = None
	POSTGRES_DB: Optional[str] = None
	POSTGRES_HOST: Optional[str] = None
	POSTGRES_PORT: int = 5432

	JWT_SECRET: str
	JWT_EXPIRE_MINUTES: int
	REFRESH_EXPIRE_DAYS: int

	cors_allowed_origins: str = "*"
	static_dir: str = "static"

	@property
	def database_url(self) -> str:
		if self.USE_SQLITE:
			return "sqlite:///./local_db.db"
		if not all([self.POSTGRES_USER, self.POSTGRES_PASSWORD, self.POSTGRES_DB, self.POSTGRES_HOST]):
			raise ValueError("PostgreSQL settings are required when USE_SQLITE=False")
		return (
			f"postgresql://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_HOST}:"
			f"{self.POSTGRES_PORT}/{self.POSTGRES_DB}"
		)

	class Config:
		env_file = ".env"

settings = Settings()
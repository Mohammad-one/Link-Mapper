from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql+psycopg2://postgres:postgres@localhost:5432/affiliate_db"

    class Config:
        env_file = ".env"


settings = Settings()

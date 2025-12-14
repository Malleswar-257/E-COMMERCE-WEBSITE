from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql://user:password@localhost/db"
    SECRET_KEY: str = "dev-secret-key-change-in-production"
    # All fields should have defaults

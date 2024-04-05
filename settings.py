from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DB_URL:str = 'sqlite:///db.sqlite3'
    BASE_URL:str = '127.0.0.1:8000'


def get_settings() -> Settings:
    return Settings()
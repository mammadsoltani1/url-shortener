from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env")

    # Database
    DATABASE_URL: str = "postgresql+psycopg2://postgres:postgres@db:5432/url_shortener"

    # Short code strategy: random | hash | uuid
    SHORTCODE_STRATEGY: str = "hash"
    SHORTCODE_LENGTH: int = 8

    # App
    BASE_URL: str = "http://localhost:8000"

settings = Settings()
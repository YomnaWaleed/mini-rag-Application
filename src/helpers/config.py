from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    APP_NAME: str = "mini-RAG"
    APP_VERSION: str = "0.1"
    OPENROUTER_API_KEY: str

    model_config = SettingsConfigDict(env_file=".env")


def get_settings():
    return Settings()

from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    telegram_bot_token: str = ""
    gemini_api_key: str = ""
    grok_api_key: str = ""
    database_url: str = ""
    llm_provider: str = "gemini"

    gemini_model: str = "gemini-2.5-flash"
    grok_model: str = "grok-2-latest"
    app_name: str = "Content Bot"
    environment: str = "development"
    log_level: str = "INFO"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


@lru_cache(maxsize=1)
def get_settings() -> Settings:
    return Settings()


settings = get_settings()

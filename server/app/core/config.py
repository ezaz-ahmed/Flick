from functools import lru_cache
from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict

SERVER_DIR = Path(__file__).resolve().parents[2]
ROOT_DIR = SERVER_DIR.parent

class Settings(BaseSettings):
    app_name: str = "Flick"
    app_version: str = "0.1.0"
    api_v1_prefix: str = "/api/v1"
    database_url: str

    model_config = SettingsConfigDict(
        env_file=ROOT_DIR / ".env",
        env_file_encoding="utf-8",
    )


@lru_cache
def get_settings() -> Settings:
    return Settings() # type: ignore[call-arg]
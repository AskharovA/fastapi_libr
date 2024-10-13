from typing import Literal
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    MODE: Literal["dev", "prod", "test"] = "dev"

    @property
    def db_url(self) -> str:
        return f""

    @property
    def redis_url(self) -> str:
        return f""

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()

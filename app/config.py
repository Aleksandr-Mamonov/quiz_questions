from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    database_username: str
    database_password: str
    database_name: str
    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "Awesome API"
    admin_username: str = ""
    admin_password: str = ""
    secret_key: str = ""
    database_url: str = ""
    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()

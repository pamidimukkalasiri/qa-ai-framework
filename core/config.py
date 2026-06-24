from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    base_url: str = "https://automationexercise.com/"
    browser: str = "chromium"
    headless: bool = True
    slow_mo: int = 0
    timeout: int = 30000
    class Config:
        env_file = ".env"
# Single settings instance used across framework
settings = Settings()
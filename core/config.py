from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field


class Settings(BaseSettings):
    base_url: str = "https://automationexercise.com"
    browser: str = "chromium"
    headless: bool = False
    slow_mo: int = 0
    timeout: int = 60000

    @property
    def wait_timeout(self):
        return self.timeout

    # Test Credentials
    test_email: str = Field(validation_alias="test_email")
    test_password: str = Field(validation_alias="test_password")

    # Free Gemini API
    groq_api_key: str = ""

    # MODERN V2 SYNTAX ONLY (Safely ignores unmatched .env fields)
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

# Single settings instance used across framework
settings = Settings()
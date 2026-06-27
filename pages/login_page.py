from pages.base_page import BasePage
from core.logger import logger
from core.config import settings

class LoginPage(BasePage):
    # locators
    EMAIL = "input[data-qa='login-email']"
    PASSWORD = "input[data-qa='login-password']"
    LOGIN_BUTTON = "button[data-qa='login-button']"
    ERROR_MESSAGE = "p:has-text('Your email or password is incorrect!')"

    def go_to_login_page(self):
        self.navigate(settings.base_url)

    def login(self, email: str, password: str):
        logger.info(f"Logging in: {email}")
        self.fill(self.EMAIL, email)
        self.fill(self.PASSWORD, password)
        self.click(self.LOGIN_BUTTON)

    def get_error_message(self) -> str:
        return self.get_text(self.ERROR_MESSAGE)

    def is_error_visible(self) -> bool:
        return self.is_visible(self.ERROR_MESSAGE)
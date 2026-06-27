from pages.base_page import BasePage
from core.logger import logger
from core.config import settings

class HomePage(BasePage):
    """Home page of automationexercise.com"""

    # Locators
    LOGIN_SIGNUP = "a[href='/login']"
    LOGGED_IN_TEXT = "a:has-text('Logged in as')"
    LOGOUT = "a[href='/logout']"
    NAV_CART = "a[href='/view_cart']"

    def go_to_home_page(self):
        self.navigate(settings.base_url)

    def click_login(self):
        self.click(self.LOGIN_SIGNUP)

    def is_logged_in(self) -> bool:
        return self.is_visible(self.LOGGED_IN_TEXT)

    def get_logged_in_text(self) -> str:
        return self.get_text(self.LOGGED_IN_TEXT)

    def logout(self):
        self.click(self.LOGOUT)
        logger.info("User logged out")
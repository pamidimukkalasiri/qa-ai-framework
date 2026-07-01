import pytest
from pages.login_page import LoginPage
from pages.home_page import HomePage
from core.config import settings

class TestLogin:

    @pytest.fixture(autouse=True)
    def setup_login_page(self, page):
        """Automatically navigates to login page"""
        page.goto(f"{settings.base_url}/login")
        self.login = LoginPage(page)
        self.home = HomePage(page)
        clean_url = f"{settings.base_url.rstrip('/')}/login"
        page.goto(clean_url)

    def test_valid_login(self, page):
        """Valid credentials should log user in."""
        self.login.login(settings.test_email, settings.test_password)
        assert self.home.is_logged_in(),"User should be logged in"

    def test_invalid_password(self, page):
        """Invalid password should not log user in."""
        self.login.login(settings.test_email, "wrong password")
        assert self.login.is_error_visible(), "Error should be visible"

    def test_empty_email(self, page):
        """Empty email should not log user in."""
        self.login.login("", settings.test_password)
        expected_url = f"{settings.base_url.rstrip('/')}/login"
        assert page.url == expected_url, "Base url should be set correctly"

    def test_logout(self, page):
        """Logout should not log user in."""
        self.login.login(settings.test_email, settings.test_password)
        self.home.logout()
        assert not self.home.is_logged_in(),"User should be logged out"
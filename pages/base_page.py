import allure
from playwright.sync_api import Page
from core.logger import logger
from core.decorators import retry, log_action, timer

class BasePage:
    """Base class for all page objects . All pages inherit from this -
    gets retry, logging, timing for free
    Every action automatically recorded as allure-setup- no manual steps needed in tests"""
    def __init__(self, page):
        self.page = page
    @allure.step("Navigating to {url}")
    @log_action
    @timer
    def navigate(self, url: str):
        """Navigates to url"""
        self.page.goto(url)

    @allure.step("Clicking:{locator}")
    @log_action
    @retry(times=3)
    def click(self, locator: str) -> None:
        self.page.locator(locator).click()


    @allure.step("Filling input field")
    @log_action
    @retry(times=3, delay=1.0)
    def fill(self, locator: str, text: str):
        """Fills text in locator and retry 3 times if it fails"""
        self.page.locator(locator).fill(text)

    @allure.step("Checking visibility : {locator}")
    def is_visible(self, locator: str) -> bool:
        """Checks if locator is visible"""
        return self.page.locator(locator).is_visible()

    @allure.step("Getting text: {locator}")
    def get_text(self, locator: str) -> str:
        """Gets text from locator and retry 3 times if it fails"""
        return self.page.locator(locator).inner_text().strip()

    def wait_for_url(self, url: str):
        """Waits until url is visible"""
        self.page.wait_for_url(url)

    def click(self, locator: str):
        self.page.click(locator)

    def navigate(self, url: str):
        self.page.goto(url)

    def wait_for_url_contains(self, keyword: str, timeout: int = 5000):
        """Waits until url contains keyword"""
        self.page.wait_for_url(f"**/{keyword}**", timeout=timeout)
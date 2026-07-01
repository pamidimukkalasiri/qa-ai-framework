import pytest
from playwright.sync_api import sync_playwright
from core.config import settings
from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.product_page import ProductPage
from pages.cart_page import CartPage

@pytest.fixture(scope='session')
def browser():
    """Launch browser once for entire test session"""
    with sync_playwright() as p:
        browser = getattr(p, settings.BROWSER).launch(
            headless=settings.headless,
            slow_mo=settings.slow_mo
        )
        yield browser
        browser.close()

@pytest.fixture(scope='function')
def page(browser):
    """Fresh page for every single test"""
    context = browser.new_context()
    page = context.new_page()
    page.set_default_timeout(settings.timeout)
    yield page
    context.close()

@pytest.fixture(scope='function')
def logged_in_page(page):
    """Reusable fixture - user already logged in.Any test that needs login just uses this
    instead of repeating login steps."""
    login = LoginPage(page)
    login.go_to_login_page()
    login.login(settings.test_email, settings.test_password)
    yield page

@pytest.fixture(scope='function')
def cart_ready_page(logged_in_page):
    """Reusable fixture - user logged in And has item in cart already
    Builds on top of logged_in_page fixture """
    product = ProductPage(logged_in_page)
    product.go_to_products()
    product.add_first_product_to_cart()
    yield logged_in_page
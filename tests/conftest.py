import pytest
from playwright.sync_api import sync_playwright
from core.config import settings

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
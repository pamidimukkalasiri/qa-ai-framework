import pytest
import os
import allure
from playwright.sync_api import sync_playwright
from core.config import settings
from pages.login_page import LoginPage
from pages.product_page import ProductPage


#------ Folder Setup---------------------------
def pytest_configure(config):
    """Create required folders on startup"""
    os.makedirs("reports/allure-results", exist_ok=True)
    os.makedirs("reports/traces", exist_ok=True)

#--------Auto Feature by Filename--------------------------
def pytest_collection_modifyitems(items):
    """Automatically assign allure feature based on test file name.
    No need to add @allure.feature in every file"""
    feature_map = {
        "login" : "Authentication",
        "product" : "Products",
        "cart" : "Shopping Cart",
        "checkout" : "Checkout",
        "network" : "Network Interception",
        }
    for item in items:
        file_name = item.fspath.basename.lower()
        for keyword, feature in feature_map.items():
            if keyword in file_name:
                item.add_marker(allure.feature(feature))
                break

#-------Browser Fixture------------------
@pytest.fixture(scope='session')
def browser_type_launch_args():
    """Override browser launch page"""
    return {
        "headless":settings.headless,
        "slow_mo":settings.slow_mo
    }

@pytest.fixture(scope='session')
def browser(browser_type_launch_args):
    """Each parallel worker get its own browser instance"""
    with sync_playwright() as p:
        browser = getattr(p, settings.browser).launch(**browser_type_launch_args)
        yield browser
        browser.close()

#-------- Page fixture--------------------
@pytest.fixture(scope='function')
def page(browser):
    """Fresh page for every single test"""
    context = browser.new_context(
        #Each context is completely isolated
        viewport={'width': 1280, 'height': 720},
    )
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

@pytest.fixture(scope='function')
def page(browser):
    """Each test gets fresh page with trace recording enabled."""
    context = browser.new_context(viewport={'width': 1280, 'height': 720})
    #Start Tracing
    context.tracing.start(
        screenshots=True,
        snapshots = True,
        sources = True
    )
    page = context.new_page()
    page.set_default_timeout(settings.timeout)
    yield page

    # Stop tracing _ save is test failed
    context.tracing.stop(
        path="reports\\trace.zip"
    )
    context.close()

#---------Screenshot on Failure-----------------------------
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Automatically takes screenshot when any test fails and attaches to Allure report"""
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        #Try all possible page fixture
        page = (
            item.funcargs.get("page") or
            item.funcargs.get("logged_in_page") or
            item.funcargs.get("cart_ready_page")
        )

        if page:
            # Full page Screenshot
            screenshot = page.screenshot(full_page=True)
            # Attach to Allure report
            allure.attach(
                screenshot,
                name= "failure_screenshot",
                attachment_type=allure.attachment_type.PNG
            )

import pytest
import allure
from allure_commons.types import Severity
from data.test_data import TestData
from pages.base_page import BasePage
from pages.cart_page import CartPage
from pages.login_page import LoginPage
from pages.home_page import HomePage
from core.config import settings
from pages.product_page import ProductPage

@allure.feature("Shopping Cart")
class TestCart:

    severity = Severity.CRITICAL

    @pytest.fixture(autouse=True)
    def setup_cart_page(self, page):
        self.login = LoginPage(page)
        self.home = HomePage(page)
        self.cart = CartPage(page)
        self.base = BasePage(page)
        self.product = ProductPage(page)
        clean_url = f"{settings.base_url.rstrip('/')}/products"
        page.goto(clean_url)

    def test_cart_has_item_after_adding(self, page):
        self.product.go_to_products()
        self.product.add_first_product_to_cart()
        self.product.continue_shopping()
        self.cart.go_to_cart()
        assert self.cart.get_cart_items_count() > 0, \
            "Cart should have at least 1 item"

    def test_product_name_in_cart(self, page):
        self.product.go_to_products()
        self.product.search_product(TestData.search_product)
        self.product.add_first_product_to_cart()
        self.product.go_to_cart()
        names = self.cart.get_product_names_in_cart()
        assert len(names) > 0, \
            "Product name should appear in cart"

    def test_remove_item_from_cart(self, page):
        self.product.go_to_products()
        self.product.add_first_product_to_cart()
        self.product.go_to_cart()
        self.cart.remove_first_item()
        page.wait_for_timeout(settings.wait_timeout)
        assert self.cart.is_cart_empty(), \
            "Cart should not be empty"

    def test_checkout_requires_login(self, page):
        self.product.go_to_products()
        self.product.add_first_product_to_cart()
        self.product.go_to_cart()
        self.cart.proceed_to_checkout()
        page.get_by_role("link", name="Register / Login").click()
        self.cart.wait_for_url_contains("login")
        assert "login" in page.url
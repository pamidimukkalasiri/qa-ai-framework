import pytest
from pages.product_page import ProductPage
from pages.home_page import HomePage
from core.config import settings
from data.test_data import TestData
import allure
from allure_commons.types import Severity

@allure.feature("Products")
class TestProducts:

    Severity = Severity.NORMAL

    @pytest.fixture(autouse=True)
    def setup_product_page(self, page):
        """Automatically navigates to products page"""

        self.product = ProductPage(page)
        self.home = HomePage(page)
        self.product.go_to_products()
        clean_url = f"{settings.base_url.rstrip('/')}/products"
        page.goto(clean_url)

    def test_navigate_to_products(self):
         assert self.product.is_products_page(),\
            "should be on products page"

    def test_search_existing_product(self, page):
        self.product.search_product(TestData.search_product)
        names = self.product.get_all_product_names()
        assert len(names) > 0, \
            "Search should return at least one product."

    def test_search_result_matches_keyword(self):
        search_term = TestData.search_term
        self.product.search_product(search_term)
        names = self.product.get_all_product_names()
        print(f"\nDEBUG- collected names: {names}")
        matches = [n for n in names if search_term.lower() in n.lower()]
        assert len(matches) > 0, f"Results should contain keyword: {search_term}"


    def test_add_product_to_cart(self, page):
        self.product.add_first_product_to_cart()
        self.product.continue_shopping()

        assert self.product.is_products_page(), TestData.order_comment
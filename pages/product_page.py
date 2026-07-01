from pages.base_page import  BasePage
from core.config import settings
from core.logger import logger

class ProductPage(BasePage):
    """Product page of automationexcercise.com"""

    #Locators
    SEARCH_INPUT = "input#search_product"
    SEARCH_BUTTON = "button#submit_search"
    PRODUCT_NAMES = ".productinfo p"
    PRODUCT_PAGE_TITLE = "h2.title.text-center"
    ADD_TO_CART = ".productinfo a.add-to-cart"
    CONTINUE_SHOPPING = "button.close-modal"
    VIEW_CART = "a:has-text('View Cart')"


    def go_to_products(self):
        self.navigate(f"{settings.base_url}/products")

    def search_product(self, product_name):
        logger.info(f"searching product {product_name}")
        self.fill(self.SEARCH_INPUT, product_name)
        self.click(self.SEARCH_BUTTON)

    def get_all_product_names(self) -> list:
        logger.info(f"getting all product names")
        elements = self.page.locator(self.PRODUCT_NAMES).all()
        return [eli.inner_text() for eli in elements]

    def is_products_page(self) -> bool:
        return self.is_visible(self.PRODUCT_PAGE_TITLE)

    def add_first_product_to_cart(self) -> None:
        logger.info(f"Adding first product to cart")
        first_product = self.page.locator(
            self.ADD_TO_CART).first
        first_product.click()
        logger.info(f"Added first product to cart")

    def continue_shopping(self):
        self.click(self.CONTINUE_SHOPPING)

    def go_to_cart(self):
        self.click(self.VIEW_CART)



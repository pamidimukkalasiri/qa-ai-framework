from pages.base_page import BasePage
from core.config import settings
from core.logger import logger

class CartPage(BasePage):

    # Locators
    CART_ITEMS = "div.cart_info"
    PRODUCT_NAME = "td.cart_description"
    DELETE_BUTTON = "a.cart_quantity_delete"
    EMPTY_CART_MESSAGE = "b:has-text('Cart is empty!')"
    CHECKOUT_BUTTON = "a:has-text('Proceed To Checkout')"

    def go_to_cart(self):
        self.navigate(f"{settings.base_url}/view_cart")

    def get_cart_items_count(self):
        items = self.page.locator(self.CART_ITEMS).all()
        return len(items)

    def get_product_names_in_cart(self):
        elements = self.page.locator(self.PRODUCT_NAME).all()
        return [eli.inner_text for eli in elements]

    def remove_first_item(self):
        self.page.locator(self.DELETE_BUTTON).first.click()

    def is_cart_empty(self) -> bool:
        return self.is_visible(self.EMPTY_CART_MESSAGE)

    def proceed_to_checkout(self):
        self.click(self.CHECKOUT_BUTTON)
        logger.info("Proceed to checkout")
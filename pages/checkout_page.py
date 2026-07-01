from pages.base_page import BasePage
from core.config import settings
from core.logger import logger

class CheckoutPage(BasePage):

    #Locators
    DELIVERY_ADDRESS = "#address_delivery"
    COMMENT_BOX = "textarea.form-control"
    PLACE_ORDER = "a:has-text('Place Order')"
    NAME_ON_CARD = "input[data-qa='name-on-card']"
    CARD_NUMBER = "input[data-qa='card-number']"
    CVC = "input[data-qa='cvc']"
    EXPIRY_MONTH = "input[data-qa='expiry-month']"
    EXPIRY_YEAR = "input[data-qa='expiry-year']"
    PAY_BUTTON = "button[data-qa='pay-button']"
    SUCCESS_MESSAGE = "b:has-text('Your order has been placed successfully!')"

    def goto_checkout_page(self):
        self.navigate(f"{settings.base_url}/checkout")

    def is_deliver_address_visible(self)->bool:
        return self.is_visible(self.DELIVERY_ADDRESS)

    def add_comment(self, comment:str):
        self.fill(self.COMMENT_BOX, comment)

    def click_place_order(self):
        self.click(self.PLACE_ORDER)
        logger.info(f"Place Order has been clicked")

    def fill_payment_details(self, name:str, card_number:str,
                             cvc:str,month:str,year:str):
        logger.info("Filling Payment Details")
        self.fill(self.NAME_ON_CARD, name)
        self.fill(self.CARD_NUMBER, card_number)
        self.fill(self.CVC, cvc)
        self.fill(self.EXPIRY_MONTH, month)
        self.fill(self.EXPIRY_YEAR, year)

    def click_pay(self):
        self.click(self.PAY_BUTTON)
        logger.info("payment submitted")

    def is_order_successful(self)->bool:
        success_locator = self.page.get_by_text("Congratulations! Your order has been confirmed!")
        success_locator.wait_for(state="visible", timeout=3000)
        return success_locator.is_visible()
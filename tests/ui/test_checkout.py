import pytest
from core.config import settings
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.product_page import ProductPage
from pages.login_page import LoginPage
from data.test_data import TestData

@pytest.fixture(autouse=True)
def checkout_flow(page):
    # Initialize all Page Objects explicitly
    login = LoginPage(page)
    product = ProductPage(page)
    cart = CartPage(page)
    checkout = CheckoutPage(page)

    # Execute the step-by-step setup workflow
    page.goto(f"{settings.base_url}/login")
    login.login(settings.test_email, settings.test_password)
    product.go_to_products()
    product.add_first_product_to_cart()
    product.continue_shopping()
    cart.go_to_cart()
    cart.proceed_to_checkout()
    return checkout


class TestCheckout:
    def test_checkout_page_loads(self, checkout_flow):
        """Checkout page should show delivery addresses
        Uses cart_ready_page fixture
        already logged in + item in cart"""
        assert checkout_flow.is_deliver_address_visible(), \
            "Delivery address should be visible"

    def test_place_order_loads_payment(self, checkout_flow):
        """Clicking place order should show payment form"""
        checkout_flow.add_comment("Test order comment")
        checkout_flow.click_place_order()

        assert checkout_flow.is_visible(
            checkout_flow.NAME_ON_CARD), "Payment form should appear"

    def test_complete_order_with_payment(self, checkout_flow):
        """Full checkout flow - add details and pay"""
        checkout_flow.click_place_order()
        checkout_flow.fill_payment_details(
            name= str(TestData.card_name),
            card_number= str(TestData.card_number),
            cvc= str(TestData.card_cvc),
            month= str(TestData.card_month),
            year= str(TestData.card_year),
        )
        checkout_flow.click_pay()
        assert checkout_flow.is_order_successful(), "Order should be successful"
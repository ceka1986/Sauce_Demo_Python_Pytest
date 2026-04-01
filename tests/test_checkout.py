from pages.cart_page import CartPage
from pages.checkout_complete_page import CheckoutCompletePage
from pages.checkout_step_one_page import CheckoutStepOnePage
from pages.checkout_step_two_page import CheckoutStepTwoPage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
import pytest
from utils.data import TestData


class TestCheckoutFlow:
    @pytest.fixture(autouse=True)
    def setup_checkout(self, login_page:LoginPage):
        login_page.open()
        login_page.login_with_credentials(TestData.VALID_USER, TestData.VALID_PASS)


    def test_complete_checkout_flow(self, inventory_page:InventoryPage, 
                                          cart_page:CartPage, 
                                          checkout_step_one_page:CheckoutStepOnePage,
                                          checkout_step_two_page:CheckoutStepTwoPage,
                                          checkout_complete_page:CheckoutCompletePage):
        
        inventory_page.add_item_to_cart(TestData.BACKPACK)
        inventory_page.click_cart_icon()
        cart_page.click_checkout()
        checkout_step_one_page.fill_in_the_form(TestData.FIRST_NAME, TestData.LAST_NAME, TestData.POSTAL_CODE)
        checkout_step_one_page.click_on_continue_button()
        checkout_step_two_page.click_finish_button()

        assert checkout_complete_page.get_page_title() == TestData.CHECKOUT_PAGE_TITLE
        assert checkout_complete_page.get_header_text() == TestData.CHECKOUT_COMPLETE_MESSAGE
        
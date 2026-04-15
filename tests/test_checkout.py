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
    def setup_checkout(self, logged_in_session):
        """
        By including 'logged_in_session' as a parameter, 
        Pytest automatically handles both login and cleanup.
        """
        pass

    @pytest.fixture
    def go_to_checkout_form(self, logged_in_session, inventory_page:InventoryPage, cart_page:CartPage):
        inventory_page.add_item_to_cart(TestData.BACKPACK)
        inventory_page.click_cart_icon()
        cart_page.click_checkout()

    def test_complete_checkout_flow(self, inventory_page:InventoryPage, 
                                          cart_page:CartPage, 
                                          checkout_step_one_page:CheckoutStepOnePage,
                                          checkout_step_two_page:CheckoutStepTwoPage,
                                          checkout_complete_page:CheckoutCompletePage):
        
        inventory_page.add_item_to_cart(TestData.BACKPACK)
        inventory_page.click_cart_icon()
        cart_page.click_checkout()
        checkout_step_one_page.wait_for_page_load()
        checkout_step_one_page.fill_in_the_form(TestData.FIRST_NAME, TestData.LAST_NAME, TestData.POSTAL_CODE)
        checkout_step_one_page.click_continue_button()
        checkout_step_two_page.wait_for_page_load()
        checkout_step_two_page.click_finish_button()
        checkout_complete_page.wait_for_page_load() 

        assert checkout_complete_page.get_page_title() == TestData.CHECKOUT_PAGE_TITLE
        assert checkout_complete_page.get_header_text() == TestData.CHECKOUT_COMPLETE_MESSAGE

    @pytest.mark.parametrize("first_name,last_name,postal_code,expected_error", TestData.INVALID_FORM_DATA)
    def test_invalid_form(self, go_to_checkout_form, checkout_step_one_page:CheckoutStepOnePage, first_name, last_name, postal_code, expected_error):
        checkout_step_one_page.fill_in_the_form(first_name, last_name, postal_code)
        checkout_step_one_page.click_continue_button()

        actual_error = checkout_step_one_page.get_error_message()

        assert expected_error in actual_error, f"Expected '{expected_error}', but got '{actual_error}'"
        assert checkout_step_one_page.is_error_displayed()


        
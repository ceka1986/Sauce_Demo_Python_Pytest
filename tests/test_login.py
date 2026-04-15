

from pages.components.sidebar import Sidebar
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
import pytest
from utils.data import TestData


class TestLogin:

    @pytest.fixture(autouse=True)
    def setup_login(self, login_page: LoginPage):
        login_page.open()

    def test_valid_login(self, login_page:LoginPage, inventory_page:InventoryPage):

        login_page.login_with_credentials(TestData.VALID_USER,  TestData.VALID_PASS)

        assert inventory_page.get_title() == "Products"


    @pytest.mark.parametrize("username, password, expected_error", TestData.INVALID_LOGIN_DATA)
    def test_invalid_logins(self, login_page:LoginPage, username, password, expected_error):

        login_page.login_with_credentials(username, password)

        actual_error = login_page.get_error_message()

        assert expected_error in actual_error
        assert login_page.is_login_button_displayed()

    def test_locked_out_user(self, login_page:LoginPage):

        login_page.login_with_credentials(TestData.LOCKED_USER, TestData.VALID_PASS)

        expected_error = TestData.ERROR_LOCKED_OUT
        actual_error = login_page.get_error_message()
        

        assert expected_error in actual_error
        assert login_page.is_login_button_displayed()

    def test_logout(self, login_page:LoginPage, sidebar:Sidebar):

        login_page.login_with_credentials(TestData.VALID_USER, TestData.VALID_PASS)
        sidebar.logout()

        assert login_page.is_login_button_displayed()
        assert login_page.is_at()
        

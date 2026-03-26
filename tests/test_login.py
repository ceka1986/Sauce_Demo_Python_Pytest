

from pages.components.sidebar import Sidebar
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
import pytest


class TestLogin:

    @pytest.fixture(autouse=True)
    def setup_login(self, login_page: LoginPage):
        login_page.open()

    def test_valid_login(self, login_page:LoginPage, inventory_page:InventoryPage):
        login_page.login_with_credentials("standard_user", "secret_sauce")

        assert inventory_page.get_title() == "Products"


    @pytest.mark.parametrize("username, password, expected_error", [
        ("standard_user", "wrong_pass", "Username and password do not match any user in this service"),
        ("wrong_user","secret_sauce", "Username and password do not match any user in this service"),
        ("wrong_user","wrong_pass", "Username and password do not match any user in this service"),
        ("","", "Username is required")
    ])
    def test_invalid_logins(self, login_page:LoginPage, username, password, expected_error):
        login_page.login_with_credentials(username, password)

        error_text = login_page.get_error_text()

        assert expected_error in error_text
        assert login_page.is_login_button_displayed()

    def test_locked_out_user(self, login_page:LoginPage):
        login_page.login_with_credentials("locked_out_user", "secret_sauce")
        error_text = "Sorry, this user has been locked out"

        assert error_text in login_page.get_error_text()
        assert login_page.is_login_button_displayed()

    def test_logout(self, login_page:LoginPage, sidebar:Sidebar):
        login_page.login_with_credentials("standard_user", "secret_sauce")
        sidebar.logout()

        assert login_page.is_login_button_displayed()
        assert login_page.is_at()
        

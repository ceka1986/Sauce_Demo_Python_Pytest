

from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage


class TestLogin:

    def test_valid_login(self, login_page:LoginPage, inventory_page:InventoryPage):
        login_page.open()
        login_page.login_with_credentials("standarad_user", "secret_sauce")

        assert inventory_page.get_title() == "Products"


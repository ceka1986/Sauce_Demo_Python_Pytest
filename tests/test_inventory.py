from pages.components.sidebar import Sidebar
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
import pytest


class TestInventory:

    @pytest.fixture(autouse=True)
    def setup_inventory(self, login_page:LoginPage, sidebar:Sidebar):
        login_page.open()
        login_page.login_with_credentials("standard_user", "secret_sauce")
        sidebar.reset_app_state()
        sidebar.close_menu()

    @pytest.mark.parametrize("item_name",["Sauce Labs Backpack","Sauce Labs Onesie"])
    def test_add_item_to_cart(self, inventory_page:InventoryPage,item_name):
        inventory_page.add_item_to_cart(item_name)

        assert inventory_page.get_cart_badge_count() == "1"
        assert inventory_page.is_item_in_cart(item_name)


from pages.components.sidebar import Sidebar
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
import pytest
from utils.data import TestData



class TestInventory:

    @pytest.fixture(autouse=True)
    def setup_inventory(self, login_page:LoginPage, sidebar:Sidebar):
        login_page.open()
        login_page.login_with_credentials(TestData.VALID_USER, TestData.VALID_PASS)
        sidebar.reset_app_state()
        sidebar.refresh_page()

    @pytest.mark.parametrize("item_name",[TestData.BACKPACK,TestData.SHIRT_RED])
    def test_add_item_to_cart(self, inventory_page:InventoryPage,item_name):
        inventory_page.add_item_to_cart(item_name)

        assert inventory_page.is_item_in_cart(item_name)
        assert inventory_page.get_cart_badge_count() == "1"
        
    
    def test_remove_item_from_cart(self, inventory_page:InventoryPage):
        item = TestData.BACKPACK
        inventory_page.add_item_to_cart(item)
        inventory_page.remove_item_from_cart(item)

        assert inventory_page.wait_for_text(inventory_page._get_dynamic_button_locator(item), "Add to cart")

    @pytest.mark.parametrize("sort_option, reverse", [
        (TestData.SORT_A_TO_Z, False),
        (TestData.SORT_Z_TO_A, True)])
    def test_sort_by_name(self, inventory_page:InventoryPage, sort_option, reverse):
        inventory_page.select_sort_option(sort_option)
        names = inventory_page.get_all_item_names()

        assert names == sorted(names, reverse=reverse)

    @pytest.mark.parametrize("sort_option, reverse", [
        (TestData.SORT_LOW_TO_HIGH, False),
        (TestData.SORT_HIGH_TO_LOW, True)])
    def test_sort_by_price(self, inventory_page: InventoryPage, sort_option, reverse):
        inventory_page.select_sort_option(sort_option)
        prices = inventory_page.get_all_item_prices()
    
        assert prices == sorted(prices, reverse=reverse)


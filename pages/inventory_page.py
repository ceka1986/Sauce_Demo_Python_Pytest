from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from utils.data import TestData


class InventoryPage(BasePage):

    _PAGE_TITLE = (By.CSS_SELECTOR, "[data-test='title']")
    _SORT_CONTAINER = (By.CSS_SELECTOR, "[data-test='product-sort-container']")
    _CART_LINK = (By.CSS_SELECTOR, "[data-test='shopping-cart-link']")
    _CART_BADGE = (By.CSS_SELECTOR, "[data-test='shopping-cart-badge']")
    _INVENTORY_ITEMS = (By.CSS_SELECTOR, "[data-test='inventory-item']")
    _ITEM_NAME = (By.CSS_SELECTOR, "[data-test='inventory-item-name']")
    _ITEM_PRICE = (By.CSS_SELECTOR, "[data-test='inventory-item-price']")
    _ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "[data-test^='add-to-cart']")
    _REMOVE_BUTTON = (By.CSS_SELECTOR, "[data-test^='remove']")

    def __init__(self, driver):
        """Initializes the InventoryPage with the WebDriver and sets the page URL"""
        super().__init__(driver)
        self.url = TestData.URL_INVENTORY

    def wait_for_page_load(self):
        """Waits for all inventory items to be fully rendered by React"""
        self.wait.until(EC.presence_of_all_elements_located(self._INVENTORY_ITEMS))

    def _get_add_button_locator(self, item_name):
        """Returns the data-test locator for the Add to Cart button of a specific item"""
        key = item_name.lower().replace(" ", "-")
        return (By.CSS_SELECTOR, f"[data-test='add-to-cart-{key}']")

    def _get_remove_button_locator(self, item_name):
        """Returns the data-test locator for the Remove button of a specific item"""
        key = item_name.lower().replace(" ", "-")
        return (By.CSS_SELECTOR, f"[data-test='remove-{key}']")

    def get_title(self):
        """Returns the title text of the inventory page"""
        return self.get_text(self._PAGE_TITLE)

    def add_item_to_cart(self, item_name):
        """Adds a specific item to the cart and waits for confirmation"""
        add_locator = self._get_add_button_locator(item_name)
        remove_locator = self._get_remove_button_locator(item_name)
        self.click(add_locator)
        # Wait for Remove button to appear — confirms item was added
        self.wait.until(EC.presence_of_element_located(remove_locator))

    def remove_item_from_cart(self, item_name):
        """Removes a specific item from the cart and waits for confirmation"""
        remove_locator = self._get_remove_button_locator(item_name)
        add_locator = self._get_add_button_locator(item_name)
        self.click(remove_locator)
        # Wait for Add to Cart button to appear — confirms item was removed
        self.wait.until(EC.presence_of_element_located(add_locator))

    def get_button_text(self, item_name):
        """Returns the current text of the cart button for a specific item"""
        try:
            remove_locator = self._get_remove_button_locator(item_name)
            self.driver.find_element(*remove_locator)
            return "Remove"
        except Exception:
            return "Add to cart"

    def is_item_in_cart(self, item_name):
        """Returns True if the item's Remove button is present in the DOM"""
        remove_locator = self._get_remove_button_locator(item_name)
        return len(self.driver.find_elements(*remove_locator)) > 0

    def click_cart_icon(self):
        """Clicks the shopping cart icon and waits for navigation to cart page"""
        self.click(self._CART_LINK)
        self.wait_for_url("cart.html")

    def get_cart_badge_count(self):
        """Returns the number shown on the cart badge, or '0' if not visible"""
        elements = self.driver.find_elements(*self._CART_BADGE)
        return elements[0].text if elements else "0"

    def select_sort_option(self, option_text):
        """Selects a sorting option from the dropdown by its visible text"""
        dropdown_element = self.find(self._SORT_CONTAINER)
        select = Select(dropdown_element)
        select.select_by_visible_text(option_text)

    def get_all_item_names(self):
        """Returns a list of all item names currently displayed on the page"""
        elements = self.find_all(self._ITEM_NAME)
        return [el.text for el in elements]

    def get_all_item_prices(self):
        """Returns a list of all item prices as floats"""
        elements = self.find_all(self._ITEM_PRICE)
        return [float(el.text.replace('$', '')) for el in elements]
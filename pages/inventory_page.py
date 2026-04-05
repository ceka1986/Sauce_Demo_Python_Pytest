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
    
    _ITEM_NAME = (By.CSS_SELECTOR, "[data-test='inventory-item-name']")
    _ITEM_PRICE = (By.CSS_SELECTOR, "[data-test='inventory-item-price']")

    def __init__(self, driver):
        """Initializes the InventoryPage with the WebDriver and sets the page URL"""
        super().__init__(driver)
        self.url = TestData.URL_INVENTORY

    def _get_dynamic_button_locator(self, item_name):
        """Generates a dynamic XPath locator for a specific item's button based on product name"""
        xpath = f"//div[@data-test='inventory-item'][descendant::div[normalize-space()='{item_name}']]//button"
        return (By.XPATH, xpath)

    def get_title(self):
        """Returns the title element of the inventory page"""
        return self.get_text(self._PAGE_TITLE)
    
    def add_item_to_cart(self, item_name):
        # Čekaj da React renderuje inventory items pre svega
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[data-test='inventory-item']")))
        locator = self._get_dynamic_button_locator(item_name)
        self.click(locator)
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[id^='remove']")))

    def remove_item_from_cart(self, item_name):
        # Čekaj da React renderuje inventory items pre svega
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[data-test='inventory-item']")))
        locator = self._get_dynamic_button_locator(item_name)
        self.click(locator)
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[id^='add-to-cart']")))

    def get_button_text(self, item_name):
        """Returns the current text of the Add to Cart/Remove button for a specific item"""
        locator = self._get_dynamic_button_locator(item_name)
        return self.get_text(locator)

    def click_cart_icon(self):
        """Clicks the shopping cart icon and waits for navigation to the cart page"""
        self.click(self._CART_LINK)
        self.wait.until(EC.url_contains("cart.html"))

    def get_cart_badge_count(self):
        """Returns the number shown on the red cart badge"""
        try:
            return self.get_text(self._CART_BADGE)
        except:
            return "0"
    
    def is_item_in_cart(self, item_name):
        try:
            self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[id^='remove']")))
            return True
        except:
            return False
    
    def select_sort_option(self, option_text):
        """Selects a sorting option from the dropdown menu by its visible text"""
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
    
    def wait_for_page_load(self):
        """Waits for all inventory items to be fully rendered by React"""
        self.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "[data-test='inventory-item']")))
    
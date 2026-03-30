from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class InventoryPage(BasePage):
   

    _TITLE = (By.CSS_SELECTOR, "[data-test='title']")  
    _SORT_CONTAINER = (By.CSS_SELECTOR, "[data-test='product-sort-container']")
    _CART_LINK = (By.CSS_SELECTOR, "[data-test='shopping-cart-link']")
    _CART_BADGE = (By.CSS_SELECTOR, "[data-test='shopping-cart-badge']") 
    
    _INVENTORY_ITEM = (By.CSS_SELECTOR, "[data-test='inventory-item']")

    _ITEM_NAME = (By.CSS_SELECTOR, "[data-test='inventory-item-name']")
    _ITEM_PRICE = (By.CSS_SELECTOR, "[data-test='inventory-item-price']")
    _ITEM_DESC = (By.CSS_SELECTOR, "[data-test='inventory-item-desc']")
    _ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, ".btn_inventory") 

    def __init__(self, driver):
        """Initializes the InventoryPage with the WebDriver and sets the page URL"""
        super().__init__(driver)
        self.url = "https://www.saucedemo.com/inventory.html"

    def _get_item_container(self, item_name):
        """Finds and returns the container element for a specific product by name"""
        xpath = f"//div[@data-test='inventory-item'][descendant::div[normalize-space()='{item_name}']]"
        locator = (By.XPATH, xpath)
        return self.find(locator)
    
    def get_title(self):
        """Returns the title element of the inventory page"""
        return self.find(self._TITLE).text
    
    def get_item_name(self, item_name):
        """Returns the text of the product name for a specific item"""
        container = self._get_item_container(item_name)
        return container.find_element(*self._ITEM_NAME).text
    
    def get_item_price(self, item_name):
        """Returns the price text for a specific item"""
        container = self._get_item_container(item_name)
        return container.find_element(*self._ITEM_PRICE).text
    
    def get_item_description(self, item_name):
        """Returns the description text for a specific item"""
        container = self._get_item_container(item_name)
        return container.find_element(*self._ITEM_DESC).text
    
    def add_item_to_cart(self, item_name):
        """Adds a specific item to the shopping cart"""
        container = self._get_item_container(item_name)
        container.find_element(*self._ADD_TO_CART_BUTTON).click()
        
    def remove_item_from_cart(self, item_name):
        """Removes a specific item from the shopping cart"""
        container = self._get_item_container(item_name)
        container.find_element(*self._ADD_TO_CART_BUTTON).click()

    def get_button_text(self, item_name):
        """Returns the current text of the Add to Cart/Remove button for a specific item"""
        container = self._get_item_container(item_name)
        return container.find_element(*self._ADD_TO_CART_BUTTON).text

    def click_cart_icon(self):
        """Clicks on the shopping cart icon to navigate to the cart page"""
        self.click(self._CART_LINK)

    def get_cart_badge_count(self):
        """Returns the number shown on the red cart badge"""
        try:
            return self.get_text(self._CART_BADGE)
        except:
            return "0"
    
    def is_item_in_cart(self, item_name):
        """Checks if a specific item is currently in the cart based on the button text"""
        return self.get_button_text(item_name) == "Remove"
    
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
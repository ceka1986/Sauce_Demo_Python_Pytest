from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class ProductDetailsPage(BasePage):
   
    _BACK_BUTTON = (By.CSS_SELECTOR, "[data-test='back-to-products']")
    _ITEM_NAME = (By.CSS_SELECTOR, "[data-test='inventory-item-name']")
    _ITEM_PRICE = (By.CSS_SELECTOR, "[data-test='inventory-item-price']")
    _ITEM_DESC = (By.CSS_SELECTOR, "[data-test='inventory-item-desc']")
    _ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, ".btn_inventory")

    def __init__(self, driver):
        super().__init__(driver)

    def click_back_to_products(self):
        """Navigates back to the main inventory page"""
        self.click(self._BACK_BUTTON)

    def get_item_name(self):
        """Returns the name of the product from the details page"""
        return self.get_text(self._ITEM_NAME)

    def get_item_price(self):
        """Returns the price of the product from the details page"""
        return self.get_text(self._ITEM_PRICE)
    
    def get_item_description(self):
        """Returns the description of the product from the details page"""
        return self.get_text(self._ITEM_DESC)

    def add_item_to_cart(self):
        """Clicks the add to cart button on the product details page"""
        self.click(self._ADD_TO_CART_BUTTON)

    def get_button_text(self):
        """Returns the current text of the add/remove button"""
        return self.get_text(self._ADD_TO_CART_BUTTON)
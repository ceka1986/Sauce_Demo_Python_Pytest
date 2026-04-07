from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from utils.data import TestData



class CartPage(BasePage):
   
   _PAGE_TITLE = (By.CSS_SELECTOR, "[data-test='title']")
   _CONTINUE_SHOPPING_BUTTON = (By.CSS_SELECTOR, "[data-test='continue-shopping']")
   _CHECKOUT_BUTTON = (By.CSS_SELECTOR, "[data-test='checkout']")
   _CART_BADGE = (By.CSS_SELECTOR, "[data-test='shopping-cart-badge']")
   
   _INVENTORY_ITEM = (By.CSS_SELECTOR, "[data-test='inventory-item']")
   _ITEM_NAME = (By.CSS_SELECTOR,"[data-test='inventory-item-name']")
   _ITEM_QUANTITY = (By.CSS_SELECTOR, "[data-test='item-quantity']")
   _ITEM_PRICE = (By.CSS_SELECTOR, "[data-test='inventory-item-price']")
   _REMOVE_BUTTON = (By.CSS_SELECTOR, "[data-test^='remove-']")

   def __init__(self, driver):
        """Initializes the CartPage with the WebDriver and sets the page URL"""
        super().__init__(driver)
        self.url = TestData.URL_CART
   
   def get_title(self):
      """Returns the page title element"""
      return self.find(self._PAGE_TITLE)
   
   def click_continue_shopping(self):
      """Clicks the 'Continue Shopping' button to return to the inventory page"""
      self.click(self._CONTINUE_SHOPPING_BUTTON)
   
   def click_checkout(self):
      """Clicks the 'Checkout' button to proceed to the information entry page"""
      self.wait_for_text(self._PAGE_TITLE, "Your Cart")
      self.js_click(self._CHECKOUT_BUTTON)
      return self.wait.until(EC.url_contains("checkout-step-one.html"))
   
   def _get_item_container(self, item_name):
        """Finds and returns the container element for a specific product by name"""
        xpath = f"//div[@data-test='inventory-item'][descendant::div[normalize-space()='{item_name}']]"
        locator = (By.XPATH, xpath)
        return self.find(locator)
   
   def remove_item_from_cart(self, item_name):
        """Removes a specific item from the shopping cart"""
        container = self._get_item_container(item_name)
        container.find_element(*self._REMOVE_BUTTON).click()

   def get_all_item_names(self):
        """Returns a list of all item names currently displayed on the page"""
        elements = self.find_all(self._ITEM_NAME)
        return [el.text for el in elements]
   
   def get_item_price(self,item_name):
       """Returns the price text for a specific item in the cart"""
       container = self._get_item_container(item_name)
       return container.find_element(*self._ITEM_PRICE).text
   
   def get_item_quantity(self, item_name):
       """Returns the quantity text for a specific item in the cart"""
       container = self._get_item_container(item_name)
       return container.find_element(*self._ITEM_QUANTITY).text
   
   def get_cart_badge_count(self):
        """Returns the number shown on the red cart badge"""
        try:
            return self.get_text(self._CART_BADGE)
        except:
            return "0"
        
   def is_cart_badge_displayed(self):
    """Checks if the cart badge is currently visible on the page"""
    elements = self.find_all(self._CART_BADGE)
    return len(elements) > 0
   
   def wait_for_page_load(self):
     """Waits for the cart container to be fully rendered"""
     self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[data-test='cart-contents-container']")))


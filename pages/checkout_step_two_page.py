from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from utils.data import TestData



class CheckoutStepTwoPage(BasePage):
   
    _PAGE_TITLE = (By.CSS_SELECTOR, "[data-test='title']")
    _CANCEL_BUTTON = (By.CSS_SELECTOR, "[data-test='cancel']")
    _FINISH_BUTTON = (By.CSS_SELECTOR, "[data-test='finish']")
    _CART_LIST = (By.CSS_SELECTOR, "[data-test='cart-list']")
    _PAYMENT_INFO = (By.CSS_SELECTOR, "[data-test='payment-info-value']")
    _SHIPPING_INFO = (By.CSS_SELECTOR, "[data-test='shipping-info-value']")
    _ITEM_SUBTOTAL = (By.CSS_SELECTOR, "[data-test='subtotal-label']")
    _TAX = (By.CSS_SELECTOR, "[data-test='tax-label']")
    _TOTAL = (By.CSS_SELECTOR, "[data-test='total-label']")

    
    
    def __init__(self, driver):
        """Initializes CheckoutStepTwoPage with the driver and its specific URL"""
        super().__init__(driver)
        self.url = TestData.URL_CHECKOUT_STEP_TWO

    def _extract_price(self, locator):
        """Helper method to extract and convert price text to a float"""
        full_text = self.get_text(locator) 
        price_string = full_text.split('$')[1] 
        return float(price_string)
    
    def get_item_subtotal(self):
        """Returns the subtotal (price without tax)"""
        return self._extract_price(self._ITEM_SUBTOTAL)
    
    def get_tax_amount(self):
        """Returns the tax amount"""
        return self._extract_price(self._TAX)
    
    def get_total_price(self):
        """Returns the final total (subtotal + tax)"""
        return self._extract_price(self._TOTAL)
    
    def get_shipping_info(self):
        """Returns the shipping information value"""
        return self.get_text(self._SHIPPING_INFO)
    
    def get_payment_info(self):
        """Returns the payment information value"""
        return self.get_text(self._PAYMENT_INFO)
    
    def click_cancel_button(self):
        """Clicks the 'Cancel' button to cancel the order and return to the inventory page"""
        self.click(self._CANCEL_BUTTON)

    def click_finish_button(self):
        """Clicks the 'Finish' button to complete the purchase"""
        self.js_click(self._FINISH_BUTTON)
        return self.wait.until(EC.url_contains("checkout-complete.html"))


    def wait_for_page_load(self):
        """Waits for the checkout summary to be fully rendered"""
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[data-test='checkout-summary-container']")))
    



     
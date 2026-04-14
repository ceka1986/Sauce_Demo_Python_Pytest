from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from utils.data import TestData




class CheckoutCompletePage(BasePage):

    _PAGE_TITLE = (By.CSS_SELECTOR, "[data-test='title']")
    _BACK_HOME_BUTTON = (By.CSS_SELECTOR, "[data-test='back-to-products']")
    _COMPLETE_HEADER = (By.CSS_SELECTOR, "[data-test='complete-header']")
    _COMPLETE_TEXT = (By.CSS_SELECTOR, "[data-test='complete-text']")


    def __init__(self, driver):
        """Initializes CheckoutCompletePage with the driver and its specific URL"""
        super().__init__(driver)
        self.url = TestData.URL_CHECKOUT_COMPLETE

    
    def get_page_title(self):
        """Returns the visible text of the page title"""
        return self.get_text(self._PAGE_TITLE)
    
    def get_header_text(self):
        """Returns the success header text"""
        return self.get_text(self._COMPLETE_HEADER)
    
    def get_complete_text(self):
        """Returns the sub-header success message text"""
        return self.get_text(self._COMPLETE_TEXT)
    
    def click_back_home_button(self):
        """Clicks the 'Back Home' button to return to the inventory page"""
        self.click(self._BACK_HOME_BUTTON)

    def wait_for_page_load(self):
        """Waits for the order confirmation to be fully rendered"""
        self.wait.until(EC.element_to_be_clickable(self._BACK_HOME_BUTTON))


    


import logging
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.remote.webdriver import WebDriver

class BasePage:
  

    def __init__(self, driver: WebDriver, timeout: int = 10):
        """Initializes the BasePage with a driver and an explicit wait timeout"""
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)
        self.logger = logging.getLogger(self.__class__.__name__)
        

    def find(self, locator):
        """Waits for an element to be visible on the page and returns it"""
        try:
            return self.wait.until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            self.logger.error(f"Timeout: Element with locator {locator} was not found!")
            raise

    def find_all(self, locator):
        """Finds all elements matching the locator without an explicit wait
        Useful for checking the number of items or verifying an element is NOT present
        """
        return self.driver.find_elements(*locator)

    def click(self, locator):
        """Waits until an element is clickable and then performs a click action"""
        element = self.wait_for_clickable(locator)
        element.click()

    def type(self, locator, text):
        """Finds an element, clears any existing text, and types the new text"""
        element = self.find(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        """Gets the visible text of the element found by the locator"""
        return self.find(locator).text
    
    def wait_for_clickable(self, locator):
        """Explicitly waits for an element to be in a clickable state"""
        return self.wait.until(EC.element_to_be_clickable(locator))
    
    def refresh_page(self):
        """Refreshes the current browser page"""
        self.driver.refresh()

    def js_click(self, locator):
        """Performs a click using JavaScript. Useful for elements blocked by overlays or off-screen."""
        element = self.wait_for_presence(locator)
        self.driver.execute_script("arguments[0].click();", element)

    def wait_for_text(self, locator, text):
        """Waits for a specific text to appear in an element before proceeding"""
        try:
            return self.wait.until(EC.text_to_be_present_in_element(locator, text))
        except TimeoutException:
            self.logger.error(f"Timeout: Text '{text}' not found in element {locator}!")
            raise

    def wait_for_presence(self, locator):
        """Waits only for the element to exist in the DOM"""
        return self.wait.until(EC.presence_of_element_located(locator))
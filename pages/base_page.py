import logging
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException, TimeoutException
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys 

class BasePage:
  

    def __init__(self, driver: WebDriver):
        """Initializes the BasePage with a driver and an explicit wait timeout"""
        self.driver = driver
        timeout =30 if os.environ.get('GITHUB_ACTIONS') else 10
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

    def wait_for_clickable(self, locator):
        """Explicitly waits for an element to be in a clickable state"""
        return self.wait.until(EC.element_to_be_clickable(locator))

    def js_click(self, locator):
        """
        Forces a click using JavaScript after centering the element in the viewport.
        """
        # Ensure element exists in DOM before JS execution
        element = self.wait.until(EC.presence_of_element_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        self.driver.execute_script("arguments[0].click();", element)


    def type(self, locator, text):
        """Finds an element, clears existing text, and types new text"""
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        """Gets the visible text of the element found by the locator"""
        return self.find(locator).text
    
    
    def refresh_page(self):
        """Refreshes the current browser page"""
        self.driver.refresh()


    def wait_for_text(self, locator, text):
        """Waits for a specific text to appear in an element before proceeding"""
        try:
            return self.wait.until(EC.text_to_be_present_in_element(locator, text))
        except TimeoutException:
            self.logger.error(f"Timeout: Text '{text}' not found in element {locator}!")
            raise

    
    def wait_for_button_text(self, locator, text):
        """Waits until the button element contains the expected text,
        Uses 'innerText' attribute instead of '.text' property,
        which is more reliable for button elements in headless Chrome on Linux"""
    
        def check_button_text(driver):
            element = driver.find_element(*locator)
            button_text = element.get_attribute("innerText") or ""
            return text in button_text
        
        try:
            return self.wait.until(check_button_text)
        except TimeoutException:
            self.logger.error(f"Timeout: Button text '{text}' not found in element {locator}!")
            raise

    def wait_for_url(self, url_part):
        """Waits for the current URL to contain the given string"""
        try:
            self.wait.until(EC.url_contains(url_part))
        except TimeoutException:
            self.logger.error(f"Timeout: URL did not contain '{url_part}'! Current URL: {self.driver.current_url}")
            raise

    def clear_session(self):
        self.driver.delete_all_cookies()
        self.driver.execute_script("window.localStorage.clear(); window.sessionStorage.clear();")
 
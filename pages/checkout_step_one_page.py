from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from utils.data import TestData




class CheckoutStepOnePage(BasePage):


    _PAGE_TITLE = (By.CSS_SELECTOR, "[data-test='title']")
    _FIRST_NAME_FIELD = (By.CSS_SELECTOR, "[data-test='firstName']")
    _LAST_NAME_FIELD = (By.CSS_SELECTOR, "[data-test='lastName']")
    _ZIP_POSTAL_CODE_FIELD = (By.CSS_SELECTOR, "[data-test='postalCode']")
    _CANCEL_BUTTON = (By.CSS_SELECTOR, "[data-test='cancel']")
    _CONTINUE_BUTTON = (By.CSS_SELECTOR, "[data-test='continue']")

    _ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")


    def __init__(self, driver):
        """Initializes CheckoutStepOnePage with the driver and its specific URL"""
        super().__init__(driver)
        self.url = TestData.URL_CHECKOUT_STEP_ONE

    def get_page_title(self):
        """Returns the visible text of the page title"""
        return self.get_text(self._PAGE_TITLE)
    
    def enter_first_name(self, first_name):
        """Clicks, clears, types and VERIFIES the input because CI is flaky"""
        element = self.wait.until(EC.element_to_be_clickable(self._FIRST_NAME_FIELD))
        
        # 1. Prvo kliknemo da dobije fokus
        element.click()
        
        # 2. Čistimo i kucamo
        element.clear()
        element.send_keys(first_name)
        
        # 3. PROVERA: Ako je polje i dalje prazno, koristimo JS kao backup
        if element.get_attribute("value") == "":
            self.driver.execute_script("arguments[0].value = arguments[1];", element, first_name)
            self.driver.execute_script("arguments[0].dispatchEvent(new Event('input', { bubbles: true }));", element)

    def enter_last_name(self, last_name):
        """Ensures last name is actually entered"""
        element = self.find(self._LAST_NAME_FIELD)
        element.click()
        element.clear()
        element.send_keys(last_name)
        if element.get_attribute("value") == "":
            self.driver.execute_script("arguments[0].value = arguments[1];", element, last_name)
            self.driver.execute_script("arguments[0].dispatchEvent(new Event('input', { bubbles: true }));", element)

    def enter_postal_code(self, postal_code):
        """Ensures postal code is actually entered"""
        element = self.find(self._ZIP_POSTAL_CODE_FIELD)
        element.click()
        element.clear()
        element.send_keys(postal_code)
        if element.get_attribute("value") == "":
            self.driver.execute_script("arguments[0].value = arguments[1];", element, postal_code)
            self.driver.execute_script("arguments[0].dispatchEvent(new Event('input', { bubbles: true }));", element)

    def fill_in_the_form(self, first_name, last_name, postal_code):
        """Fills out the entire checkout form using the provided data"""
        self.enter_first_name(first_name)
        self.enter_last_name(last_name)
        self.enter_postal_code(postal_code)

    def click_on_continue_button(self):
        """
        Clicks the 'Continue' button using a direct ID-based JavaScript call.
        This bypasses standard Selenium click issues on <input type="submit"> 
        elements in headless CI environments.
        """
        # Ensure the button is present in the DOM
        self.wait.until(EC.presence_of_element_located(self._CONTINUE_BUTTON))
        
        # Direct JS click on the ID 'continue' as seen in the HTML
        self.driver.execute_script("document.getElementById('continue').click();")
        
        # Explicitly wait for the URL to change to the next step
        return self.wait.until(EC.url_contains("checkout-step-two.html"))
        

    def click_on_cancel_button(self):
        """Clicks the 'Cancel' button to return to the Cart page"""
        self.click(self._CANCEL_BUTTON)

    def get_error_message(self):
        """Returns the text content of the error message if it appears"""
        return self.get_text(self._ERROR_MESSAGE)
    
    def is_error_displayed(self):
        """Quickly checks if an error message is visible without waiting"""
        return len(self.find_all(self._ERROR_MESSAGE)) > 0
    
    def wait_for_page_load(self):
        """Waits for the checkout form to be fully rendered"""
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[data-test='checkout-info-container']")))

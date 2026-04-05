from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from utils.data import TestData



class LoginPage(BasePage):

    _USERNAME_FIELD = (By.CSS_SELECTOR, "[data-test='username']")
    _PASSWORD_FIELD = (By.CSS_SELECTOR, "[data-test='password']")
    _LOGIN_BUTTON = (By.CSS_SELECTOR, "[data-test='login-button']")
    _ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")


    def __init__(self, driver):
        super().__init__(driver)
        self.url = TestData.URL_LOGIN

    
    def open(self):
        """Opens the login page URL directly"""
        self.driver.get(self.url)


    def login_with_credentials(self, username, password):
        """
        Main login action 
        Utilizes 'type' and 'click' methods from BasePage for stability
        """
        self.type(self._USERNAME_FIELD, username)
        self.type(self._PASSWORD_FIELD, password)
        self.click(self._LOGIN_BUTTON)


    def get_error_message(self):
        """Retrieves the error message text displayed on failed login"""
        return self.get_text(self._ERROR_MESSAGE)


    def is_login_button_displayed(self):
        """Used to verify the user is on the login page (e.g., after Logout)"""
        return self.find(self._LOGIN_BUTTON).is_displayed()
    
    def is_at(self):
        """Checks if the browser is currently on the expected page URL"""
        return self.driver.current_url.rstrip('/') == self.url.rstrip('/')
    
    def wait_for_page_load(self):
        """Waits for the login form to be fully rendered"""
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[data-test='login-container']")))


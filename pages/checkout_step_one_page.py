from pages.base_page import BasePage
from selenium.webdriver.remote.webdriver import WebDriver


class CheckoutStepOnePage(BasePage):


    

    def __init__(self, driver):
        """Initializes CheckoutStepOnePage with the driver and its specific URL"""
        super().__init__(driver)
        self.url = "https://www.saucedemo.com/checkout-step-one.html"
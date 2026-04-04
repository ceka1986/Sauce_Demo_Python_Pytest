import os

from pages.cart_page import CartPage
from pages.checkout_complete_page import CheckoutCompletePage
from pages.checkout_step_one_page import CheckoutStepOnePage
from pages.checkout_step_two_page import CheckoutStepTwoPage
from pages.components.sidebar import Sidebar
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
from pages.product_details_page import ProductDetailsPage
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="function")
def driver():
    """Sets up the Chrome driver with essential options and ensures clean teardown"""
    chrome_options = Options()
    chrome_options.add_argument("--headless") 
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--window-size=1920,1080")

    chrome_options.add_argument("--disable-gpu")  
    chrome_options.add_argument("--remote-allow-origins=*")
    
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    #driver.maximize_window()
    
    yield driver
    driver.quit()

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        mode = "a" if os.path.exists("failures.txt") else "w"
        try:
            driver = item.funcargs['driver']
            
            if not os.path.exists("screenshots"):
                os.makedirs("screenshots")
            
            screenshot_name = f"screenshots/{item.name}.png"
            driver.save_screenshot(screenshot_name)
            print(f"\nScreenshot saved to: {screenshot_name}")
        except Exception as e:
            print(f"\nFail to take screenshot: {e}")


@pytest.fixture
def login_page(driver) -> LoginPage: return LoginPage(driver)

@pytest.fixture
def inventory_page(driver) -> InventoryPage: return InventoryPage(driver)

@pytest.fixture
def product_details_page(driver) -> ProductDetailsPage: return ProductDetailsPage(driver)

@pytest.fixture
def cart_page(driver) -> CartPage: return CartPage(driver)

@pytest.fixture
def sidebar(driver) -> Sidebar: return Sidebar(driver)

@pytest.fixture
def checkout_step_one_page(driver) -> CheckoutStepOnePage: return CheckoutStepOnePage(driver)

@pytest.fixture
def checkout_step_two_page(driver) -> CheckoutStepTwoPage: return CheckoutStepTwoPage(driver)

@pytest.fixture
def checkout_complete_page(driver) -> CheckoutCompletePage: return CheckoutCompletePage(driver)
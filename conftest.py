import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from selenium.webdriver.remote.webdriver import WebDriver


@pytest.fixture(scope="function")
def driver():
    # Automatski skida i pokreće Chrome drajver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    
    yield driver
    
    driver.quit()

# Fixtures za stranice (da ih ne praviš ručno u svakom testu)
@pytest.fixture
def login_page(driver): return LoginPage(driver)

@pytest.fixture
def inventory_page(driver): return InventoryPage(driver)

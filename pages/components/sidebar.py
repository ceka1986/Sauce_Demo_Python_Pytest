from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class Sidebar(BasePage):
    
    _MENU_BUTTON = (By.ID, "react-burger-menu-btn")
    _CLOSE_BUTTON = (By.ID, "react-burger-cross-btn")
    _LOGOUT_LINK = (By.ID, "logout_sidebar_link")
    _RESET_APP_STATE = (By.ID, "reset_sidebar_link")
    _ALL_ITEMS = (By.ID, "inventory_sidebar_link")

    def __init__(self, driver: WebDriver):
        """Initializes the Sidebar component"""
        super().__init__(driver)

    def open_menu(self):
        """Opens the burger menu and waits for it to be ready"""
        self.click(self._MENU_BUTTON)
        self.wait_for_clickable(self._CLOSE_BUTTON)

    def logout(self):
        """Opens the menu and performs the logout action"""
        self.open_menu()
        self.wait_for_clickable(self._LOGOUT_LINK)
        self.click(self._LOGOUT_LINK)
    
    def reset_app_state(self):
        """Opens the menu and resets the application state """
        self.open_menu()
        self.click(self._RESET_APP_STATE)

    def show_all_items(self):
        """Opens the menu and navigates back to the inventory page"""
        self.open_menu()
        self.click(self._ALL_ITEMS)

    def close_menu(self):
        """Clicks the 'X' button to close the sidebar menu"""
        self.click(self._CLOSE_BUTTON)
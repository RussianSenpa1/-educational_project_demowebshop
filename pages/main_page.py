from selenium.webdriver.common.by import By
from .base_page import BasePage
from .locators import MainPageLocators

class MainPage(BasePage):
    def should_be_register_button(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_SELECTOR), "Register button is not presented"

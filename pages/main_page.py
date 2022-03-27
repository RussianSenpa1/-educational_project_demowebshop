from .base_page import BasePage
from .locators import MainPageLocators


class MainPage(BasePage):
    def should_be_register_button(self):
        assert self.is_element_present(*MainPageLocators.REGISTER_SELECTOR), "Register button is not presented"

    def should_be_login_button(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_SELECTOR), "Login button is not presented"

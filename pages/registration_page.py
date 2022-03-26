from .base_page import BasePage
from .locators import RegisterPageLocators


class RegistrationPage(BasePage):
    def should_be_register_url(self):
        assert "register" in self.url, "URL is not register"

    def should_be_firstname_field(self):
        assert self.is_element_present(*RegisterPageLocators.FIRST_NAME_SELECTOR), "First_name field is not presented"
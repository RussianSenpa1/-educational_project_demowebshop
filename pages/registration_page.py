from .base_page import BasePage
from .locators import RegisterPageLocators


class RegistrationPage(BasePage):
    def should_be_register_url(self):
        assert "register" in self.url, "URL is not register"

    def should_be_firstname_field(self):
        assert self.is_element_present(*RegisterPageLocators.FIRST_NAME_SELECTOR), "FirstName field is not presented"

    def should_be_lastname_field(self):
        assert self.is_element_present(*RegisterPageLocators.LAST_NAME_SELECTOR), "LastName field is not presented"

    def should_be_email_field(self):
        assert self.is_element_present(*RegisterPageLocators.EMAIL_REGISTER_SELECTOR), "Email field is not presented"

    def should_be_password_field(self):
        assert self.is_element_present(
            *RegisterPageLocators.PASSWORD_REGISTER_SELECTOR), "Password field is not presented"

    def should_be_confirm_password_field(self):
        assert self.is_element_present(
            *RegisterPageLocators.CONFIRMPASSWORD_REGISTER_SELECTOR), "Confirm Password field is not presented"

    def should_be_register_button(self):
        assert self.is_element_present(
            *RegisterPageLocators.REGISTER_BUTTON_SELECTOR), "Register Button is not presented"

    def should_be_gender_male_female(self):
        assert self.is_element_present(
            *RegisterPageLocators.GENDER_MALE_SELECTOR) and self.is_element_present(
            *RegisterPageLocators.GENDER_FEMALE_SELECTOR), "Gender checkboxs is not presented"

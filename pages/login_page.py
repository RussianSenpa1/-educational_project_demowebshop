from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_url(self):
        assert "login" in self.url, "URL is not login"

    def should_be_email_field(self):
        assert self.is_element_present(*LoginPageLocators.EMAIL_LOGIN_SELETOR), "Email field is not presented in login page"

    def should_be_password_field(self):
        assert self.is_element_present(
            *LoginPageLocators.PASSWORD_LOGIN_SELECTOR), "Password field is not presented in login page"

    def should_be_login_button(self):
        assert self.is_element_present(
            *LoginPageLocators.LOGINBUTTON_LOGIN_SELECTOR), "Login button is not presented in login page"
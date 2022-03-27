from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_url(self):
        assert "login" in self.url, "URL is not login"

    def should_be_email_field(self):
        assert self.is_element_present(
            *LoginPageLocators.EMAIL_LOGIN_SELETOR), "Email field is not presented in login page"

    def should_be_password_field(self):
        assert self.is_element_present(
            *LoginPageLocators.PASSWORD_LOGIN_SELECTOR), "Password field is not presented in login page"

    def should_be_login_button(self):
        assert self.is_element_present(
            *LoginPageLocators.LOGINBUTTON_LOGIN_SELECTOR), "Login button is not presented in login page"

    def login_user(self, email, password):
        email_field = self.browser.find_element(*LoginPageLocators.EMAIL_LOGIN_SELETOR)
        email_field.send_keys(str(email))
        password_field = self.browser.find_element(*LoginPageLocators.PASSWORD_LOGIN_SELECTOR)
        password_field.send_keys(str(password))
        register = self.browser.find_element(*LoginPageLocators.LOGINBUTTON_LOGIN_SELECTOR)
        register.click()

    def should_be_login_account(self, email):
        account_email = (self.browser.find_element(*LoginPageLocators.ACCOUNT_SELECTOR)).text
        assert account_email == email, "Error during login"

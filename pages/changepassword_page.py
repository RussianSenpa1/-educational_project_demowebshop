from .base_page import BasePage
from .locators import PasswordChangePageLocators


class PasswordChangePage(BasePage):
    def should_be_field_change_password(self):
        assert self.is_element_present(
            *PasswordChangePageLocators.OLD_PASSWORD_SELECTOR) and self.is_element_present(
            *PasswordChangePageLocators.NEW_PASSWORD_SELECTOR) and self.is_element_present(
            *PasswordChangePageLocators.CONFIRMNEW_PASSWORD_SELECTOR) and self.is_element_present(
            *PasswordChangePageLocators.PASSWORD_CHANGE_BUTTON_SELECTOR), "Full field is not presented in Password change page"

    def new_password_data(self, password):
        old_password_field = self.browser.find_element(*PasswordChangePageLocators.OLD_PASSWORD_SELECTOR)
        old_password_field.send_keys(str(password))
        new_password = self.browser.find_element(*PasswordChangePageLocators.NEW_PASSWORD_SELECTOR)
        new_password.send_keys(*PasswordChangePageLocators.NEW_PASSWORD)
        confirm_new_password = self.browser.find_element(*PasswordChangePageLocators.CONFIRMNEW_PASSWORD_SELECTOR)
        confirm_new_password.send_keys(*PasswordChangePageLocators.NEW_PASSWORD)
        register = self.browser.find_element(*PasswordChangePageLocators.PASSWORD_CHANGE_BUTTON_SELECTOR)
        register.click()

    def should_be_change_password_message(self):
        message = (self.browser.find_element(*PasswordChangePageLocators.REZULT_SELECTOR)).text
        message_true = PasswordChangePageLocators.MESSAGE_TRUE
        assert message_true in message, "Text PasswordChange message is false"

    def should_be_change_password(self):
        assert self.is_element_present(
            *PasswordChangePageLocators.REZULT_SELECTOR), "Failed to change password"

from selenium.common.exceptions import NoSuchElementException
from .locators import MainPageLocators, LoginPageLocators, PasswordChangePageLocators


class BasePage():
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def is_element_present(self, how, what):  # Метод проверки элемента на странице
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True

    def is_not_element_present(self, how, what):  # Метод проверки отсутствия элемента на странице
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return True
        return False

    def open(self):  # Метод открытия страницы
        self.browser.get(self.url)

    def go_to_register_page(self):
        link = self.browser.find_element(*MainPageLocators.REGISTER_SELECTOR)
        link.click()

    def go_to_login_page(self):
        link = self.browser.find_element(*MainPageLocators.LOGIN_SELECTOR)
        link.click()

    def go_to_user_page(self):
        link = self.browser.find_element(*LoginPageLocators.ACCOUNT_SELECTOR)
        link.click()

    def go_to_changepassword_page(self):
        link = self.browser.find_element(*PasswordChangePageLocators.PASSWORD_CHANGE_BUTTON_CUSTOMER_SELECTOR)
        link.click()

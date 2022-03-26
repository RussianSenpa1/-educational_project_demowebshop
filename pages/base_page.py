from selenium.common.exceptions import NoSuchElementException
from .locators import MainPageLocators

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

    def open(self):  # Метод открытия страницы
        self.browser.get(self.url)

    def go_to_register_page(self):
        link = self.browser.find_element(*MainPageLocators.LOGIN_SELECTOR)
        link.click()

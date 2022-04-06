import pytest

from .pages.registration_page import RegistrationPage
from .pages.locators import LinksLocators
from .pages.login_page import LoginPage


def test_should_see_login_email_field(browser):  # Проверка есть ли поле ввода email
    link = LinksLocators.LOGIN_PAGES_LINK
    page = LoginPage(browser, link)
    page.open()
    page.should_be_email_field()


def test_should_see_login_password_field(browser):  # Проверка есть ли поле ввода пароля
    link = LinksLocators.LOGIN_PAGES_LINK
    page = LoginPage(browser, link)
    page.open()
    page.should_be_password_field()


def test_should_see_login_login_button(browser):  # Проверка есть ли кнопка логина
    link = LinksLocators.LOGIN_PAGES_LINK
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_button()


class TestLoginUser():
    @pytest.fixture
    def register(self, browser):
        link = LinksLocators.REGISTER_PAGES_LINK
        page = RegistrationPage(browser, link)
        page.open()
        first_name, last_name, email, password = page.registration_data()
        page.new_user_register(first_name=first_name, last_name=last_name, email=email, password=password)
        return email, password

    @pytest.mark.main_test
    def test_login_user(self, browser, register):
        link = LinksLocators.LOGIN_PAGES_LINK
        page = LoginPage(browser, link)
        page.open()
        page.login_user(email=register[0], password=register[1])
        page.should_be_login_account(email=register[0])

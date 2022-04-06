import pytest

from .pages.changepassword_page import PasswordChangePage
from .pages.locators import LinksLocators
from .pages.registration_page import RegistrationPage


def test_changepassword_field(browser):  # Проверка все ли поля есть на странице смены пароля
    link = LinksLocators.REGISTER_PAGES_LINK
    page = RegistrationPage(browser, link)
    page.open()
    first_name, last_name, email, password = page.registration_data()
    page.new_user_register(first_name=first_name, last_name=last_name, email=email, password=password)
    link = LinksLocators.PASSWORDCHANGE_PAGES_LINK
    page = PasswordChangePage(browser, link)
    page.open()
    page.should_be_field_change_password()

@pytest.mark.main_test
def test_changepassword_new_password(browser):  # Проверка смены пароля
    link = LinksLocators.REGISTER_PAGES_LINK
    page = RegistrationPage(browser, link)
    page.open()
    first_name, last_name, email, password = page.registration_data()
    page.new_user_register(first_name=first_name, last_name=last_name, email=email, password=password)
    link = LinksLocators.PASSWORDCHANGE_PAGES_LINK
    page = PasswordChangePage(browser, link)
    page.open()
    page.new_password_data(password=password)
    page.should_be_change_password()

@pytest.mark.main_test
def test_changepassword_new_password_message(browser):  # Проверка текста сообщения при смене пароля
    link = LinksLocators.REGISTER_PAGES_LINK
    page = RegistrationPage(browser, link)
    page.open()
    first_name, last_name, email, password = page.registration_data()
    page.new_user_register(first_name=first_name, last_name=last_name, email=email, password=password)
    link = LinksLocators.PASSWORDCHANGE_PAGES_LINK
    page = PasswordChangePage(browser, link)
    page.open()
    page.new_password_data(password=password)
    page.should_be_change_password_message()

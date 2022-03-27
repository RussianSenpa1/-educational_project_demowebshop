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
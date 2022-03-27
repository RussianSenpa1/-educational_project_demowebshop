from .pages.login_page import LoginPage
from .pages.registration_page import RegistrationPage
from .pages.locators import LinksLocators
from .pages.main_page import MainPage


def test_should_see_register_button(browser):  # Проверка есть ли кнопка регистрации на странице
    link = LinksLocators.MAIN_PAGES_LINK
    page = MainPage(browser, link)
    page.open()
    page.should_be_register_button()


def test_should_see_register_url(browser):  # Содержит ли url - register при переходе по кнопке "Register"
    link = LinksLocators.MAIN_PAGES_LINK
    page = MainPage(browser, link)
    page.open()
    page.go_to_register_page()
    register_page = RegistrationPage(browser, browser.current_url)
    register_page.should_be_register_url()


def test_should_see_login_button(browser):  # Проверка есть ли кнопка регистрации на странице
    link = LinksLocators.MAIN_PAGES_LINK
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_button()


def test_should_see_login_url(browser):  # Содержит ли url - register при переходе по кнопке "Register"
    link = LinksLocators.MAIN_PAGES_LINK
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_url()

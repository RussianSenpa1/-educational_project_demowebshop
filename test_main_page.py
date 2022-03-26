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
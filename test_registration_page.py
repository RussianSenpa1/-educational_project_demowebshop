from .pages.locators import LinksLocators
from .pages.registration_page import RegistrationPage

def test_should_see_register_firstname_field(browser):  # Проверка есть ли поле ввода имени
    link = LinksLocators.REGISTER_PAGES_LINK
    page = RegistrationPage(browser, link)
    page.open()
    page.should_be_firstname_field()

def test_should_see_register_lastname_field(browser):  # Проверка есть ли поле ввода фамилии
    link = LinksLocators.REGISTER_PAGES_LINK
    page = RegistrationPage(browser, link)
    page.open()
    page.should_be_lastname_field()

def test_should_see_register_email_field(browser):  # Проверка есть ли поле ввода email
    link = LinksLocators.REGISTER_PAGES_LINK
    page = RegistrationPage(browser, link)
    page.open()
    page.should_be_email_field()
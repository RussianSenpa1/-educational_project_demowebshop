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


def test_should_see_register_password_field(browser):  # Проверка есть ли поле ввода пароля
    link = LinksLocators.REGISTER_PAGES_LINK
    page = RegistrationPage(browser, link)
    page.open()
    page.should_be_password_field()


def test_should_see_register_confirm_password_field(browser):  # Проверка есть ли поле ввода подтверждения пароля
    link = LinksLocators.REGISTER_PAGES_LINK
    page = RegistrationPage(browser, link)
    page.open()
    page.should_be_confirm_password_field()


def test_should_see_register_button(browser):  # Проверка есть ли кнопка регистрации
    link = LinksLocators.REGISTER_PAGES_LINK
    page = RegistrationPage(browser, link)
    page.open()
    page.should_be_register_button()


def test_should_see_gender_checkboxs(browser):  # Проверка есть ли чекбоксы пола
    link = LinksLocators.REGISTER_PAGES_LINK
    page = RegistrationPage(browser, link)
    page.open()
    page.should_be_gender_male_female()


def test_go_to_registration(browser):  # Проверка регистрации
    link = LinksLocators.REGISTER_PAGES_LINK
    page = RegistrationPage(browser, link)
    page.open()
    first_name, last_name, email, password = page.registration_data()
    page.new_user_register(first_name=first_name, last_name=last_name, email=email, password=password)
    page.should_be_registration()

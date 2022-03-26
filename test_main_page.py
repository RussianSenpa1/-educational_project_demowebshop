from .pages.locators import LinksLocators
from .pages.main_page import MainPage


def test_should_see_register_button(browser):  # Проверка есть ли кнопка регистрации на странице
    link = LinksLocators.MAIN_PAGES_LINK
    page = MainPage(browser, link)
    page.open()
    page.should_be_register_button()
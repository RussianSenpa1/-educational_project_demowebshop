from .pages.main_page import MainPage


def test_should_see_register_button(browser):  # Проверка есть ли кнопка регистрации на странице
    link = "http://demowebshop.tricentis.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_register_button()
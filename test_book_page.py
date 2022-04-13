import pytest
from selenium.webdriver.common.by import By

from .pages.book_page import BookPage
from .pages.locators import LinksLocators, TestAccount
from .pages.login_page import LoginPage


@pytest.fixture  # Фикстура очишения корзины после теста
def clear_account(browser):
    yield browser
    browser.get('http://demowebshop.tricentis.com/cart')
    books = browser.find_element(By.XPATH, "//*[@class='cart-item-row']").find_elements(By.XPATH,
                                                                                        "//*[@type='checkbox']")
    for i in books:
        i.click()
    clear_button = browser.find_element(By.XPATH, "//*[@class='button-2 update-cart-button']")
    clear_button.click()


@pytest.mark.parametrize('link_book', ["http://demowebshop.tricentis.com/computing-and-internet"])
def test_should_be_buy_button(browser, link_book):  # Тест на наличие кнопки покупки на странице книги
    link = LinksLocators.LOGIN_PAGES_LINK
    login = TestAccount.LOGIN
    password = TestAccount.PASSWORD
    page = LoginPage(browser, link)
    page.open()
    page.login_user(email=login, password=password)
    page = BookPage(browser, link_book)
    page.open()
    page.should_be_buy_button()


@pytest.mark.main_test
@pytest.mark.usefixtures("clear_account")
@pytest.mark.parametrize('link_book', ["http://demowebshop.tricentis.com/computing-and-internet"])
def test_should_be_massenge_buy_book(browser, link_book):  # Тест на текст всплывающего сообщения при добавлении книги
    link = LinksLocators.LOGIN_PAGES_LINK
    login = TestAccount.LOGIN
    password = TestAccount.PASSWORD
    page = LoginPage(browser, link)
    page.open()
    page.login_user(email=login, password=password)
    page = BookPage(browser, link_book)
    page.open()
    page.should_be_buy_massenge()

import pytest
from selenium.webdriver.common.by import By

from .pages.books_pages import BooksPage
from .pages.locators import LinksLocators, TestAccount, LoginPageLocators

@pytest.fixture  # Фикстура авторизации на аккаунт
def authorization_account(browser):
    browser.get(LinksLocators.LOGIN_PAGES_LINK)
    email_field = browser.find_element(*LoginPageLocators.EMAIL_LOGIN_SELETOR)
    email_field.send_keys(*TestAccount.LOGIN)
    password_field = browser.find_element(*LoginPageLocators.PASSWORD_LOGIN_SELECTOR)
    password_field.send_keys(*TestAccount.PASSWORD)
    register = browser.find_element(*LoginPageLocators.LOGINBUTTON_LOGIN_SELECTOR)
    register.click()

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

def test_should_be_buy_button(browser):  # Тест на наличие книг на странице
    link_books = LinksLocators.BOOKS_PAGES_LINK
    page = BooksPage(browser, link_books)
    page.open()
    page.should_be_books()


@pytest.mark.main_test
@pytest.mark.usefixtures("authorization_account")
@pytest.mark.usefixtures("clear_account")
def test_should_be_massenge_buy_book(browser):  # Тест на текст всплывающего сообщения при добавлении книги
    link_books = LinksLocators.BOOKS_PAGES_LINK
    page = BooksPage(browser, link_books)
    page.open()
    page.should_be_buy_massenge_baooks_page()
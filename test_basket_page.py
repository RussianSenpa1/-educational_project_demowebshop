import pytest

from .pages.basket_page import BasketPage
from .pages.locators import LinksLocators, TestAccount, LoginPageLocators, BooksPageLocators, BasketPageLocators


@pytest.fixture  # Фикстура авторизации на аккаунт, проверики и удаления с корзины товара
def authorization_account(browser):
    browser.get(LinksLocators.LOGIN_PAGES_LINK)
    email_field = browser.find_element(*LoginPageLocators.EMAIL_LOGIN_SELETOR)
    email_field.send_keys(*TestAccount.LOGIN)
    password_field = browser.find_element(*LoginPageLocators.PASSWORD_LOGIN_SELECTOR)
    password_field.send_keys(*TestAccount.PASSWORD)
    register = browser.find_element(*LoginPageLocators.LOGINBUTTON_LOGIN_SELECTOR)
    register.click()
    browser.get(LinksLocators.BASKET_PAGES_LINK)
    if browser.find_element(*BasketPageLocators.BOOKS_BASKET_SELECTOR).find_elements(
            *BasketPageLocators.CHECK_BOX_BOOKS) == True:
        books = browser.find_element(*BasketPageLocators.BOOKS_BASKET_SELECTOR).find_elements(
            *BasketPageLocators.CHECK_BOX_BOOKS)
        if len(books) != 0:
            for i in books:
                i.click()
            clear_button = browser.find_element(*BasketPageLocators.CLEAR_BUTTON_SELECTOR)
            clear_button.click()


@pytest.fixture  # Фикстура добавления одной книги в корзину
def buy_one_book(browser):
    browser.get(LinksLocators.BOOKS_PAGES_LINK)
    books = browser.find_element(*BooksPageLocators.BOOKS_CONTEINER_SELECTOR).find_elements(
        *BooksPageLocators.BOOKS_BOOK_SELECTOR)
    for i in books:
        if i.find_element(*BooksPageLocators.BUTTON_BUY_BOOKS_SELECTOR):
            button_bay = i.find_element(*BooksPageLocators.BUTTON_BUY_BOOKS_SELECTOR)
            button_bay.click()
            break


@pytest.fixture  # Фикстура очишения корзины после теста
def clear_account(browser):
    yield browser
    try:
        browser.get(LinksLocators.BASKET_PAGES_LINK)
        books = browser.find_element(*BasketPageLocators.BOOKS_BASKET_SELECTOR).find_elements(
            *BasketPageLocators.CHECK_BOX_BOOKS)
        if len(books) != 0:
            for i in books:
                i.click()
            clear_button = browser.find_element(*BasketPageLocators.CLEAR_BUTTON_SELECTOR)
            clear_button.click()
    except:
        pass


@pytest.mark.usefixtures("authorization_account")
@pytest.mark.usefixtures("buy_one_book")
@pytest.mark.usefixtures("clear_account")
def test_should_be_price_book(browser):  # Тест соответствует ли цены книги, суб тотал книги, тотал цена
    link = LinksLocators.BASKET_PAGES_LINK
    page = BasketPage(browser, link)
    page.open()
    page.should_be_price()


@pytest.mark.main_test
@pytest.mark.usefixtures("authorization_account")
@pytest.mark.usefixtures("buy_one_book")
@pytest.mark.usefixtures("clear_account")
def test_should_be_price_book_change(browser):  # Тест соответствует ли цены при изменении кол-ва книг в корзине
    link = LinksLocators.BASKET_PAGES_LINK
    page = BasketPage(browser, link)
    page.open()
    page.should_be_price_change()


@pytest.mark.main_test
@pytest.mark.usefixtures("authorization_account")
@pytest.mark.usefixtures("buy_one_book")
@pytest.mark.usefixtures("clear_account")
def test_should_be_zero_books(browser):  # Тест при изменении кол-ва книг на 0
    link = LinksLocators.BASKET_PAGES_LINK
    page = BasketPage(browser, link)
    page.open()
    page.should_be_zero_books()


@pytest.mark.main_test
@pytest.mark.usefixtures("authorization_account")
@pytest.mark.usefixtures("buy_one_book")
@pytest.mark.usefixtures("clear_account")
def test_should_be_a_lote_of_books(browser):  # Тест есть ли сообщение при превышении макс числа книг
    link = LinksLocators.BASKET_PAGES_LINK
    page = BasketPage(browser, link)
    page.open()
    page.should_be_a_lote_of_books()


@pytest.mark.usefixtures("authorization_account")
@pytest.mark.usefixtures("buy_one_book")
@pytest.mark.usefixtures("clear_account")
def test_should_be_ten_thousand_books(browser):  # Тест появляется ли сообщение ошибки при 10000 книг
    link = LinksLocators.BASKET_PAGES_LINK
    page = BasketPage(browser, link)
    page.open()
    page.should_be_ten_thousand_books()

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage
from .locators import BooksPageLocators


class BooksPage(BasePage):

    def should_be_books(self):
        books = self.browser.find_element(*BooksPageLocators.BOOKS_CONTEINER_SELECTOR).find_elements(
            *BooksPageLocators.BOOKS_BOOK_SELECTOR)
        len_books = len(books)
        assert len_books != 0, "Books is not the page"

    def should_be_buy_massenge_baooks_page(self):
        books = self.browser.find_element(*BooksPageLocators.BOOKS_CONTEINER_SELECTOR).find_elements(
            *BooksPageLocators.BOOKS_BOOK_SELECTOR)
        for i in books:
            if i.find_element(*BooksPageLocators.BUTTON_BUY_BOOKS_SELECTOR):
                button_bay = i.find_element(*BooksPageLocators.BUTTON_BUY_BOOKS_SELECTOR)
                button_bay.click()
                break
        massenge = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located(BooksPageLocators.MASSENGE_BUY_BOOKS_SELECTOR))
        assert 'The product has been added to your' in massenge.text, "The message is wrong"

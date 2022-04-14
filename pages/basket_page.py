from random import randrange
from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def should_be_price(self):
        price_product = self.browser.find_element(*BasketPageLocators.PRICE_PRODUCT_SELECTOR)
        price_product_subtotal = self.browser.find_element(*BasketPageLocators.PRICE_PRODUCT_SUBTOTAL_SELECTOR)
        price_total = self.browser.find_element(*BasketPageLocators.PRICE_TOTAL_SELECTOR)
        assert price_product.text == price_product_subtotal.text == price_total.text, "Prices do not match"

    def should_be_price_change(self):
        amount_books_field = self.browser.find_element(*BasketPageLocators.FIELD_AMOUNT_BOOKS_SELECTOR)
        amount_books_field.click()
        amount_books_field.clear()
        random_amount_books = randrange(1, 9999, 1)
        amount_books_field.send_keys(str(random_amount_books))
        button_update = self.browser.find_element(*BasketPageLocators.CLEAR_BUTTON_SELECTOR)
        button_update.click()
        price_product_subtotal = self.browser.find_element(*BasketPageLocators.PRICE_PRODUCT_SUBTOTAL_SELECTOR)
        price_total = self.browser.find_element(*BasketPageLocators.PRICE_TOTAL_SELECTOR)
        assert price_product_subtotal.text == price_total.text, "Prices are not equal when changing"

    def should_be_zero_books(self):
        amount_books_field = self.browser.find_element(*BasketPageLocators.FIELD_AMOUNT_BOOKS_SELECTOR)
        amount_books_field.click()
        amount_books_field.clear()
        amount_books = 0
        amount_books_field.send_keys(str(amount_books))
        button_update = self.browser.find_element(*BasketPageLocators.CLEAR_BUTTON_SELECTOR)
        button_update.click()
        assert self.is_not_element_present(*BasketPageLocators.BOOKS_BASKET_SELECTOR), "Book left on the page"

    def should_be_a_lote_of_books(self):
        amount_books_field = self.browser.find_element(*BasketPageLocators.FIELD_AMOUNT_BOOKS_SELECTOR)
        amount_books_field.click()
        amount_books_field.clear()
        amount_books = 10001
        amount_books_field.send_keys(str(amount_books))
        button_update = self.browser.find_element(*BasketPageLocators.CLEAR_BUTTON_SELECTOR)
        button_update.click()
        assert self.is_element_present(*BasketPageLocators.MASSENGE_FIELD_SELECTOR), "Massenge field is not on the page"

    def should_be_ten_thousand_books(self):
        amount_books_field = self.browser.find_element(*BasketPageLocators.FIELD_AMOUNT_BOOKS_SELECTOR)
        amount_books_field.click()
        amount_books_field.clear()
        amount_books = 10000
        amount_books_field.send_keys(str(amount_books))
        button_update = self.browser.find_element(*BasketPageLocators.CLEAR_BUTTON_SELECTOR)
        button_update.click()
        assert self.is_not_element_present(
            *BasketPageLocators.MASSENGE_FIELD_SELECTOR), "Massenge field is on the page of ten thousand books"

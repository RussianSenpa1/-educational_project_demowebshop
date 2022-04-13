from .base_page import BasePage
from .locators import BookPageLocators

class BookPage(BasePage):
    def should_be_buy_button(self):
        assert self.is_element_present(*BookPageLocators.BUTTON_BUY_SELECTOR), "Buy button is not presented"

    def should_be_buy_massenge(self):
        button = self.browser.find_element(*BookPageLocators.BUTTON_BUY_SELECTOR)
        button.click()
        massenge = self.browser.find_element(*BookPageLocators.MASSENGE_BUY_BOOK_SELECTOR)
        assert 'The product has been added to your' in massenge.text, "The message is wrong"
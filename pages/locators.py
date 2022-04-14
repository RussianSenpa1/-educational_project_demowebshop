from selenium.webdriver.common.by import By


class LinksLocators():
    MAIN_PAGES_LINK = 'http://demowebshop.tricentis.com/'
    REGISTER_PAGES_LINK = 'http://demowebshop.tricentis.com/register'
    LOGIN_PAGES_LINK = 'http://demowebshop.tricentis.com/login'
    PASSWORDCHANGE_PAGES_LINK = 'http://demowebshop.tricentis.com/customer/changepassword'
    BOOK_PAGES_LINK = 'http://demowebshop.tricentis.com/health'
    BOOKS_PAGES_LINK = 'http://demowebshop.tricentis.com/books'

class TestAccount():
    LOGIN = 'bloodtwix90@mail.ru'
    PASSWORD = '123321qQq'

class MainPageLocators():
    REGISTER_SELECTOR = (By.XPATH, "//a[@class='ico-register']")
    LOGIN_SELECTOR = (By.XPATH, "//a[@class='ico-login']")


class RegisterPageLocators():
    FIRST_NAME_SELECTOR = (By.XPATH, "//*[@id='FirstName']")
    LAST_NAME_SELECTOR = (By.XPATH, "//*[@id='LastName']")
    EMAIL_REGISTER_SELECTOR = (By.XPATH, "//*[@id='Email']")
    PASSWORD_REGISTER_SELECTOR = (By.XPATH, "//*[@id='Password']")
    CONFIRMPASSWORD_REGISTER_SELECTOR = (By.XPATH, "//*[@id='ConfirmPassword']")
    REGISTER_BUTTON_SELECTOR = (By.XPATH, "//*[@id='register-button']")
    GENDER_MALE_SELECTOR = (By.XPATH, "//*[@id='gender-male']")
    GENDER_FEMALE_SELECTOR = (By.XPATH, "//*[@id='gender-female']")
    REZULT_MASSAGE_REGISTR_SELECTOR = (By.XPATH, "//*[@class='result']")
    REZULT_BUTTON_REGISTR_SELECTOR = (By.XPATH, "//*[@class='button-1 register-continue-button']")


class LoginPageLocators():
    EMAIL_LOGIN_SELETOR = (By.XPATH, "//*[@id='Email']")
    PASSWORD_LOGIN_SELECTOR = (By.XPATH, "//*[@id='Password']")
    LOGINBUTTON_LOGIN_SELECTOR = (By.XPATH, "//*[@class='button-1 login-button']")
    ACCOUNT_SELECTOR = (By.XPATH, "//*[@class='account']")


class PasswordChangePageLocators():
    PASSWORD_CHANGE_BUTTON_CUSTOMER_SELECTOR = (By.XPATH, "//*[@class='active']")
    OLD_PASSWORD_SELECTOR = (By.XPATH, "//*[@id='OldPassword']")
    NEW_PASSWORD_SELECTOR = (By.XPATH, "//*[@id='NewPassword']")
    CONFIRMNEW_PASSWORD_SELECTOR = (By.XPATH, "//*[@id='ConfirmNewPassword']")
    PASSWORD_CHANGE_BUTTON_SELECTOR = (By.XPATH, "//*[@class='button-1 change-password-button']")
    REZULT_SELECTOR = (By.XPATH, "//*[@class='result']")
    MESSAGE_TRUE = 'Password was changed'
    NEW_PASSWORD = '123321qQq'


class BookPageLocators():
    BUTTON_BUY_SELECTOR = (By.XPATH, "//*[@class='button-1 add-to-cart-button']")
    MASSENGE_BUY_BOOK_SELECTOR = (By.XPATH, "//p[@class='content']")

class BooksPageLocators():
    BUTTON_BUY_BOOKS_SELECTOR = (By.XPATH, "//*[@class='button-2 product-box-add-to-cart-button']")
    MASSENGE_BUY_BOOKS_SELECTOR = (By.XPATH, "//p[@class='content']")

    BOOKS_CONTEINER_SELECTOR = (By.XPATH, "//*[@class='product-grid']")
    BOOKS_BOOK_SELECTOR = (By.XPATH, "//*[@class='item-box']")

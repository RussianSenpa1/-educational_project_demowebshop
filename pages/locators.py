from selenium.webdriver.common.by import By

class LinksLocators():
    MAIN_PAGES_LINK = 'http://demowebshop.tricentis.com/'
    REGISTER_PAGES_LINK = 'http://demowebshop.tricentis.com/register'

class MainPageLocators():
    LOGIN_SELECTOR = (By.XPATH, "//a[@class='ico-register']")

class RegisterPageLocators():
    FIRST_NAME_SELECTOR = (By.XPATH, "//*[@id='FirstName']")
    LAST_NAME_SELECTOR = (By.XPATH, "//*[@id='LastName']")
    EMAIL_REGISTER_SELECTOR = (By.XPATH, "//*[@id='Email']")
    PASSWORD_REGISTER_SELECTOR = (By.XPATH, "//*[@id='Password']")
from selenium.webdriver.common.by import By

class LinksLocators():
    MAIN_PAGES_LINK = 'http://demowebshop.tricentis.com/'
    REGISTER_PAGES_LINK = 'http://demowebshop.tricentis.com/register'

class MainPageLocators():
    LOGIN_SELECTOR = (By.XPATH, "//a[@class='ico-register']")

class RegisterPageLocators():
    FIRST_NAME_SELECTOR = (By.XPATH, "//*[@id='FirstName']")
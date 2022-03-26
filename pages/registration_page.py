import faker as faker

from .base_page import BasePage
from .locators import RegisterPageLocators


class RegistrationPage(BasePage):
    def should_be_register_url(self):
        assert "register" in self.url, "URL is not register"

    def should_be_firstname_field(self):
        assert self.is_element_present(*RegisterPageLocators.FIRST_NAME_SELECTOR), "FirstName field is not presented"

    def should_be_lastname_field(self):
        assert self.is_element_present(*RegisterPageLocators.LAST_NAME_SELECTOR), "LastName field is not presented"

    def should_be_email_field(self):
        assert self.is_element_present(*RegisterPageLocators.EMAIL_REGISTER_SELECTOR), "Email field is not presented"

    def should_be_password_field(self):
        assert self.is_element_present(
            *RegisterPageLocators.PASSWORD_REGISTER_SELECTOR), "Password field is not presented"

    def should_be_confirm_password_field(self):
        assert self.is_element_present(
            *RegisterPageLocators.CONFIRMPASSWORD_REGISTER_SELECTOR), "Confirm Password field is not presented"

    def should_be_register_button(self):
        assert self.is_element_present(
            *RegisterPageLocators.REGISTER_BUTTON_SELECTOR), "Register Button is not presented"

    def should_be_gender_male_female(self):
        assert self.is_element_present(
            *RegisterPageLocators.GENDER_MALE_SELECTOR) and self.is_element_present(
            *RegisterPageLocators.GENDER_FEMALE_SELECTOR), "Gender checkboxs is not presented"

    def should_be_registration(self):        #Проверка успешной регистрации
        assert self.is_element_present(
            *RegisterPageLocators.REZULT_MASSAGE_REGISTR_SELECTOR) and self.is_element_present(
            *RegisterPageLocators.REZULT_BUTTON_REGISTR_SELECTOR), "registration failed"


    def registration_data(self):     #Создание рандомных данных для регистрации
        first_name = faker.Faker().first_name()  # Создание рандомного Имени
        last_name = faker.Faker().last_name()  # Создание рандомного Фамилии
        email = faker.Faker().email()  # Создание рандомного Email
        password = "BloodTwix775"
        return first_name,last_name,email,password

    def new_user_register(self,first_name, last_name, email, password):    #Заполнение полей регистрации и нажатие кнопки регистрации

        first_name_field = self.browser.find_element(*RegisterPageLocators.FIRST_NAME_SELECTOR)
        first_name_field.send_keys(str(first_name))

        last_name_field = self.browser.find_element(*RegisterPageLocators.LAST_NAME_SELECTOR)
        last_name_field.send_keys(str(last_name))

        email_field = self.browser.find_element(*RegisterPageLocators.EMAIL_REGISTER_SELECTOR)
        email_field.send_keys(str(email))

        password_field = self.browser.find_element(*RegisterPageLocators.PASSWORD_REGISTER_SELECTOR)
        password_field.send_keys(str(password))

        confirmpassword_field = self.browser.find_element(*RegisterPageLocators.CONFIRMPASSWORD_REGISTER_SELECTOR)
        confirmpassword_field.send_keys(str(password))

        register = self.browser.find_element(*RegisterPageLocators.REGISTER_BUTTON_SELECTOR)
        register.click()

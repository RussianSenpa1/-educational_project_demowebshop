from .base_page import BasePage

class RegistrationPage(BasePage):
    def should_be_register_url(self):
        assert "register" in self.url, "URL is not register"
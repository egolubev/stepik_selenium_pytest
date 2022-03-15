from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url() # ссылка для входа найдена
        self.should_be_login_form() # форма для входа найдена
        self.should_be_register_form() # форма для регистрации найдена

    def should_be_login_url(self):
        assert "login" in self.url

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form not found"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form not found"

    def register_new_user(self, email, password):
        self.go_to_login_page()
        email_field = self.browser.find_element(*LoginPageLocators.EMAIL_FIELD)
        email_field.send_keys(email)
        pass1_field = self.browser.find_element(*LoginPageLocators.PASS_1_FIELD)
        pass1_field.send_keys(password)
        pass2_field = self.browser.find_element(*LoginPageLocators.PASS_2_FIELD)
        pass2_field.send_keys(password)
        button_registr = self.browser.find_element(*LoginPageLocators.BUTTON_REGISTR)
        button_registr.click()	
	
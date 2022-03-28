import time
from .base_page import BasePage
from .locators import LoginPageLocators, BasketPageLocators


class LoginPage(BasePage, LoginPageLocators):
    def __init__(self, browser, url, timeout=10):
        super().__init__(browser, url, timeout)

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        print(self.browser.current_url)
        assert "/login" in self.browser.current_url, "login is absent in current url"
        assert True

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"
        assert True

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"
        assert True

    def register_new_user(self, email, password):
        email_field = self.browser.find_element(*LoginPageLocators.EMAIL_FIELD)
        password_field = self.browser.find_element(*LoginPageLocators.PASSWORD_FIELD)
        confirm_password_field = self.browser.find_element(*LoginPageLocators.CONFIRM_PASSWORD_FIELD)
        register_button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        password_field.send_keys(password)
        confirm_password_field.send_keys(password)
        email_field.send_keys(email)
        register_button.click()


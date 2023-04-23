from pages.base_page import BasePage
from pages.locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, f"This url is not login url: {self.browser.current_url}"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self, email, password):
        input_email = self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL)
        input_password = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD)
        input_confirm_password = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD_CONFIRM)
        register_button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)

        input_email.send_keys(email)
        input_password.send_keys(password)
        input_confirm_password.send_keys(password)
        register_button.click()

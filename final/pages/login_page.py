from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def register_new_user(self, email, password):
        self.browser.find_element(*LoginPageLocators.EMAIL_REG).send_keys(email)
        self.browser.find_element(*LoginPageLocators.PASS_REG).send_keys(password)
        self.browser.find_element(*LoginPageLocators.CONFIRM_PASS_REG).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REG_BTN).click()

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in self.browser.current_url, "It's not a login page"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not present"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REG_FORM), "Reg form is not present"

    def should_see_registration_success_message(self):
        message = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located(LoginPageLocators.SUCCESS_MESSAGE)).text
        assert message in 'Thanks for registering!', \
            "Success message is not presented, but should be"

import math

from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from .locators import BasePageLocators, LoginPageLocators


class BasePage():
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def go_to_basket_page(self):
        link = self.browser.find_element(*BasePageLocators.BASKET_LINK)
        link.click()

    def go_to_login_page(self):
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()

    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True

    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    def open(self):
        self.browser.get(self.url)

    def should_be_authorized_user(self):
        assert self.is_element_present(*BasePageLocators.USER_ICON), \
            "User icon is not presented, probably unauthorised user"

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"

    def should_be_login_page(self):
        assert "/login/" in self.browser.current_url, "Url not from login page"
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not present"

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def search_for_product(self, search_string):
        self.browser.find_element(*BasePageLocators.SEARCH_FIELD).send_keys(search_string)
        self.browser.find_element(*BasePageLocators.SEARCH_BUTTON).click()

    def should_be_search_results(self,search_string):
        search_result = self.browser.find_element(*BasePageLocators.SEARCH_RESULT).text.lower()
        assert search_string in search_result, "Got wrong search result"

    def should_not_be_search_results(self):
        assert self.is_not_element_present(*BasePageLocators.SEARCH_RESULT), \
            "Found some items"

from .base_page import BasePage
from .locators import ProductPageLocators, BasePageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        add_to_basket = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        add_to_basket.click()

    def add_review(self):
        if self.is_element_present(*BasePageLocators.USER_ICON):
            # Зарегистрированный пользователь
            pass
        else:
            # Незарегистрированный пользователь
            pass


    def add_to_wishlist(self):
        if self.is_element_present(*BasePageLocators.USER_ICON):
            self.browser.find_element(*ProductPageLocators.ADD_TO_WISHLIST_BUTTON_REGISTERED).click()
            message = self.browser.find_element(*ProductPageLocators.ADDED_TO_WISHLIST_MESSAGE).text
            product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
            assert message == f"'{product_name}' was added to your wish list.", f"Got wrong message - {message}"
        else:
            assert not self.browser.find_element(*ProductPageLocators.ADD_TO_WISHLIST_BUTTON).is_enabled()

    def should_be_alert(self):
        assert self.browser.switch_to.alert, 'There is no alert'

    def should_be_success_message(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        product_name_in_alert = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_SUCCESS_MESSAGE).text
        assert product_name == product_name_in_alert, "Product name mismatch"

    def should_change_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text.split(" ")[-1]
        total_price = self.browser.find_element(*ProductPageLocators.TOTAL_PRICE).text
        total_price_message = self.browser.find_element(*ProductPageLocators.TOTAL_PRICE_MESSAGE).text
        assert product_price in total_price, "Product price and total price mismatch"
        assert product_price in total_price_message, "Product price and total price message mismatch"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_be_disappeared_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

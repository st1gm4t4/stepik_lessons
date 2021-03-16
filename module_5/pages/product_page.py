from .base_page import BasePage
from .locators import ProductPageLocators



class ProductPage(BasePage):
    def add_to_basket(self):
        add_to_basket = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        add_to_basket.click()

    def should_be_success_message(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        alert_text = self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE).text
        assert product_name in alert_text, "Product name mismatch"

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

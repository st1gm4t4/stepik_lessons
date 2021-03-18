from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_empty_basket(self):
        self.should_be_basket_url()
        self.should_be_no_items()
        self.should_be_empty_basket_message()

    def should_be_no_items(self):
        assert self.is_not_element_present(*BasketPageLocators.ITEMS_IN_BASKET), "Basket has items"

    def should_be_basket_url(self):
        assert '/basket/' in self.browser.current_url, "Not basket url"

    def should_be_empty_basket_message(self):
        message = self.browser.find_element(*BasketPageLocators.BASKET_IS_EMPTY_MESSAGE).text
        assert message == "Your basket is empty. Continue shopping", "Basket is not empty"

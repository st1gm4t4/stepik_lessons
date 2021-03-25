import uuid

import pytest

from .pages.login_page import LoginPage
from .pages.product_page import ProductPage


class TestProductPage():
    @pytest.mark.personal_tests
    def test_guest_cant_add_to_wishlist(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/hacking-exposed-wireless_208/"
        page = ProductPage(browser, link)
        page.open()
        page.add_to_wishlist()
        page.should_be_disabled_add_to_wishlist_button()

    @pytest.mark.personal_tests
    @pytest.mark.parametrize('search_string',
                             ["python", "handbook", ])
    def test_guest_can_search(self, browser, search_string):
        link = "http://selenium1py.pythonanywhere.com/catalogue/"
        page = ProductPage(browser, link)
        page.open()
        page.search_for_product(search_string)
        page.should_be_search_results(search_string)

    @pytest.mark.personal_tests
    def test_no_search_results(self, browser, search_string="azaza"):
        link = "http://selenium1py.pythonanywhere.com/catalogue/"
        page = ProductPage(browser, link)
        page.open()
        page.search_for_product(search_string)
        page.should_not_be_search_results()

    @pytest.mark.personal_tests
    def test_notify_guest_when_item_available(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/catalogue/hackers-painters_185/'
        page = ProductPage(browser, link)
        page.open()
        email = f"{uuid.uuid4().hex}@gmail.com"
        page.notify_me(email)
        page.should_be_notify_me_message(email)


class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/accounts/login/'
        register_page = LoginPage(browser, link)
        register_page.open()
        # регистрация нового пользователя
        email = f'{uuid.uuid4().hex}@mail.org'
        password = 'Nots0simplepassWord'
        register_page.register_new_user(email, password)
        # register_page.should_see_registration_success_message()
        register_page.should_be_authorized_user()
        return email

    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/"
        page = ProductPage(browser, link)
        page.open()
        page.add_to_basket()
        page.should_be_success_message()
        page.should_change_price()

    @pytest.mark.personal_tests
    def test_user_can_add_to_wishlist(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/"
        page = ProductPage(browser, link)
        page.open()
        page.add_to_wishlist()
        page.should_be_added_to_user_wishlist()

    @pytest.mark.personal_tests
    def test_notify_user_when_item_available(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/catalogue/hackers-painters_185/'
        page = ProductPage(browser, link)
        page.open()
        email = uuid.uuid4().hex
        page.notify_me(email)
        page.should_be_notify_me_message(email)

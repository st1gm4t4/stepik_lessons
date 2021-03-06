from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, "div.basket-mini.pull-right.hidden-xs > span > a")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    SEARCH_FIELD = (By.CSS_SELECTOR, "#id_q")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "div.navbar-collapse.primary-collapse.collapse > form > input")
    SEARCH_RESULT = (By.CSS_SELECTOR, "article > h3 > a")
    NOTHING_FOUND = (By.CSS_SELECTOR, "#default > div.container-fluid.page > div > div > div > form > p")


class BasketPageLocators():
    BASKET_IS_EMPTY_MESSAGE = (By.CSS_SELECTOR, "#content_inner > p")
    ITEMS_IN_BASKET = (By.CSS_SELECTOR, "#basket_formset > div")


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REG_FORM = (By.CSS_SELECTOR, "#register_form")
    EMAIL_REG = (By.CSS_SELECTOR, "#id_registration-email")
    PASS_REG = (By.CSS_SELECTOR, "#id_registration-password1")
    CONFIRM_PASS_REG = (By.CSS_SELECTOR, "#id_registration-password2")
    REG_BTN = (By.CSS_SELECTOR, "#register_form > button")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages > div.alert.alert-success.fade.in > div")


class ProductPageLocators():
    ADD_TO_BASKET = (By.CSS_SELECTOR, "#add_to_basket_form > button")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.col-sm-6.product_main > h1")
    PRODUCT_NAME_IN_SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "p.price_color")
    TOTAL_PRICE = (By.CSS_SELECTOR, "div.basket-mini.pull-right.hidden-xs")
    TOTAL_PRICE_MESSAGE = (
    By.CSS_SELECTOR, "#messages > div.alert.alert-safe.alert-noicon.alert-info.fade.in > div > p:nth-child(1) > strong")
    ADD_TO_WISHLIST_BUTTON_REGISTERED = (By.CSS_SELECTOR, "#add_to_wishlist_form > button")
    ADD_TO_WISHLIST_BUTTON = (By.CSS_SELECTOR, "div.col-sm-6.product_main > button")
    ADDED_TO_WISHLIST_MESSAGE = (By.CSS_SELECTOR, "#messages > div > div")
    NOTIFY_ME_BUTTON = (By.CSS_SELECTOR, "#alert_form > button")
    NOTIFY_ME_MESSAGE = (By.CSS_SELECTOR, "#messages > div > div")
    NOTIFY_ME_EMAIL_FIELD = (By.CSS_SELECTOR, "#id_email")
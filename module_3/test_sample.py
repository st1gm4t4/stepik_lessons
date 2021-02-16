import uuid
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

"""
Тест-кейс: Добавление товара в корзину со страницы товара.
"""
available_product_url = 'http://selenium1py.pythonanywhere.com/ru/catalogue/adolescence-of-p-1-r_96/'
unavailable_product_url = 'http://selenium1py.pythonanywhere.com/ru/catalogue/the-city-and-the-stars_95/'
add_to_basket_button_locator = '#add_to_basket_form>button'
instock_availability_locator = 'p.instock.availability'
out_of_stock_availability_locator = 'p.outofstock.availability'
item_name_locator = 'div.col-sm-6.product_main>h1'
item_price_locator = 'div.col-sm-6.product_main>p.price_color'
basket_total_sum_popup_locator = 'div.alert.alert-safe.alert-noicon.alert-info.fade.in>div>p>strong'
item_name_popup_locator = '#messages>div:nth-child(1)>div>strong'
notify_me_button_locator = '#alert_form>button'
notification_popup_locator = '#messages'
email = '#id_email'
email_address = f'test+{uuid.uuid4().hex}@test.com'



def test_add_to_basket_available_item():
    # Arrange
    browser = webdriver.Chrome()
    browser.get(available_product_url)
    # Берем название и цену для последующего сравнения с текстом в плашках
    item_price = browser.find_element(By.CSS_SELECTOR, item_price_locator).text
    item_name = browser.find_element(By.CSS_SELECTOR, item_name_locator).text

    # Act
    try:
        # Проверка доступности товара для заказа по наличию элемента "на складе", ждем загрузку страницы
        WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, instock_availability_locator))
        )
        # Добавление в корзину
        browser.find_element(By.CSS_SELECTOR, add_to_basket_button_locator).click()

    # Assert
        # Проверка стоимости товара в плашке "Стоимость корзины теперь составляет"
        EC.presence_of_element_located((By.CSS_SELECTOR, instock_availability_locator))
        assert item_price == browser.find_element(By.CSS_SELECTOR, basket_total_sum_popup_locator).text, \
            "Item price in popup didn't match actual price"
        # Проверка названия товара в плашке "... был добавлен в вашу корзину"
        assert item_name == browser.find_element(By.CSS_SELECTOR, item_name_popup_locator).text, \
            "Item name in popup didn't match actual item name"


    finally:
        browser.quit()


def test_add_to_basket_unavailable_item_and_check_notification():
    # Arrange
    browser = webdriver.Chrome()
    browser.get(unavailable_product_url)

    # Act
    try:
        # Количество товара на складе не показывается, ждем загрузку страницы
        WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, out_of_stock_availability_locator))
        )
        # Проверяем отсутствие кнопки "Добавить в корзину"
        add_to_basket_button_list = browser.find_elements(By.CSS_SELECTOR, add_to_basket_button_locator)
        assert len(add_to_basket_button_list) == 0, \
            "Кнопка 'Добавить в корзину' есть на странице"
        # Проверяем работу кнопки "Сообщить мне"
        browser.find_element(By.CSS_SELECTOR, email).send_keys(email_address)
        browser.find_element(By.CSS_SELECTOR, notify_me_button_locator).click()
        WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, notification_popup_locator))
        )
        notification = browser.find_element(By.CSS_SELECTOR, notification_popup_locator).text
        assert f'Письмо с подтверждением отправлено на {email_address}' in notification, \
            "Текст попапа не соответствует шаблону, либо отображен неправильный email"


    finally:
        browser.quit()


if __name__ == "__main__":
    test_add_to_basket_available_item()
    test_add_to_basket_unavailable_item_and_check_notification()

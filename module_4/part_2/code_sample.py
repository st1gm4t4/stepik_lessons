import uuid

link = 'http://selenium1py.pythonanywhere.com/accounts/login/'
email_locator = '#id_registration-email'
password_1_locator = '#id_registration-password1'
password_2_locator = '#id_registration-password2'
submit_button_locator = '#register_form > button'
password = 'test2test'
login_message_locator = '#messages'
login_message_text = 'Thanks for registering!'


def test_button_language(browser):
    browser.get(link)
    browser.execute_script("arguments[0].scrollIntoView();", browser.find_element_by_css_selector(submit_button_locator))
    browser.find_element_by_css_selector(email_locator).send_keys(f'test{str(uuid.uuid4().hex)}@test.com')
    browser.find_element_by_css_selector(password_1_locator).send_keys(password)
    browser.find_element_by_css_selector(password_2_locator).send_keys(password)
    browser.find_element_by_css_selector(submit_button_locator).click()
    assert login_message_text in browser.find_element_by_css_selector(login_message_locator).text, \
        'Login was not successfull'
import os
from datetime import datetime

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en-GB',
                     help="Choose browser language. Default is 'en-GB'")

    parser.addoption('--browser', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")

    parser.addoption('--screenshots', action='store', default="off",
                     help="Taking screenshots or not")


@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")
    browser = None
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': language})
    browser_name = request.config.getoption("browser")
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox()
    else:
        print(f"Browser {browser_name} still is not implemented")
    browser.maximize_window()
    yield browser
    print("\nquit browser..")
    screenshots = request.config.getoption("screenshots")
    if screenshots == "on":
        dir = 'screenshots'
        if not os.path.exists(dir):
            os.makedirs(dir)
        now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        browser.save_screenshot(f'{dir}/screenshot-{now}.png')
    browser.quit()


@pytest.fixture(scope="function")
def browser_lang(request):
    return request.config.getoption('--language')

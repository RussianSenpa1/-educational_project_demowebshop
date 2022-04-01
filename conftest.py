import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--browser', action='store', default='chrome',
                     help="Browser choice. chrome or firefox")
    parser.addoption('--headless', action='store', default='off',
                     help="Headless choice. on or off")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser")
    headless_what = request.config.getoption("headless")

    if browser_name == "chrome":
        if headless_what == 'off':
            browser = webdriver.Chrome()
            yield browser
            browser.quit()

        elif headless_what == 'on':
            options = Options()
            options.add_argument('headless')
            browser = webdriver.Chrome(options=options)
            yield browser
            browser.quit()

    elif browser_name == "firefox":
        if headless_what == 'off':
            browser = webdriver.Firefox()
            yield browser
            browser.quit()
        elif headless_what == 'on':
            options = webdriver.FirefoxOptions()
            options.headless = True
            browser = webdriver.Firefox(options=options)
            yield browser
            browser.quit()

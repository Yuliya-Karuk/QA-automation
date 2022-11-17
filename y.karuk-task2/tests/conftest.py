import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from utils.work_with_json import DataJson
from config.config import Config


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en',
                     help="Choose language: ru, en and etc")


@pytest.fixture(scope="function")
def browser(request):
    browser_access = DataJson.finding_value_from_json('../config/config_data.json', 'access')
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument(browser_access)
    chrome_options.add_experimental_option('prefs', {'intl.accept_languages': "language"})
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    user_language = request.config.getoption("language")
    base_url = DataJson.finding_value_from_json('../config/config_data.json', 'url')
    browser.get(base_url)
    yield browser
    browser.delete_all_cookies()
    browser.quit()







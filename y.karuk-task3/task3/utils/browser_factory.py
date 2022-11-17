from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.chrome.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from task3.utils.json_manager import DataJson


class BrowserFactory:
    __browser_access = DataJson.finding_value_from_json('../data/config_data.json', 'access')

    @staticmethod
    def choose_webdriver(browser_name):
        if browser_name == 'firefox':
            firefox_service = Service(GeckoDriverManager().install())
            firefox_options = BrowserFactory.set_firefox_options()
            return webdriver.Firefox(service=firefox_service, options=firefox_options)
        if browser_name == 'chrome':
            chrome_service = Service(ChromeDriverManager().install())
            chrome_options = BrowserFactory.set_chrome_options()
            return webdriver.Chrome(service=chrome_service, options=chrome_options)

    @staticmethod
    def set_chrome_options():
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument(BrowserFactory.__browser_access)
        return chrome_options

    @staticmethod
    def set_firefox_options():
        firefox_options = FirefoxOptions()
        firefox_options.add_argument(BrowserFactory.__browser_access)
        return firefox_options

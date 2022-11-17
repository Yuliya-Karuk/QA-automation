from task3.utils.singleton import Singleton
from task3.utils.json_manager import DataJson
from task3.utils.browser_factory import BrowserFactory


class WebApp(metaclass=Singleton):
    __browser_name = DataJson.finding_value_from_json('../data/test_data.json', 'browser_chrome')
    __instance = None

    def __init__(self):
        self.driver = BrowserFactory().choose_webdriver(WebApp.__browser_name)

    @staticmethod
    def get_instance():
        if WebApp.__instance is None:
            return WebApp()
        return WebApp.__instance

    @staticmethod
    def del_instance():
        WebApp._instances = {}
        WebApp.__instance = None
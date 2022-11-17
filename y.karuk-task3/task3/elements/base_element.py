from task3.utils.driver_utils import DriverUtils
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from task3.utils.json_manager import DataJson
from task3.utils.logger import Logger
from task3.utils.js_executor import JS_executor as JS


class BaseElement():
    __base_wait_time = DataJson.finding_value_from_json('../data/config_data.json', 'wait_time')
    __browser = DriverUtils().get_driver()
    __wait = WebDriverWait(__browser, __base_wait_time)

    def __init__(self, locator, name_elem):
        self.locator = locator
        self.name_elem = name_elem

    def find_element(self):
        Logger.log("INFO", f'find element {self.name_elem}')
        element = BaseElement.__wait.until(EC.presence_of_element_located((By.XPATH, self.locator)))
        return element

    def click_element(self):
        Logger.log("INFO", f'click element {self.name_elem}')
        element = self.find_element()
        element.click()

    def find_click_element_JS(self):
        Logger.log("INFO", f'click element {self.name_elem} with JS')
        element = self.find_element()
        JS.click_element_with_JS(element)

    def get_text(self):
        Logger.log("INFO", f'find text from element {self.name_elem}')
        element = self.find_element()
        return element.text

    def element_is_visible(self):
        Logger.log("INFO", f'check element is visible {self.name_elem}')
        try:
            BaseElement.__wait.until(EC.visibility_of_element_located((By.XPATH, self.locator)))
            return True
        except:
            return False

    def element_is_invisible(self):
        Logger.log("INFO", f'check element is invisible {self.name_elem}')
        try:
            BaseElement.__wait.until(EC.invisibility_of_element_located((By.XPATH, self.locator)))
            return True
        except:
            return False

    def get_attribute(self, name_of_attribute):
        Logger.log("INFO", f'get attribute from element {self.name_elem}')
        element = self.find_element()
        return element.get_attribute(name_of_attribute)
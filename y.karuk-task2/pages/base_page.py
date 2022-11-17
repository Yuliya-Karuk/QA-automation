from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.work_with_json import DataJson



class BasePage():
    base_wait_time = DataJson.finding_value_from_json('../config/config_data.json', 'wait_time')

    def find_text_from_element(self, browser, unique_locator):
        try:
            searching_element = WebDriverWait(browser, self.base_wait_time).until(
                EC.presence_of_element_located((By.XPATH, unique_locator)))
            searching_text = searching_element.text
            return searching_text
        except AssertionError:
            return "There isn`t such element"


    def find_url(self, browser):
        url = browser.current_url
        return url





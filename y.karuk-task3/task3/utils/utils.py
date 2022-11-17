from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import random
import string
import re
from task3.utils.driver_utils import DriverUtils
from task3.utils.logger import Logger
from datetime import datetime
from task3.utils.json_manager import DataJson


class Utils:
    __browser = DriverUtils().get_driver()
    __base_wait_time = DataJson.finding_value_from_json('../data/config_data.json', 'wait_time')
    __wait = WebDriverWait(__browser, __base_wait_time)

    @staticmethod
    def find_digit_from_string(searching_string):
        list_with_number = re.findall('[0-9]+', searching_string)
        number_string = list_with_number[0]
        for i in list_with_number[1:]:
            number_string = number_string + i
        number_int = int(number_string)
        return number_int

    @staticmethod
    def find_number_from_string(searching_string):
        list_with_number = re.findall('[0-9.]+', searching_string)
        number_string = list_with_number[0]
        for i in list_with_number[1:]:
            number_string = number_string + i
        number_float = float(number_string)
        return number_float

    @staticmethod
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    @staticmethod
    def subtraction_string(string, substring):
        return string.replace(substring, '')

    @staticmethod
    def switch_to_default_content():
        Logger.log("INFO", f'switch to default content on page')
        Utils.__browser.switch_to.default_content()

    @staticmethod
    def find_list_of_elements(locator):
        list_of_elements = Utils.__wait.until(EC.presence_of_all_elements_located((By.XPATH, locator)))
        return list_of_elements

    @staticmethod
    def find_closest_year(month_day):
        current_year = int(datetime.now().strftime("%Y"))
        closest_years = [current_year - (current_year % 4), current_year + (4 - current_year % 4)]
        delta_in_time = []
        needed_year = []
        for i in closest_years:
            delta = abs(datetime(i, month_day[0], month_day[1]) - datetime.now())
            if len(delta_in_time) == 0:
                delta_in_time.append(delta)
                needed_year.append(i)
            else:
                if delta < delta_in_time[0]:
                    delta_in_time[0] = delta
                    needed_year[0] = i
        return needed_year[0]
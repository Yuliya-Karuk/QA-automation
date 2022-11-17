from task3.elements.base_element import BaseElement
from task3.utils.json_manager import DataJson
from task3.utils.logger import Logger


class Input(BaseElement):
    __base_wait_time = DataJson.finding_value_from_json('../data/config_data.json', 'wait_time')

    def __init__(self, locator, name_elem):
        super().__init__(locator, name_elem)

    def send_keys(self, key_value):
        Logger.log("INFO", f'send keys in input {self.name_elem}')
        element = self.find_element()
        element.send_keys(key_value)
from task3.elements.base_element import BaseElement
from task3.utils.webapp import WebApp
from task3.utils.logger import Logger
from task3.utils.driver_utils import DriverUtils


class Iframe(BaseElement):
    def __init__(self, locator, name_elem, iframe_tag):
        super().__init__(locator, name_elem)
        self.iframe_tag = iframe_tag

    def find_and_switch_to_iframe_by_tag(self):
        browser = DriverUtils().get_driver()
        Logger.log("INFO", f'find element {self.name_elem}')
        iframe = browser.find_elements_by_tag_name('iframe')[self.iframe_tag]
        Logger.log("INFO", f'switch to {self.name_elem}')
        browser.switch_to.frame(iframe)
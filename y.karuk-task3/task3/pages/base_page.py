from abc import ABC
from task3.elements.base_element import BaseElement
from task3.utils.logger import Logger


class BasePage(ABC):
    def __init__(self, unique_element, name_page):
        self.__unique_element: BaseElement = unique_element
        self.name_page = name_page

    def is_page_open(self):
        Logger.log("INFO", f'{self.name_page} is open')
        try:
            self.__unique_element.element_is_visible()
            self.__unique_element.find_element()
            return True
        except:
            return False
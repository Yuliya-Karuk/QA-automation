from task3.pages.base_page import BasePage
from task3.elements.button import Button
from task3.utils.logger import Logger


class MainPage(BasePage):
    __name_page = 'Main Page'
    __box_alert = Button("//h5[contains(text(), 'Alerts')]/ancestor::div[@class='card-body']",
                         'button to open Alert page')
    __box_elements = Button("//h5[contains(text(), 'Elements')]/ancestor::div[@class='card-body']",
                            'button to open Elements page')
    __box_widgets = Button("//h5[contains(text(), 'Widgets')]/ancestor::div[@class='card-body']",
                           'button to open Widgets page')
    __unique_element = Button("//div[@class='home-banner']", "unique element from Main page")

    def __init__(self):
        super().__init__(MainPage.__unique_element, MainPage.__name_page)

    def click_box_alert(self):
        Logger.log("INFO", f'to open Alert page from {self.__name_page}')
        self.__box_alert.find_click_element_JS()

    def click_box_elements(self):
        Logger.log("INFO", f'to open Elements page from {self.__name_page}')
        self.__box_elements.find_click_element_JS()

    def click_box_widgets(self):
        Logger.log("INFO", f'to open Widgets page from {self.__name_page}')
        self.__box_widgets.find_click_element_JS()


main_page = MainPage()
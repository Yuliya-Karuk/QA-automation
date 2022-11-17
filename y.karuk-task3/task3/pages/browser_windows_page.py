from task3.elements.text import Text
from task3.pages.base_page import BasePage
from task3.elements.button import Button
from task3.utils.logger import Logger
from task3.pages.navigation_form import NavForm


class BrowserWindowsPage(BasePage):
    __name_page = 'Browser Window Page'
    __unique_element = Text("//div[@class='main-header' and contains(text(), 'Browser Windows')]",
                            "browser window page unique element")
    __button_new_tab = Button("//button[@id='tabButton']", 'button new tab')

    def __init__(self):
        super().__init__(BrowserWindowsPage.__unique_element, BrowserWindowsPage.__name_page)

    def open_new_tab(self):
        Logger.log("INFO", f'open New Tab from {self.__name_page}')
        BrowserWindowsPage.__button_new_tab.click_element()

    def click_main_button_element_nav_menu(self):
        NavForm.click_main_button_element()

    def click_button_links_nav_menu(self):
        NavForm.click_button_links()


browser_windows_page = BrowserWindowsPage()
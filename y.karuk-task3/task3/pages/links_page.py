from task3.elements.text import Text
from task3.pages.base_page import BasePage
from task3.elements.button import Button


class LinksPage(BasePage):
    __name_page = 'Links Page'
    __unique_element = Text("//div[@class='main-header' and contains(text(), 'Links')]", "unique element on Links page")
    __link_home = Button("//a[@id='simpleLink']", 'link home')

    def __init__(self):
        super().__init__(LinksPage.__unique_element, LinksPage.__name_page)

    def click_link_home(self):
        self.__link_home.click_element()


links_page = LinksPage()
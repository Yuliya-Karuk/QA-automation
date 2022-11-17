from task3.elements.text import Text
from task3.pages.base_page import BasePage
from task3.elements.iframe import Iframe


class FramesPage(BasePage):
    __name_page = 'Frames Page'
    __unique_element = Text("//div[@class='main-header' and contains(text(), 'Frames')]", "unique element on frame page")
    __first_iframe = Iframe("", 'first iframe', 1)
    __second_iframe = Iframe("", 'second iframe', 2)
    __first_text = Text("//h1", 'text from first iframe')
    __second_text = Text("//body/h1", 'text from second iframe')

    def __init__(self):
        super().__init__(FramesPage.__unique_element, FramesPage.__name_page)

    def switch_to_first_iframe(self):
        self.__first_iframe.find_and_switch_to_iframe_by_tag()

    def find_text_from_first_iframe(self):
        text = self.__first_text.get_text()
        return text

    def switch_to_second_iframe(self):
        self.__second_iframe.find_and_switch_to_iframe_by_tag()

    def find_text_from_second_iframe(self):
        text = self.__second_text.get_text()
        return text


frames_page = FramesPage()
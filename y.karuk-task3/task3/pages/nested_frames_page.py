from task3.elements.text import Text
from task3.pages.base_page import BasePage
from task3.elements.iframe import Iframe


class NestedFramesPage(BasePage):
    __name_page = 'Nested Frames Page'
    __parental_iframe = Iframe("", 'parental_iframe', 1)
    __child_iframe = Iframe("", 'child_iframe', 0)
    __unique_element = Text("//div[@class='main-header' and contains(text(), 'Nested')]",
                            "unique element from nested frames page")
    __parental_text = Text("//body", 'parental_text')
    __child_text = Text("//p", 'parental_text')

    def __init__(self):
        super().__init__(NestedFramesPage.__unique_element, NestedFramesPage.__name_page)

    def switch_to_parental_iframe(self):
        self.__parental_iframe.find_and_switch_to_iframe_by_tag()

    def find_text_from_parental_iframe(self):
        text = self.__parental_text.get_text()
        return text

    def switch_to_child_iframe(self):
        self.__child_iframe.find_and_switch_to_iframe_by_tag()

    def find_text_from_child_iframe(self):
        text = self.__child_text.get_text()
        return text


nested_frames_page = NestedFramesPage()
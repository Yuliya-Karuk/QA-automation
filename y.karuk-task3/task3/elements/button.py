from task3.elements.base_element import BaseElement


class Button(BaseElement):
    def __init__(self, locator, name_elem):
        super().__init__(locator, name_elem)
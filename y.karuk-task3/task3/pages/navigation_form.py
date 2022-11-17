from task3.elements.button import Button
from task3.utils.logger import Logger


class NavForm:
    __button_alert = Button("//span[(text()='Alerts')]/ancestor::li", 'button alert')
    __button_nested_frames = Button("//span[(text()='Nested Frames')]/ancestor::li",
                                    'button nested frames')
    __button_frames = Button("//span[(text()='Frames')]/ancestor::li", 'button frames')
    __button_web_tables = Button("//span[(text()='Web Tables')]/ancestor::li", 'button web tables')
    __button_browser_windows = Button("//span[(text()='Browser Windows')]/ancestor::li", 'button browser window')
    __main_button_element = Button("//div[text()='Elements']", 'accordion button elements')
    __button_links = Button("//span[(text()='Links')]/ancestor::li", 'button links')
    __button_date_picker = Button("//span[(text()='Date Picker')]/ancestor::li", 'button links')

    @staticmethod
    def click_button_alert():
        Logger.log("INFO", f'to click Alert button on navigation menu')
        NavForm.__button_alert.find_click_element_JS()

    @staticmethod
    def click_button_nested_frames():
        Logger.log("INFO", f'to click Nested Frame button on navigation menu')
        NavForm.__button_nested_frames.find_click_element_JS()

    @staticmethod
    def click_button_frames():
        Logger.log("INFO", f'to click Frames button on navigation menu')
        NavForm.__button_frames.find_click_element_JS()

    @staticmethod
    def click_button_web_tables():
        Logger.log("INFO", f'to click Web Tables button on navigation menu')
        NavForm.__button_web_tables.find_click_element_JS()

    @staticmethod
    def click_button_browser_windows():
        Logger.log("INFO", f'to click Browser Windows button on navigation menu')
        NavForm.__button_browser_windows.find_click_element_JS()

    @staticmethod
    def click_main_button_element():
        Logger.log("INFO", f'to click accordion button Elements')
        NavForm.__main_button_element.find_click_element_JS()

    @staticmethod
    def click_button_links():
        Logger.log("INFO", f'to click Links button on navigation menu')
        NavForm.__button_links.find_click_element_JS()

    @staticmethod
    def click_button_date_picker():
        Logger.log("INFO", f'to click Date Picker button on navigation menu')
        NavForm. __button_date_picker.find_click_element_JS()
from task3.elements.button import Button
from task3.elements.text import Text
from task3.utils.utils import Utils
from task3.pages.base_page import BasePage
from task3.utils.logger import Logger
from task3.pages.navigation_form import NavForm


class AlertPage(BasePage):
    __name_page = 'Alert Page'
    __button_to_see_alert = Button("//button[@id='alertButton']", "button to see alert")
    __button_to_see_confirm = Button("//button[@id='confirmButton']", "button to see confirm")
    __button_to_see_prompt = Button("//button[@id='promtButton']", "button to see prompt")
    __unique_element = Text("//div[@class='main-header' and contains(text(), 'Alerts')]", "unique_element from Alert page")
    __confirm_text = Text("//span[@id='confirmResult']", "text box after accept confirm")
    __prompt_text = Text("//span[@id='promptResult']", "text box after send keys to prompt")

    def __init__(self):
        super().__init__(AlertPage.__unique_element, AlertPage.__name_page)

    def click_button_to_see_alert(self):
        Logger.log("INFO", f'to open alert form from {self.__name_page}')
        self.__button_to_see_alert.click_element()

    def click_button_to_see_confirm(self):
        Logger.log("INFO", f'to open confirm form from {self.__name_page}')
        self.__button_to_see_confirm.click_element()

    def find_text_after_confirm(self):
        return self.__confirm_text.get_text()

    def click_button_to_see_prompt(self):
        Logger.log("INFO", f'to open prompt form from {self.__name_page}')
        self.__button_to_see_prompt.click_element()

    def find_text_after_prompt(self):
        text = self.__prompt_text.get_text()
        sub_string = "You entered "
        entered_text = Utils.subtraction_string(text, sub_string)
        return entered_text

    def click_button_alert_nav_menu(self):
        NavForm.click_button_alert()

    def click_button_nested_frames_nav_menu(self):
        NavForm.click_button_nested_frames()

    def click_button_frames_nav_menu(self):
        NavForm.click_button_frames()

    def click_button_browser_windows_nav_menu(self):
        NavForm.click_button_browser_windows()


alert_page = AlertPage()
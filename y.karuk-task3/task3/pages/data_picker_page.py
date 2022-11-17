from task3.elements.input import Input
from task3.elements.text import Text
from task3.utils.utils import Utils
from task3.pages.base_page import BasePage
from task3.utils.logger import Logger
from datetime import datetime
from task3.utils.json_manager import DataJson
from task3.utils.js_executor import JS_executor as JS
from task3.pages.navigation_form import NavForm


class DatePickerPage(BasePage):
    __name_page = 'Date Picker Page'
    __unique_element = Text("//div[@class='main-header' and contains(text(), 'Date Picker')]", "unique_element from Date Picker page")
    __select_date_field = Input("//input[@id='datePickerMonthYearInput']", "select date field")
    __date_and_time_field = Input("//input[@id='dateAndTimePickerInput']", "date and time field")

    def __init__(self):
        super().__init__(DatePickerPage.__unique_element, DatePickerPage.__name_page)

    def get_date(self):
        Logger.log("INFO", f'to get date from select data field on {self.__name_page}')
        return self.__select_date_field.get_attribute('value')

    def compare_date(self):
        Logger.log("INFO", f'to compare date from select data field on {self.__name_page} with current date')
        date_on_page = self.get_date()
        now_date = datetime.now().strftime("%m/%d/%Y")
        if date_on_page == now_date:
            return True
        else:
            return False

    def get_timedate(self):
        Logger.log("INFO", f'to get timedate from data and time field on {self.__name_page}')
        return self.__date_and_time_field.get_attribute('value')

    def compare_timedate(self):
        Logger.log("INFO", f'to compare timedate from data and time field on {self.__name_page} with current timedate')
        timedate_on_page = self.get_timedate()
        now_timedate = datetime.now().strftime("%B %#d, %Y %#I:%M %p")
        if timedate_on_page == now_timedate:
            return True
        else:
            return False

    def set_date_nearest_year(self):
        Logger.log("INFO", f'to set needed date to data field on {self.__name_page}')
        date_for_test = DataJson.finding_value_from_json('../data/test_data.json', 'date_for_test')
        needed_year = Utils.find_closest_year(date_for_test)
        all_date = f"0{date_for_test[0]}/{date_for_test[1]}/{needed_year}"
        element = self.__select_date_field.find_element()
        JS.set_attribute_with_JS(all_date, element)
        return all_date

    def click_button_date_picker_nav_menu(self):
        NavForm.click_button_date_picker()


date_picker_page = DatePickerPage()
from task3.elements.text import Text
from task3.pages.base_page import BasePage
from task3.elements.button import Button
from task3.elements.form import Form
from task3.elements.input import Input
from task3.utils.logger import Logger
from task3.utils.js_executor import JS_executor as JS
from task3.utils.utils import Utils
from task3.pages.navigation_form import NavForm


class WebTablesPage(BasePage):
    __name_page = 'Web Tables Page'
    __unique_element = Text("//div[@class='main-header' and contains(text(),'Web Tables')]",
                            "unique element on Web Tables page")
    __add_button = Button("//button[@id='addNewRecordButton']", 'add button for add user')
    __registration_form = Form("//div[@class='modal-content']", 'registration form')
    __input_first_name = Input("//input[@id='firstName']", 'input first name')
    __input_last_name = Input("//input[@id='lastName']", 'input last name')
    __input_email = Input("//input[@id='userEmail']", 'input user email')
    __input_age = Input("//input[@id='age']", 'input age')
    __input_salary = Input("//input[@id='salary']", 'input salary')
    __input_department = Input("//input[@id='department']", 'input department')
    __submit_button = Button("//button[@id='submit']", 'submit button to add User data')
    __list_of_rows_locator = "//div[@class='rt-tbody']//div[@role='row' and not(contains(@class, '-padRow'))]"
    __list_of_first_name = "//div[@class='rt-tbody']//div[@role='row' and not(contains(@class, '-padRow'))]/div[1]"
    __list_of_last_name = "//div[@class='rt-tbody']//div[@role='row' and not(contains(@class, '-padRow'))]/div[2]"
    __list_of_age = "//div[@class='rt-tbody']//div[@role='row' and not(contains(@class, '-padRow'))]/div[3]"
    __list_of_email = "//div[@class='rt-tbody']//div[@role='row' and not(contains(@class, '-padRow'))]/div[4]"
    __list_of_salary = "//div[@class='rt-tbody']//div[@role='row' and not(contains(@class, '-padRow'))]/div[5]"
    __list_of_department = "//div[@class='rt-tbody']//div[@role='row' and not(contains(@class, '-padRow'))]/div[6]"
    __list_of_delete_locator = "//span[@title='Delete']"

    def __init__(self):
        super().__init__(WebTablesPage.__unique_element, WebTablesPage.__name_page)

    def click_add_button(self):
        self.__add_button.click_element()

    def registration_form_is_open(self):
        Logger.log("INFO", f'open {self.__registration_form.name_elem} on {self.__name_page}')
        return self.__registration_form.element_is_visible()

    def fill_registration_form(self, user):
        Logger.log("INFO", f'fill the {self.__registration_form.name_elem} on {self.__name_page}')
        self.__input_first_name.send_keys(user["First_name"])
        self.__input_last_name.send_keys(user["Last name"])
        self.__input_email.send_keys(user["email"])
        self.__input_age.send_keys(user["age"])
        self.__input_salary.send_keys(user["Salary"])
        self.__input_department.send_keys(user["Department"])
        self.__submit_button.click_element()

    def registration_form_is_closed(self):
        Logger.log("INFO", f'close {self.__registration_form.name_elem} on {self.__name_page}')
        return self.__registration_form.element_is_invisible()

    def find_data_user_one_the_page(self):
        Logger.log("INFO", f'find number of data user rows on {self.__name_page}')
        list_of_rows_user_data = self.find_number_of_rows_user_data()
        Logger.log("INFO", f'find list of first name data users on {self.__name_page}')
        list_of_first_names = Utils.find_list_of_elements(self.__list_of_first_name)
        Logger.log("INFO", f'find list of last name data users on {self.__name_page}')
        list_of_last_names = Utils.find_list_of_elements(self. __list_of_last_name)
        Logger.log("INFO", f'find list of age data users on {self.__name_page}')
        list_of_age = Utils.find_list_of_elements(self.__list_of_age)
        Logger.log("INFO", f'find list of email data users on {self.__name_page}')
        list_of_email = Utils.find_list_of_elements(self.__list_of_email)
        Logger.log("INFO", f'find list of salary data users on {self.__name_page}')
        list_of_salary = Utils.find_list_of_elements(self.__list_of_salary)
        Logger.log("INFO", f'find list of department data users on {self.__name_page}')
        list_of_department = Utils.find_list_of_elements(self.__list_of_department)
        all_user = []
        Logger.log("INFO", f'distribute data for each user into a separate dictionary on {self.__name_page}')
        for i in range(list_of_rows_user_data):
            user = {}
            user["First_name"] = list_of_first_names[i].text
            user["Last name"] = list_of_last_names[i].text
            user["age"] = list_of_age[i].text
            user["email"] = list_of_email[i].text
            user["Salary"] = list_of_salary[i].text
            user["Department"] = list_of_department[i].text
            all_user.append(user)
        return all_user

    def check_data_user_one_the_page(self, entered_data):
        Logger.log("INFO", f'check added data of User appeared in a table on {self.__name_page}')
        founded_all_data_user = self.find_data_user_one_the_page()
        for i in founded_all_data_user:
            if i == entered_data:
                return True
        return False

    def delete_user_data(self):
        Logger.log("INFO", f'delete added data of User from table on {self.__name_page}')
        list_of_delete_button = Utils.find_list_of_elements(self.__list_of_delete_locator)
        JS.click_element_with_JS(list_of_delete_button[-1])

    def find_number_of_rows_user_data(self):
        Logger.log("INFO", f'find number of rows data Users in a table on {self.__name_page}')
        list_of_rows_user_data = Utils.find_list_of_elements(self.__list_of_rows_locator)
        return len(list_of_rows_user_data)

    def click_button_web_tables_nav_menu(self):
        NavForm.click_button_web_tables()


web_tables_page = WebTablesPage()
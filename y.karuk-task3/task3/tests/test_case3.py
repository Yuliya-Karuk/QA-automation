import pytest
from task3.pages.main_page import main_page
from task3.pages.web_tables import web_tables_page
from task3.utils.json_manager import DataJson


user_1 = DataJson.finding_value_from_json('../data/test_data.json', 'User 1')
user_2 = DataJson.finding_value_from_json('../data/test_data.json', 'User 2')


class Test:
    @pytest.mark.parametrize('users', [user_1, user_2])
    def test_case(self, setup, users):
        assert main_page.is_page_open() == True, 'Main page isn`t open '
        main_page.click_box_elements()
        web_tables_page.click_button_web_tables_nav_menu()
        assert web_tables_page.is_page_open() == True, "Page with Web Tables form isn`t open"
        web_tables_page.click_add_button()
        assert web_tables_page.registration_form_is_open() == True, "gfh"
        web_tables_page.fill_registration_form(users)
        assert web_tables_page.registration_form_is_closed() == True, "Registration form hasn`t closed."
        assert web_tables_page.check_data_user_one_the_page(users) == True, "Data of User № hasn`t appeared in a table"
        numbers_of_records_before_del = web_tables_page.find_number_of_rows_user_data()
        web_tables_page.delete_user_data()
        numbers_of_records_after_del = web_tables_page.find_number_of_rows_user_data()
        assert numbers_of_records_before_del != numbers_of_records_after_del, "Number of records in table hasn't changed"
        assert web_tables_page.check_data_user_one_the_page(users) == False, "Data of User № hasn`t appeared in a table"



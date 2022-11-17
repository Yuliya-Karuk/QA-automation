from task3.pages.main_page import main_page
from task3.pages.data_picker_page import date_picker_page


class Test:
    def test_case(self, setup):
        assert main_page.is_page_open() == True, 'Main page isn`t open '
        main_page.click_box_widgets()
        date_picker_page.click_button_date_picker_nav_menu()
        assert date_picker_page.is_page_open() == True, 'Page with Date Picker form isn`t open.'
        assert date_picker_page.compare_date() == True and date_picker_page.compare_timedate() == True,\
            "Values of Select Date and Date And Time fields aren`t equal to current date and time "
        assert date_picker_page.set_date_nearest_year() == date_picker_page.get_date(),\
            "Value isn`t equal to the one set previously"

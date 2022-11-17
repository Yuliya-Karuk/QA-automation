from task3.pages.main_page import main_page
from task3.pages.frames_page import frames_page
from task3.pages.alert_page import alert_page
from task3.pages.nested_frames_page import nested_frames_page
from task3.utils.utils import Utils


class Test:
    def test_case(self, setup):
        assert main_page.is_page_open() == True, 'Main page isn`t open'
        main_page.click_box_alert()
        alert_page.click_button_nested_frames_nav_menu()
        assert nested_frames_page.is_page_open() == True, 'Page with Nested Frames form isn`t open'
        nested_frames_page.switch_to_parental_iframe()
        parental_text = nested_frames_page.find_text_from_parental_iframe()
        nested_frames_page.switch_to_child_iframe()
        child_text = nested_frames_page.find_text_from_child_iframe()
        assert parental_text == "Parent frame" and child_text == "Child Iframe",\
            "There aren`t messages 'Parent frame' & 'Child Iframe' present on page"
        Utils.switch_to_default_content()
        alert_page.click_button_frames_nav_menu()
        assert frames_page.is_page_open() == True, 'Page with Frames form isn`t open'
        frames_page.switch_to_first_iframe()
        first_text = frames_page.find_text_from_first_iframe()
        Utils.switch_to_default_content()
        frames_page.switch_to_second_iframe()
        second_text = frames_page.find_text_from_second_iframe()
        assert first_text == second_text, "Message from upper frame isn`t equal to the message from lower frame"
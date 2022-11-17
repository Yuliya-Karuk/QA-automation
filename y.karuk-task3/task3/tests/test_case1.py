from task3.pages.main_page import main_page
from task3.pages.alert_page import alert_page
from task3.utils.alert import Alert


class Test:
    def test_case(self, setup):
        assert main_page.is_page_open() == True, 'Main page isn`t open '
        main_page.click_box_alert()
        alert_page.click_button_alert_nav_menu()
        alert_page.click_button_to_see_alert()
        assert Alert.check_is_alert_appeared() == True, "Alerts form hasn`t appeared on page "
        assert Alert.capture_text_alert() == "You clicked a button", "Alert with text 'You clicked a button' isn`t open "
        Alert.accept_alert()
        assert Alert.check_is_alert_closed() == True, "Alert hasn`t closed"
        alert_page.click_button_to_see_confirm()
        assert Alert.capture_text_alert() == "Do you confirm action?", "Alert with text 'Do you confirm action? isn`t open"
        Alert.accept_alert()
        assert Alert.check_is_alert_closed() == True, "Alert hasn`t closed"
        assert alert_page.find_text_after_confirm() == "You selected Ok", "Text 'You selected Ok' has appeared on page"
        alert_page.click_button_to_see_prompt()
        assert Alert.capture_text_alert() == "Please enter your name", "Alert with text 'Please enter your name' isn`t open"
        sent_keys = Alert.send_keys_to_prompt()
        assert Alert.check_is_alert_closed() == True, "Alert hasn`t closed"
        assert sent_keys == alert_page.find_text_after_prompt() , "Appeared text equals to the one you've entered before"
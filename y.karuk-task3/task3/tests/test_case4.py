from task3.pages.main_page import main_page
from task3.pages.navigation_form import NavForm
from task3.pages.browser_windows_page import browser_windows_page
from task3.utils.window import Window
from task3.pages.links_page import links_page
from task3.pages.alert_page import alert_page


class Test:
    def test_case(self, setup):
        assert main_page.is_page_open() == True, 'Main page isn`t open '
        main_page.click_box_alert()
        alert_page.click_button_browser_windows_nav_menu()
        assert browser_windows_page.is_page_open() == True, 'Page with Browser Windows form isn`t open'
        browser_windows_page.open_new_tab()
        original_tab = Window.find_current_window()
        Window.switch_to_other_tab(original_tab)
        assert Window.new_tab_is_open(original_tab) == True, "New tab with sample page isn`t open"
        Window.close_tab_and_switch_to_original(original_tab)
        assert browser_windows_page.is_page_open() == True, 'Page with Browser Windows form isn`t open'
        browser_windows_page.click_main_button_element_nav_menu()
        browser_windows_page.click_button_links_nav_menu()
        assert links_page.is_page_open() == True, 'Links page isn`t open '
        links_page.click_link_home()
        Window.switch_to_other_tab(original_tab)
        assert Window.new_tab_is_open(original_tab) == True and main_page.is_page_open() == True, 'New tab with main page isn`t open'
        new_tab = Window.find_current_window()
        Window.switch_to_other_tab(new_tab)
        assert links_page.is_page_open() == True, 'Links page isn`t open '
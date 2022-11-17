from pages.main_page import MainPage
from pages.topsellers_page import TopPage
from pages.game_page import GamePage
from utils.work_with_json import DataJson


class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Test_task2(MainPage, TopPage, GamePage, metaclass=Singleton):
    def __init__(self, browser):
        self.browser = browser


def test_2(browser):

    page = Test_task2(browser)

    assert page.check_is_open_main_page(), "Main page isn`t opened"

    page.click_button_in_popup(page.noteworthy_popup, page.button_top_sellers)
    assert page.check_is_open_top_page(), "Page with Top Sellers products isn`t opened"

    checkbox_1 = DataJson.finding_value_from_json('../config/test_data.json', "Narrow by OS")
    page.open_check_box_panel(checkbox_1)
    assert page.check_box(checkbox_1), "Chechkbox 'SteamOS + Linux' isn`t ticked"

    checkbox_2 = DataJson.finding_value_from_json('../config/test_data.json', "Narrow by number of players")
    page.open_check_box_panel(checkbox_2)
    assert page.check_box(checkbox_2), "Checkbox 'LAN Co-op' isn`t ticked"

    checkbox_3 = DataJson.finding_value_from_json('../config/test_data.json', "Narrow by tag")
    page.open_check_box_panel(checkbox_3)
    assert page.check_box_tag(checkbox_3), "Checkbox 'Action' isn`t checked;"

    assert page.comparing_searching_results() == True, \
        "Number of results isn`t matching your search equals to number of games in games list"

    list_1 = page.finding_data_about_game()

    page.go_to_first_searching_gamepage()
    assert page.check_is_open_game_page(), "Page with game's description isn`t open"

    list_2 = page.find_data_from_game_page()

    assert list_1 == list_2, \
        "Game's data from game page (name, release date and price) aren`t equal to data from Top Sellers page "


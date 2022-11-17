from pages.main_page import MainPage
from pages.base_page import BasePage
from pages.community_market_page import CommunityMarket
from pages.items_page import ItemPage
from utils.work_with_json import DataJson

class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Test_task3(BasePage, MainPage, CommunityMarket, ItemPage, metaclass=Singleton):
    def __init__(self, browser):
        self.browser = browser



def test_2(browser):
    page = Test_task3(browser)

    assert page.check_is_open_main_page(), "Main page isn`t opened"

    page.click_button_in_popup(page.community_popup, page.link_to_market_page)
    assert page.check_is_open_community_market_page(), "Community Market page isn`t open "

    page.advanced_search_window()
    assert page.check_is_open_advanced_search_window(), "'SEARCH COMMUNITY MARKET' window isn`t open"

    filter_1 = DataJson.finding_value_from_json('../config/test_data.json', "Game")
    filter_2 = DataJson.finding_value_from_json('../config/test_data.json', "Hero")
    filter_3 = DataJson.finding_value_from_json('../config/test_data.json', "Rarity")
    filter_4 = DataJson.finding_value_from_json('../config/test_data.json', "Search")
    page.finding_game(filter_1)
    page.choose_hero_game(filter_2)
    page.choose_rarity_game(filter_3)
    page.search_by_text(filter_4)
    page.click_submit_advanced_search()

    '''I use a separate locator for the Dota filter, because I can't generate it like for other filters. 
    Therefore, a separate method was also created to remove the Dota filter'''
    assert page.compare_matching_filters(page.filter_dota, [filter_2, filter_3, filter_4]),\
        "Filters 'Dota 2', 'Lifestealer', 'Immortal', 'golden' haven`t appeared on the page"


    assert page.check_finding_games(filter_4) == True, "Top 5 results don`t contain word 'Golden' in their names."

    url_1 = page.find_url(browser)
    page.remove_filter(filter_4)
    page.remove_filter_dota(page.filter_dota)
    url_2 = page.find_url(browser)
    assert url_1 != url_2, "List of items hasn`t been updated"

    game_number = DataJson.finding_value_from_json('../config/test_data.json', "game_number")
    name_game_1 = page.finding_name_game_community_page(game_number)
    page.go_to_item_page(game_number)
    assert page.check_is_open_item_page(), "Item's page isn`t open"

    assert page.finding_filters([filter_1, filter_2, filter_3]) == True, "Item's data (game, hero, rarity) aren`t equals to the ones set in step"

    name_game_2 = page.finding_game_name_item_page()
    assert name_game_1 == name_game_2, "Item's name doesn`t equal to its' name from previous page"




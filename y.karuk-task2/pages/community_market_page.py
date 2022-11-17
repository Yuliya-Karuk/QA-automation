from pages.base_page import BasePage
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from utils.work_with_json import DataJson




class CommunityMarket():
    base_wait_time = DataJson.finding_value_from_json('../config/config_data.json', 'wait_time')
    community_market_unique_element = "//div[@id='moreInfo']//a[@href='https://steamcommunity.com/market/faq/']"
    advanced_search_button = "//div[@id='market_search_advanced_show']"
    header_advanced_search_window = "//div[@class='title_text']"
    advanced_search_window = "//div[@class='option']"
    all_games_fild = "//div[@class='option']"
    hero_select = "//select[contains(@name, 'Hero')]"
    advanced_search_box_search = "//input[@id='advancedSearchBox']"
    advanced_search_box_submit = "//div[contains(@class, 'btn_medium') and contains(@onclick, 'submit')]"
    filter_dota = "//div[contains(@class, 'results_header')]//a[contains(text(), '')][1]"
    results_advanced_search = "//span[contains(@id, 'result')]"
    find_item_search_value = "//input[@value='golden']"


    def check_is_open_community_market_page(self):
        return WebDriverWait(self.browser, self.base_wait_time).until(
            EC.presence_of_element_located((By.XPATH, self.community_market_unique_element)))

    def advanced_search_window(self):
        button = WebDriverWait(self.browser, self.base_wait_time).until(
                EC.element_to_be_clickable((By.XPATH, self.advanced_search_button)))
        button.click()

    def check_is_open_advanced_search_window(self):
        return WebDriverWait(self.browser, self.base_wait_time).until(
            EC.presence_of_element_located((By.XPATH, self.header_advanced_search_window)))

    def finding_game(self, game):
        game_name_locator = f"//div[contains(@class, 'popup_menu_item')]//img[@alt='{game}']"
        menu = WebDriverWait(self.browser, self.base_wait_time).until(
                EC.presence_of_element_located((By.XPATH, self.all_games_fild)))
        menu.click()
        game = WebDriverWait(self.browser, self.base_wait_time).until(
                EC.presence_of_element_located((By.XPATH, game_name_locator)))
        game.click()

    def choose_hero_game(self, hero_name):
        select = Select(WebDriverWait(self.browser, self.base_wait_time).until(
                EC.presence_of_element_located((By.XPATH, self.hero_select))))
        select.select_by_visible_text(hero_name)
        return

    def choose_rarity_game(self, rarity):
        game_rarity_locator = f"//input[contains(@id, 'Rarity_{rarity}')]"
        check_point = WebDriverWait(self.browser, self.base_wait_time).until(
            EC.presence_of_element_located((By.XPATH, game_rarity_locator)))
        check_point.click()

    def search_by_text(self, search_text):
        search_line = WebDriverWait(self.browser, self.base_wait_time).until(
            EC.presence_of_element_located((By.XPATH, self.advanced_search_box_search)))
        search_line.send_keys(search_text)

    def click_submit_advanced_search(self):
        button = WebDriverWait(self.browser, self.base_wait_time).until(
            EC.presence_of_element_located((By.XPATH, self.advanced_search_box_submit)))
        button.click()

    def compare_matching_filters(self, dota_locator, list_of_filters):
        list_of_locators = [dota_locator]
        for i in list_of_filters:
            filter_locator = f"//div[contains(@class, 'results_header')]//a[contains(text(), '{i}')]"
            list_of_locators.append(filter_locator)
        for i in list_of_locators:
            try:
                WebDriverWait(self.browser, self.base_wait_time).until(
                    EC.presence_of_element_located((By.XPATH, i)))
            except:
                return False
        return True

    def check_finding_games(self, text):
        list_names = []
        for i in range(1, 6):
            locator = f"//a[contains(@id, 'result')][{i}]//span[contains(@id, 'result')]"
            text_element = BasePage.find_text_from_element(self, self.browser, locator)
            place_of_text = text_element.find(text)
            list_names.append(place_of_text)
        for i in list_names:
            if i >= 0:
                pass
            else:
                return False
        return True

    def remove_filter(self, filter):
        locator_remove = f"//div[contains(@class, 'results_header')]//a[contains(text(), '{filter}')]//span[@class='removeIcon']"
        filter_remove_button = WebDriverWait(self.browser, self.base_wait_time).until(
            EC.presence_of_element_located((By.XPATH, locator_remove)))
        filter_remove_button.click()

    def remove_filter_dota(self, locator_remove):
        filter_remove_button = WebDriverWait(self.browser, self.base_wait_time).until(
            EC.presence_of_element_located((By.XPATH, locator_remove)))
        filter_remove_button.click()

    def finding_name_game_community_page(self, number):
        locator_searching_game = f"//div[contains(@id, 'searchResultsRows')]//a[{number}]//span[contains(@class, 'item_name')]"
        game_name = BasePage.find_text_from_element(self, self.browser, locator_searching_game)
        return game_name

    def go_to_item_page(self, number):
        locator = f"//a[contains(@id, 'result')][{number}]"
        button = WebDriverWait(self.browser, self.base_wait_time).until(
                EC.element_to_be_clickable((By.XPATH, locator)))
        button.click()










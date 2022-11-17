from pages.base_page import BasePage
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.work_with_json import DataJson


class ItemPage():
    base_wait_time = DataJson.finding_value_from_json('../config/config_data.json', 'wait_time')
    item_page_unique_element = "//div[@id='pricehistory']"
    name_game_item_page = "//div[@id='mainContents']//h1[contains(@class, 'item_name')]"
    filter_name_game_item_page = "//div[@id='mainContents']//div[contains(@id, 'game_name')]"
    filter_name_game_rarity_page = "//div[@id='mainContents']//div[contains(@id, 'item_type')]"
    filter_hero_item_page = "//div[@id='mainContents']//div[@class= 'descriptor'][1]"


    def check_is_open_item_page(self):
        return WebDriverWait(self.browser, self.base_wait_time).until(
                EC.presence_of_element_located((By.XPATH, self.item_page_unique_element)))

    def finding_game_name_item_page(self):
        game_name = BasePage.find_text_from_element(self, self.browser, self.name_game_item_page)
        return game_name

    def finding_filters(self, list_of_filter):
        list_names = []
        game_filter = BasePage.find_text_from_element(self, self.browser, self.filter_name_game_item_page)
        hero_filter = BasePage.find_text_from_element(self, self.browser, self.filter_hero_item_page)
        rarity_filter = BasePage.find_text_from_element(self, self.browser, self.filter_name_game_rarity_page)
        list_of_filters_item_page = [game_filter, hero_filter, rarity_filter]
        for i in range(3):
            place_of_text = list_of_filters_item_page[i].find(list_of_filter[i])
            list_names.append(place_of_text)
        for i in list_names:
            if i >= 0:
                pass
            else:
                return False
        return True




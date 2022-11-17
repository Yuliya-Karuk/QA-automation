from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.utils import Utils
from utils.work_with_json import DataJson


class GamePage():
    base_wait_time = DataJson.finding_value_from_json('../config/config_data.json', 'wait_time')
    gamepage_unique_element = "//div[@class='game_description_snippet']"
    name_game_page_game = "//div[@id='appHubAppName']"
    release_date_page_game = "//div[@class='release_date']//div[@class='date']"
    price_page_game = "//div[contains(@class, 'game_purchase_price')]"


    def check_is_open_game_page(self):
        return WebDriverWait(self.browser, self.base_wait_time).until(
                EC.presence_of_element_located((By.XPATH, self.gamepage_unique_element)))

    def find_data_from_game_page(self):
        game_name = BasePage.find_text_from_element(self, self.browser, self.name_game_page_game)
        release_date = BasePage.find_text_from_element(self, self.browser, self.release_date_page_game)
        price_string = BasePage.find_text_from_element(self, self.browser, self.price_page_game)
        price_number = Utils.find_number_from_string(price_string)
        list_data = [game_name, release_date, price_number]
        return list_data
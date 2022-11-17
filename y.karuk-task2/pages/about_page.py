from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.utils import Utils
from utils.work_with_json import DataJson

class AboutPage():
    about_page_unique_element = "//div[@class='about_subtitle']"
    number_gamers_online = "//div[contains(@class, 'gamers_online')]/parent::div"
    number_gamers_in_game = "//div[contains(@class, 'gamers_in_game')]/parent::div"
    link_to_main_page = "//div[@class='supernav_container']//a[@href='https://store.steampowered.com/?snr=1_14_4__global-header']"
    base_wait_time = DataJson.finding_value_from_json('../config/config_data.json', 'wait_time')

    def check_is_open_about_page(self):
        return WebDriverWait(self.browser, self.base_wait_time).until(
                EC.presence_of_element_located((By.XPATH, self.about_page_unique_element)))

    def find_gamers_online(self):
        gamers_online_text = BasePage.find_text_from_element(self, self.browser, self.number_gamers_online)
        gamers_online_number = Utils.find_digit_from_string(gamers_online_text)
        return int(gamers_online_number)

    def find_gamers_in_game(self):
        gamers_in_game_text = BasePage.find_text_from_element(self, self.browser, self.number_gamers_in_game)
        gamers_in_game_number = Utils.find_digit_from_string(gamers_in_game_text)
        return int(gamers_in_game_number)

    def go_to_other_page(self, locator):
        button = WebDriverWait(self.browser, self.base_wait_time).until(
                EC.element_to_be_clickable((By.XPATH, locator)))
        button.click()
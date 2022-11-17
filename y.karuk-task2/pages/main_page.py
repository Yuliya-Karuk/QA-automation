from pages.base_page import BasePage
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from utils.work_with_json import DataJson

class MainPage():
    base_wait_time = DataJson.finding_value_from_json('../config/config_data.json', 'wait_time')
    main_page_unique_element = "//div[@class='home_page_gutter']"
    link_to_about_page = "//div[@class='supernav_container']//a[contains(@href, 'about')]"
    noteworthy_popup = "//div[@id='noteworthy_tab']"
    button_top_sellers = "//div[@id='noteworthy_flyout']//a[1]"
    community_popup = "//div[@class='content']//a[@data-tooltip-content='.submenu_community']"
    link_to_market_page = "//div[@class='content']//a[@href='https://steamcommunity.com/market/']"


    def check_is_open_main_page(self):
        return WebDriverWait(self.browser, self.base_wait_time).until(
                EC.presence_of_element_located((By.XPATH, self.main_page_unique_element)))

    def go_to_about_page(self):
        button = WebDriverWait(self.browser, self.base_wait_time).until(
                EC.element_to_be_clickable((By.XPATH, self.link_to_about_page)))
        button.click()


    def click_button_in_popup(self, locator_menu, locator_link):
        button_menu = WebDriverWait(self.browser, self.base_wait_time).until(
                EC.presence_of_element_located((By.XPATH, locator_menu)))
        action = ActionChains(self.browser).move_to_element(button_menu)
        action.perform()
        link_button = WebDriverWait(self.browser, self.base_wait_time).until(
                EC.visibility_of_element_located((By.XPATH, locator_link)))
        link_button.click()

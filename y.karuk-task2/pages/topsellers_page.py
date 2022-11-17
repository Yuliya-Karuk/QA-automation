from pages.base_page import BasePage
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.utils import Utils
from utils.work_with_json import DataJson
from selenium.common.exceptions import NoSuchElementException




class TopPage():
    base_wait_time = DataJson.finding_value_from_json('../config/config_data.json', 'wait_time')
    top_page_unique_element = "//div[@class='search_results_filtered_warning']"
    tag_suggest_line = "//input[@id='TagSuggest']"
    search_result_row = "//div[contains(@id, 'search_results') and not(contains(@class, 'collapsed'))][1]/div[1]"
    link_on_searching_game = "//a[contains(@class, 'ds_collapse_flag')]"
    name_first_searching_game = "//div[contains(@id, 'search_resultsRows')]//a[1]//span[@class='title']"
    release_date_first_searching_game = "//div[contains(@id, 'search_resultsRows')]//a[1]//div[contains(@class, 'search_released')][1]"
    price_first_searching_game = "//div[contains(@id, 'search_resultsRows')]//a[1]//div[contains(@class, 'search_price') and not(contains(@class, 'discount'))]"
    link_first_searching_game = link_on_searching_game + '[1]'

    def check_is_open_top_page(self):
        return WebDriverWait(self.browser, self.base_wait_time).until(
                EC.presence_of_element_located((By.XPATH, self.top_page_unique_element)))


    '''method that reveals the checkbox panel if it is hidden'''
    def open_check_box_panel(self, list_json):
        panel_visible_popup_locator = f"//div[@data-collapse-name={list_json[0]}]/div[2]"
        panel_name_for_click_locator = f"//div[@data-collapse-name={list_json[0]}]/div[1]"
        try:
            WebDriverWait(self.browser, self.base_wait_time).until(
                EC.visibility_of_element_located((By.XPATH, panel_visible_popup_locator)))
        except:
            panel_name = WebDriverWait(self.browser, self.base_wait_time).until(
                EC.presence_of_element_located((By.XPATH, panel_name_for_click_locator)))
            panel_name.click()


    def check_box(self, list_json):
        check_box_locator = f"//span[@data-loc={list_json[1]}]//span[contains(@class, 'checkbox')]"
        check_point = WebDriverWait(self.browser, self.base_wait_time).until(
            EC.presence_of_element_located((By.XPATH, check_box_locator)))
        action = ActionChains(self.browser).move_to_element(check_point).perform()
        check_point.click()
        check_box_checked_locator = f"//div[@data-loc={list_json[1]} and contains(@class,'checked')]"
        return WebDriverWait(self.browser, self.base_wait_time).until(
            EC.presence_of_element_located((By.XPATH,  check_box_checked_locator)))


    def check_box_tag(self, list_json):
        check_box_locator = f"//span[@data-loc={list_json[1]}]//span[contains(@class, 'checkbox')]"
        try:
            check_point = WebDriverWait(self.browser, self.base_wait_time).until(
                EC.presence_of_element_located((By.XPATH, check_box_locator)))
        except NoSuchElementException:
            searching_tag_line = WebDriverWait(self.browser, self.base_wait_time).until(
                EC.presence_of_element_located((By.XPATH, self.tag_suggest_line)))
            searching_tag_line.send_keys(list_json[1])
        check_point = WebDriverWait(self.browser, self.base_wait_time).until(
            EC.presence_of_element_located((By.XPATH, check_box_locator)))
        action = ActionChains(self.browser)
        action.move_to_element(check_point).click().perform()
        check_box_checked_locator = f"//div[@data-loc={list_json[1]} and contains(@class,'checked')]"
        return WebDriverWait(self.browser, self.base_wait_time).until(
                EC.presence_of_element_located((By.XPATH, check_box_checked_locator)))



    def comparing_searching_results(self):
        visibility_searching_line = WebDriverWait(self.browser, self.base_wait_time).until(
                EC.visibility_of_element_located((By.XPATH, self.search_result_row)))
        text_from_searching_line = BasePage.find_text_from_element(self, self.browser, self.search_result_row)
        number_from_searching_line = Utils.find_digit_from_string(text_from_searching_line)
        list_of_games = WebDriverWait(self.browser, self.base_wait_time).until(
                EC.presence_of_all_elements_located((By.XPATH, self.link_on_searching_game)))
        counter = 0
        for i in list_of_games:
            counter = counter + 1
        return number_from_searching_line == counter


    def finding_data_about_game(self):
        game_name = BasePage.find_text_from_element(self, self.browser, self.name_first_searching_game)
        release_date = BasePage.find_text_from_element(self, self.browser, self.release_date_first_searching_game)
        price_string = BasePage.find_text_from_element(self, self.browser, self.price_first_searching_game)
        price_number = Utils.find_number_from_string(price_string)
        list_data = [game_name, release_date, price_number]
        return list_data

    def go_to_first_searching_gamepage(self):
        button = WebDriverWait(self.browser, self.base_wait_time).until(
                EC.element_to_be_clickable((By.XPATH, self.link_first_searching_game)))
        button.click()
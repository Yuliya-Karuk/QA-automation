from pages.main_page import MainPage
from pages.about_page import AboutPage


class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]



class Test_task1(MainPage, AboutPage, metaclass=Singleton):
    def __init__(self, browser):
        self.browser = browser

def test_1(browser):

    page = Test_task1(browser)
    assert page.check_is_open_main_page(), "It isn`t Main page"
    page.go_to_about_page()
    assert page.check_is_open_about_page(), "It isn`t About page"

    gamers_online = page.find_gamers_online()
    gamers_in_game = page.find_gamers_in_game()

    assert gamers_online > gamers_in_game, "Number of in-game players is more than number of players online"

    page.go_to_other_page(page.link_to_main_page)
    assert page.check_is_open_main_page(), "It isn`t Main page"










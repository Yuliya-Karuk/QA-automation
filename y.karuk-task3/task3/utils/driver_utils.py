from task3.utils.webapp import WebApp


class DriverUtils:
    def __init__(self):
        self.driver = WebApp().get_instance().driver

    def get_driver(self):
        return self.driver

    def go_to_page(self, url):
        self.driver.get(url)

    def maximize(self):
        self.driver.maximize_window()

    def close_driver(self):
        self.driver.close()
        self.driver.quit()

    @staticmethod
    def clear_instance():
        WebApp.del_instance()
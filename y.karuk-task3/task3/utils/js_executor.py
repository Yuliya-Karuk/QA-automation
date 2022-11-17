from task3.utils.driver_utils import DriverUtils


class JS_executor:
    __browser = DriverUtils().get_driver()

    @staticmethod
    def click_element_with_JS(element):
        JS_executor.__browser.execute_script("arguments[0].click();", element)

    @staticmethod
    def scroll_down():
        JS_executor.__browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    @staticmethod
    def set_attribute_with_JS(value, element):
        JS_executor.__browser.execute_script(f"arguments[0].value = '{value}';", element)
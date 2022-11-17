from task3.utils.logger import Logger
from task3.utils.driver_utils import DriverUtils


class Window():
    __browser = DriverUtils().get_driver()

    @staticmethod
    def find_current_window():
        Logger.log("INFO", f'find current window')
        current_window = Window.__browser.current_window_handle
        return current_window

    @staticmethod
    def switch_to_other_tab(previous_window):
        for i in Window.__browser.window_handles:
            if i != previous_window:
                Window.__browser.switch_to.window(i)
                break

    @staticmethod
    def new_tab_is_open(previous_window):
        Logger.log("INFO", f'check new window is open')
        current_window = Window.find_current_window()
        if current_window != previous_window:
            return True
        else:
            return False

    @staticmethod
    def close_tab_and_switch_to_original(original_window):
        Logger.log("INFO", f'close tab and switch to original window')
        Window.__browser.close()
        Window.__browser.switch_to.window(original_window)
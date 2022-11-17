from task3.utils.utils import Utils
from task3.utils.logger import Logger
from task3.utils.driver_utils import DriverUtils


class Alert():
    __browser = DriverUtils().get_driver()

    @staticmethod
    def accept_alert():
        Logger.log("INFO", f'switch and accept alert')
        alert = Alert.__browser.switch_to.alert
        alert.accept()

    @staticmethod
    def capture_text_alert():
        Logger.log("INFO", f'switch and capture text from alert')
        alert = Alert.__browser.switch_to.alert
        text_alert = alert.text
        return text_alert

    @staticmethod
    def send_keys_to_prompt():
        Logger.log("INFO", f'switch and send keys to prompt')
        prompt = Alert.__browser.switch_to.alert
        key = Utils.generate_random_string(8)
        prompt.send_keys(key)
        prompt.accept()
        return key

    @staticmethod
    def check_is_alert_appeared():
        Logger.log("INFO", f'check is alert appeared')
        try:
            alert = Alert.__browser.switch_to.alert
            return True
        except:
            return False

    @staticmethod
    def check_is_alert_closed():
        Logger.log("INFO", f'check is alert closed')
        try:
            alert = Alert.__browser.switch_to.alert
            return False
        except:
            return True
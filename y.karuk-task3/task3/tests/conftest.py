import pytest
from task3.utils.json_manager import DataJson
from task3.utils.driver_utils import DriverUtils
from task3.utils.logger import Logger

Logger.log("INFO", f'start browser')


@pytest.fixture(scope="function")
def setup():
    DriverUtils().maximize()
    url = DataJson.finding_value_from_json('../data/config_data.json', 'url')
    DriverUtils().go_to_page(url)
    yield
    DriverUtils().close_driver()
    DriverUtils.clear_instance()
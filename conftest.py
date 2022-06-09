import json

import allure
import pytest
from allure_commons.types import AttachmentType
from helpers.utils import get_config
from utils.drivers import Drivers

CONFIG_PATH = "config.json"
DEFAULT_WAIT_TIME = 10
SUPPORTED_BROWSERS = ["chrome", "firefox", "edge"]


@pytest.fixture(scope='session')
def config():
    return get_config(config_path=CONFIG_PATH)


@pytest.fixture()
def setup(request, config):
    driver = Drivers.get_driver(config)
    driver.implicitly_wait(config["timeout"])
    request.cls.driver = driver
    before_failed = request.session.testsfailed
    if config["browser"] == "firefox":
        driver.maximize_window()
    yield

    if request.session.testsfailed != before_failed:
        allure.attach(driver.get_screenshot_as_png(),
                      name=request.function.__name__,
                      attachment_type=AttachmentType.PNG)
    driver.quit()

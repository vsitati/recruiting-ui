import json
from selenium.common.exceptions import StaleElementReferenceException


def get_config(config_path):
    config_file = open(config_path)
    return json.load(config_file)


def do_click(element):
    try:
        return element.click()
    except StaleElementReferenceException:
        pass


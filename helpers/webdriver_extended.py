from helpers.utils import get_config
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.event_firing_webdriver import EventFiringWebDriver


class WebDriverExtended(EventFiringWebDriver):
    def __init__(self, driver, event_listener):
        super().__init__(driver, event_listener)
        self.config = get_config(config_path='./config.json')
        self.timeout = self.config.get("timeout")
        self.poll_freq = self.config.get("poll_frequency")
        self.driver = driver

    @staticmethod
    def locator_types():
        return dict(
            id=By.ID,
            class_name=By.CLASS_NAME,
            name=By.NAME,
            xpath=By.XPATH,
            css_selector=By.CSS_SELECTOR
        )

    def open(self, url):
        self.get(url)

    def find_element_by_locator(self, locator):
        # valid_locator_types = ["id", "css_selector", "xpath", "name", "class_name"]

        # if "[" and "]" in locator and "xpath=" not in locator:
        #     locator_type = "xpath"
        #     element = locator
        # elif "xpath=" in locator:
        #     locator_type, element = locator.split("xpath=")
        #     locator_type = "xpath"
        # elif "=" in locator:
        #     locator_type, element = locator.split("=")
        # elif "#" in locator:
        #     locator_type, element = locator.split("#")
        #     locator_type = "id"
        # else:
        #     try:
        #         locator_type, element = locator  # (By.NAME, element)
        #     except ValueError:
        #         locator_type = "id"
        #         element = locator

        # by_locator_type = self.locator_types().get(locator_type)
        locator_type, element = locator
        # try:
        #     return self.find_element(locator_type, element)
        # except Exception as e:
        #     print(e)
        return WebDriverWait(self.driver, self.timeout, poll_frequency=self.poll_freq).until(
            ec.presence_of_element_located((locator_type, element)))

    def find_elements_by_locator(self, locator):
        locator_type, element = locator
        return WebDriverWait(self.driver, self.timeout, poll_frequency=self.poll_freq).until(
            ec.presence_of_all_elements_located((locator_type, element)))

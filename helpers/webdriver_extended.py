from config import Config
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.event_firing_webdriver import EventFiringWebDriver


class WebDriverExtended(EventFiringWebDriver):
    def __init__(self, driver, event_listener):
        super().__init__(driver, event_listener)
        self.config = Config.env_config
        self.timeout = self.config.get("timeout")
        self.poll_freq = self.config.get("poll_frequency")
        self.driver = EventFiringWebDriver(driver, event_listener)

    @staticmethod
    def locator_types():
        """
        A dictionary of all locator types.
        :return: A dictionary of all locator types.
        """
        return dict(
            id=By.ID,
            class_name=By.CLASS_NAME,
            name=By.NAME,
            xpath=By.XPATH,
            css_selector=By.CSS_SELECTOR
        )

    def open(self, url):
        """
        Open any given URL
        :param url: The URL to be navigating too
        """
        self.get(url)

    def find_element_by_locator(self, locator):
        """
        Determine if the selected element is present.
        :param locator: Locator element.
        :return: An instance of the selected element.
        """

        locator_type, element = locator
        return WebDriverWait(self.driver, self.timeout, poll_frequency=self.poll_freq).until(
            ec.presence_of_element_located((locator_type, element)))

    def find_elements_by_locator(self, locator):
        """
        Determine if the selected element is present.
        :param locator: Locator element.
        :return: A list of the selected element instances.
        """
        locator_type, element = locator
        return WebDriverWait(self.driver, self.timeout, poll_frequency=self.poll_freq).until(
            ec.presence_of_all_elements_located((locator_type, element)))

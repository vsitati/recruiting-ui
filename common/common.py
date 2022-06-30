import allure
from config import Config
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By


class Elements:
    quick_search = (By.ID, 'quick_search_input')


class Common(Elements):
    """ In the common class we define all common functionality """
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Opening main page")
    def open(self, url):
        """
        Opens any valid URL
        :param url: The url you navigating too
        :return: Updated driver version
        """
        return self.driver.open(url=url)

    def select_from_dropdown(self, locator, text):
        """
        Select any given option from select type dropdown list
        :param locator: Locator element
        :param text: option from the dropdown
        """
        select = Select(self.driver.find_element_by_locator(locator))
        select.select_by_visible_text(text)

    @staticmethod
    def do_click(element):
        """
        Perform a click on a given element.
        :param element: The element to be clicked on.
        """
        try:
            return element.click()
        except StaleElementReferenceException:
            pass

    @staticmethod
    def get_env_url(info, app):
        endpoint = info.get(app)
        company = info.get("company")
        config = Config.env_config.get("env", {})
        protocol = config[app]['url']['protocol']
        domain = config[app]['url']['domain']
        path = config[app]['endpoints'][endpoint]

        if app == "cx":
            return f"{protocol}://{domain}/{company}{path}"
        else:
            return f"{protocol}://{company}{domain}{path}"

    def is_element_visible(self, locator):
        try:
            return self.driver.find_element_by_locator(locator) and True
        except Exception as e:
            return False

    def get_text(self, locator):
        try:
            return self.driver.find_element_by_locator(locator).text
        except Exception as e:
            return "Text not found"

    def enter_text(self, element, text):
        return self.driver.find_element_by_locator(element).send_keys(text)

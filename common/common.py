import allure
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import StaleElementReferenceException


class Common:
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

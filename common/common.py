import allure
from selenium.webdriver.support.ui import Select


class Common:
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    @allure.step("Opening main page")
    def open(self, url):
        return self.driver.open(url=url)

    def select_from_dropdown(self, locator, text):
        select = Select(self.driver.find_element_by_locator(locator))
        select.select_by_visible_text(text)

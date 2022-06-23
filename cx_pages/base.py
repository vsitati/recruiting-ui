import allure
from common.common import Common


class BasePage(Common):
    def __init__(self, driver):
        super().__init__(driver)

    def get_title(self):
        return self.driver.title

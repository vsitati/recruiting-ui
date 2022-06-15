import allure
from cx_pages.login import Login
from common.common import Common


class BasePage(Login, Common):
    def __init__(self, driver):
        super().__init__(driver)
        # self.driver = driver

    def get_title(self):
        return self.driver.title




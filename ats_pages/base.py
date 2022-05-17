import allure
from ats_pages.login import Login
from ats_pages.left_menus import LeftMenus
from common.common import Common


class BasePage(LeftMenus, Login, Common):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

from selenium.webdriver.common.by import By
from common.common import Common
from test_data.test_data_details import TestData

class Elements:
        auto_rm_01_login = (By.ID, 'loginAs992286')


class UserManagement(Common, Elements):
    def __init__(self, driver):
        super().__init__(driver)

    def do_loginas(self, env_info):
        company = env_info.get("company")
        return self.do_click(self.driver.find_element_by_locator(self.auto_rm_01_login))
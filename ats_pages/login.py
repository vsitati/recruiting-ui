from selenium.webdriver.common.by import By
from ats_pages.base import BasePage


class Elements:
    username_id = (By.ID, 'login')
    password_id = (By.ID, 'password')
    login_btn = (By.ID, 'btnLogin')


class Login(BasePage, Elements):
    def __init__(self, driver):
        super().__init__(driver)

    def do_login(self, config):
        test_url = config["base_url"]
        username = "UFT_RM_01"
        password = "Gators2012"
        self.open(test_url)
        self.driver.find_element_by_locator(self.username_id).send_keys(username)
        self.driver.find_element_by_locator(self.password_id).send_keys(password)
        return self.do_click(self.driver.find_element_by_locator(self.login_btn))

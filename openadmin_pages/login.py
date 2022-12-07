from selenium.webdriver.common.by import By
from test_data.test_data_details import TestingData
from common.common import Common

class Elements:
    username_id = (By.ID, 'login')
    password_id = (By.ID, 'password')
    login_btn = (By.CLASS_NAME, 'ui-btn')


class Login(Common, Elements):
    def __init__(self, driver):
        super().__init__(driver)

    def do_login(self, env_info, cred=None):
        company = env_info.get("company")
        username, password = TestingData.data[company]["users"]["open_admin"]
        if cred:
            if cred.get("username", ""):
                username = cred.get("username", "")
            if cred.get("password", ""):
                password = cred.get("password", "")

        self.open_url(self.get_env_url(info=env_info, app="ats"))
        self.driver.find_element_by_locator(self.username_id).send_keys(username)
        self.driver.find_element_by_locator(self.password_id).send_keys(password)
        return self.do_click(self.driver.find_element_by_locator(self.login_btn))

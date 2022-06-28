from selenium.webdriver.common.by import By
from ats_pages.base import BasePage
from test_data.test_data_details import TestData


class Elements:
    username_id = (By.ID, 'login')
    password_id = (By.ID, 'password')
    login_btn = (By.ID, 'btnLogin')
    login_error = (By.CSS_SELECTOR, '.sr-login-error')


class Login(BasePage, Elements):
    def __init__(self, driver):
        super().__init__(driver)

    def do_login(self, env_info, cred=None):
        user_role = env_info.get("user_role")
        company = env_info.get("company")
        username, password = TestData.data[company]["users"][user_role]
        if cred:
            if cred.get("username", ""):
                username = cred.get("username", "")
            if cred.get("password", ""):
                password = cred.get("password", "")

        self.open(self.get_env_url(info=env_info, app="ats"))
        self.driver.find_element_by_locator(self.username_id).send_keys(username)
        self.driver.find_element_by_locator(self.password_id).send_keys(password)
        return self.do_click(self.driver.find_element_by_locator(self.login_btn))

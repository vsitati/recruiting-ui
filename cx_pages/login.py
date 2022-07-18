import allure
from cx_pages.base import BasePage
from selenium.webdriver.common.by import By
from test_data.test_data_details import TestData


class Elements:
    username_id = (By.ID, 'Admin_AdminLogin_EmailAddress')
    password_id = (By.ID, 'Admin_AdminLogin_Password')
    sign_in_btn = (By.ID, 'Admin_AdminLogin_SubmitButton')


class Login(BasePage, Elements):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.title("CX Career Site Login")
    def do_login(self, env_info):
        user_role = env_info.get("user_role")
        company = env_info.get("company")
        username, password = TestData.data[company]["users"][user_role]
        self.open_url(self.get_env_url(info=env_info, app="cx"))

        self.driver.find_element_by_locator(self.username_id).send_keys(username)
        self.driver.find_element_by_locator(self.password_id).send_keys(password)
        return self.do_click(self.driver.find_element_by_locator(self.sign_in_btn))

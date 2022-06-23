import allure
from cx_pages.base import BasePage
from selenium.webdriver.common.by import By


class Elements:
    username_id = (By.ID, 'Admin_AdminLogin_EmailAddress')
    password_id = (By.ID, 'Admin_AdminLogin_Password')
    sign_in_btn = (By.ID, 'Admin_AdminLogin_SubmitButton')


class Login(BasePage, Elements):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.title("CX Career Site Login")
    def do_login(self, config):
        test_url = config["base_cx_url"]
        username = "UFT_RM_01"
        password = "Gators2012"
        self.open(test_url)

        self.driver.find_element_by_locator(self.username_id).send_keys(username)
        self.driver.find_element_by_locator(self.password_id).send_keys(password)
        return self.do_click(self.driver.find_element_by_locator(self.sign_in_btn))

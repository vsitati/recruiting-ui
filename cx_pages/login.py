import allure
from helpers.utils import do_click
from selenium.webdriver.common.by import By


class Elements:
    username_id = (By.ID, 'Admin_AdminLogin_EmailAddress')
    password_id = (By.ID, 'Admin_AdminLogin_Password')
    sign_in_btn = (By.ID, 'Admin_AdminLogin_SubmitButton')


class Login(Elements):
    def __init__(self, driver):
        self.driver = driver

    @allure.title("CX Career Site Login")
    def do_login(self, username, password):
        self.driver.find_element_by_locator(self.username_id).send_keys(username)
        self.driver.find_element_by_locator(self.password_id).send_keys(password)
        return do_click(self.driver.find_element_by_locator(self.sign_in_btn))

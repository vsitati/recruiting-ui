import allure
from helpers.utils import do_click
from selenium.webdriver.common.by import By


class Elements:
    username_id = (By.ID, 'login')
    password_id = (By.ID, 'password')
    login_btn = (By.ID, 'btnLogin')


class Login(Elements):
    def __init__(self, driver):
        self.driver = driver

    def do_login(self, username, password):
        self.driver.find_element_by_locator(self.username_id).send_keys(username)
        self.driver.find_element_by_locator(self.password_id).send_keys(password)
        return do_click(self.driver.find_element_by_locator(self.login_btn))

from ats_pages.base import BasePage
from selenium.webdriver.common.by import By


class Elements:
    heading = (By.TAG_NAME, "H3")
    new_password = (By.ID, "candidatepassword")
    confirm_new_password = (By.ID, "candidateconfirmpassword")


class ChangePassword(BasePage, Elements):
    def __init__(self, driver):
        super().__init__(driver)

    def change_password(self, new_password, confirm_password):
        self.driver.find_element_by_locator(self.new_password).send_keys(new_password)
        self.driver.find_element_by_locator(self.confirm_new_password).send_keys(confirm_password)
        return self.click_submit_btn()


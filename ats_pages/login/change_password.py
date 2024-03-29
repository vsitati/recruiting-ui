from common.common import Common
from selenium.webdriver.common.by import By


class Elements:
    heading = (By.TAG_NAME, "H3")
    new_password = (By.ID, "candidatepassword")
    confirm_new_password = (By.ID, "candidateconfirmpassword")
    mismatch_passwords = (By.CSS_SELECTOR, ".alert.alert-danger")
    success_message = (By.CSS_SELECTOR, ".alert.alert-success")


class ChangePassword(Common, Elements):
    def __init__(self, driver):
        super().__init__(driver)

    def do_change_password(self, new_password, confirm_password):
        self.driver.find_element_by_locator(self.new_password).send_keys(new_password)
        self.driver.find_element_by_locator(self.confirm_new_password).send_keys(confirm_password)
        return self.click_submit_btn()

    def get_mismatched_text(self):
        return self.driver.find_element_by_locator(self.mismatch_passwords).text

    def get_password_change_success_msg(self):
        return self.driver.find_element_by_locator(self.success_message).text

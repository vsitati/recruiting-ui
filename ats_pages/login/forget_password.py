from selenium.webdriver.common.by import By
from common.common import Common
from test_data.test_data_details import SrTestData


class Elements:
    username = (By.ID, 'username')
    submit_btn = (By.ID, 'submitButton')
    return_to_login = (By.ID, 'returnToLoginLink')
    forget_password_instruction_text = (By.ID, "forgotPasswordInstructionText")
    heading = (By.TAG_NAME, "H3")
    empty_field_error = (By.ID, "username-error")
    acc_verification_heading = (By.XPATH, ".//span[@class = 'sr-product-logo']")
    account_verification_text = (By.CSS_SELECTOR, ".alert.alert-info")


class ForgetPassword(Common, Elements):
    def __init__(self, driver):
        super().__init__(driver)

    def verify_instruction_text(self):
        instruction_text = self.get_text(self.forget_password_instruction_text)
        test_data_text = SrTestData.forget_password_text
        return instruction_text == test_data_text

    def forget_password_heading(self):
        return self.driver.find_element_by_locator(self.heading).text

    def account_verification_heading(self):
        return self.driver.find_element_by_locator(self.acc_verification_heading).text

    def verify_account_verification_text(self):
        return self.driver.find_element_by_locator(self.account_verification_text).text

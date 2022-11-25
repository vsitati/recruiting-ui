import allure
from common.common import Common
from selenium.webdriver.common.by import By


class Elements:
    firstname = (By.ID, 'Apply_ApplyToJob_FirstName')
    lastname = (By.ID, 'Apply_ApplyToJob_LastName')
    email = (By.ID, 'Apply_ApplyToJob_Email')
    choose_file_btn = (By.ID, 'Apply_ApplyToJob_File')
    apply_btn = (By.ID, 'Apply_ApplyToJob_SubmitButton')
    apply_success_heading = (By.ID, "Apply_Success_PageHeading")
    apply_success_page_text = (By.ID, "Apply_Success_PageText")
    continue_btn = (By.ID, "Apply_Success_ExternalLink")


class QuickApply(Common, Elements):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Fill in Quick Apply Form')
    def fill_in_quick_apply_form(self, firstname, lastname, email, file_path):
        self.driver.find_element_by_locator(self.firstname).send_keys(firstname)
        self.driver.find_element_by_locator(self.lastname).send_keys(lastname)
        self.driver.find_element_by_locator(self.email).send_keys(email)
        self.driver.find_element_by_locator(self.choose_file_btn).send_keys(file_path)
        apply_elem = self.driver.find_element_by_locator(self.apply_btn)
        self.driver.execute_script("arguments[0].scrollIntoView();", apply_elem)
        self.do_click(apply_elem)


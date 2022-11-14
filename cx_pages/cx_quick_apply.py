import allure
from cx_pages.base import BasePage
from selenium.webdriver.common.by import By



class Elements:
    AdminLogin = (By.ID, 'SuperAdmin_AdminLogin_EmailAddress')
    password = (By.ID, 'SuperAdmin_AdminLogin_Password')
    lucee_site = (By.ID, 'SuperAdmin_CustomerLogin-luceeqa01')
    qa_visibility = (By.CLASS_NAME, 'sr-career-site-list-banner')
    job_list = (By.ID, 'Jobs_PagedJobList_Job-171786')
    apply_link = (By.ID, 'Jobs_JobDetail_ApplyLink')
    pre_submission = (By.ID, 'Apply_ApplyToJob_PresubmissionText_Accept')
    firstname = (By.ID, 'Apply_ApplyToJob_FirstName')
    lastname = (By.ID, 'Apply_ApplyToJob_LastName')
    email = (By.ID, 'Apply_ApplyToJob_Email')
    uploadBtn = (By.ID, 'Apply_ApplyToJob_File')
    submit_btn = (By.ID, 'Apply_ApplyToJob_SubmitButton')


class QuickApply(BasePage, Elements):
    def __init__(self, driver):
        super().__init__(driver)

    def test_main(self):
        self.driver.find_element_by_locator(self.AdminLogin).send_keys("auto_rm_01")
        self.driver.find_element_by_locator(self.password).send_keys("@Silkroad@1")
        return self.click_submit_btn()

    @allure.step('Select Lucee Qa')
    def select_lucee_qa01(self):
        self.driver.find_element_by_locator(self.lucee_site).click()

    @allure.step('Qa visibility')
    def select_qa_visibility(self):
        self.driver.find_element_by_locator(self.qa_visibility).click()

    @allure.step('Job List')
    def select_job_to_apply(self):
        self.driver.find_element_by_locator(self.job_list).click()
s
    @allure.step('Click apply')
    def select_click_apply(self):
        self.driver.find_element_by_locator(self.apply_link).click()

    @allure.step('Fill in form')
    def fill_in_form(self):
        self.driver.find_element_by_locator(self.firstname).send_keys("")
        self.driver.find_element_by_locator(self.lastname).send_keys("")
        self.driver.find_element_by_locator(self.email).send_keys("")
        self.driver.find_element_by_locator(self.uploadBtn).click()

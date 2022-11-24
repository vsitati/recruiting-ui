from selenium.webdriver.common.by import By
from common.common import Common


class Elements:
    candidate_name = (By.ID, "candidateFormattedName")
    candidate_email = (By.ID, "candidateEmailAddress")
    job_tracked = (By.ID, "jobTrackedForLink")
    resume_tab = (By.ID, "resumeTab")
    attachment_tab = (By.ID, "attachmentsTab")
    history_tab = (By.ID, "attachmentsTab")


class CandidateResumeProfile(Common, Elements):
    def __init__(self, driver):
        super().__init__(driver)

    def verify_candidate_name(self, candidate_name):
        return self.driver.find_element_by_locator(self.candidate_name).text == candidate_name

    def verify_candidate_email(self, candidate_email):
        return self.driver.find_element_by_locator(self.candidate_email).text == candidate_email

    def open_attachment_tab(self):
        return self.do_click(self.driver.find_element_by_locator(self.attachment_tab))

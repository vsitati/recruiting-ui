from selenium.webdriver.common.by import By
from common.common import Common


class Elements:
    candidate_name = (By.ID, "candidateFormattedName")
    candidate_email = (By.ID, "candidateEmailAddress")
    job_tracked = (By.ID, "jobTrackedForLink")
    resume_tab = (By.ID, "resumeTab")
    attachment_tab = (By.ID, "attachmentsTab")
    history_tab = (By.ID, "attachmentsTab")
    attachments_parent = (By.CSS_SELECTOR, ".lifesuite__table-container")


class CandidateResumeProfile(Common, Elements):
    def __init__(self, driver):
        super().__init__(driver)

    def verify_candidate_name(self):
        return self.driver.find_element_by_locator(self.candidate_name).text

    def verify_candidate_email(self):
        return self.driver.find_element_by_locator(self.candidate_email).text

    def open_attachment_tab(self):
        return self.do_click(self.driver.find_element_by_locator(self.attachment_tab))

    def get_attachment_names(self):
        attachments_text = []
        parent_elems = self.driver.find_elements_by_locator(self.attachments_parent)
        for parent_elem in parent_elems:
            attachments_text += parent_elem.text.split(" ")
            # TODO remove all unwanted text by filter on the file ext
            # TODO Perform a list filter
        return attachments_text

from selenium.webdriver.common.by import By
from common.common import Common


class Elements:
    check_box = (By.CSS_SELECTOR, ".resume-checkbox.bulk-action-item-checkbox")


class CandidateAdvancedSearch(Common, Elements):
    def __init__(self, driver):
        super().__init__(driver)

    def get_check_box_elem(self, candidate_name):
        check_box_elems = self.driver.find_elements_by_locator(self.check_box)
        for check_box_elem in check_box_elems:
            if check_box_elem.get_attribute("data-candidatename") == candidate_name:
                return check_box_elem
        return ""

    def open_candidate_profile(self, candidate_name):
        elem = self.get_check_box_elem(candidate_name=candidate_name)
        resume_id = elem.get_attribute("value")
        return self.open_url(self.get_all_hrefs(specific_href=resume_id))

    def open_job_title(self, candidate_name):
        elem = self.get_check_box_elem(candidate_name=candidate_name)
        job_id = elem.get_attribute("data-jobid")
        return self.open_url(self.get_all_hrefs(specific_href=job_id))

    def select_candidate(self, candidate_name):
        elem = self.get_check_box_elem(candidate_name=candidate_name)
        return self.do_click(elem)

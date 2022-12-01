from selenium.webdriver.common.by import By
from common.common import Common
from helpers.utils import BaseError
import time


class Elements:
    check_box = (By.CSS_SELECTOR, ".resume-checkbox.bulk-action-item-checkbox")
    next_page = (By.ID, "bulkActionItemsPagerButton_next")
    pagination_parent = (By.ID, "bulkActionItemPager")
    pagination_tags = (By.TAG_NAME, "li")


class CandidateAdvancedSearch(Common, Elements):
    def __init__(self, driver):
        super().__init__(driver)

    def get_check_box_elem(self, candidate_name):

        def find_candidate_name(_candidate_name):
            check_box_elems = self.driver.find_elements_by_locator(self.check_box)
            for check_box_elem in check_box_elems:
                if check_box_elem.get_attribute("data-candidatename") == _candidate_name:
                    return check_box_elem

        result = find_candidate_name(_candidate_name=candidate_name)

        if not result:
            pagination_parent_elem = self.driver.find_element_by_locator(self.pagination_parent)
            pagination_parent_elems = pagination_parent_elem.find_elements(*self.pagination_tags)
            total_pages = len(pagination_parent_elems[1:-1]) + 1
            for i in range(total_pages):
                next_page_elem = self.driver.find_element_by_locator(self.next_page)
                self.driver.execute_script("arguments[0].scrollIntoView();", next_page_elem)
                self.do_click(next_page_elem)
                time.sleep(2)
                result = find_candidate_name(_candidate_name=candidate_name)
                if result:
                    return result

        if not result:
            # TODO need to add logging
            raise BaseError(f"Candidate Name: {candidate_name} not found.")
        return result

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

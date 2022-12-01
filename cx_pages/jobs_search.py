import random

from common.common import Common
from selenium.webdriver.common.by import By


class Elements:
    job_search_input_box = (By.ID, 'Jobs_JobSearch_SearchInput')
    page_number = (By.ID, 'Jobs_PagedJobList_CurrentPageText')
    next_page = (By.ID, 'Jobs_PagedJobList_NextLink')
    prev_page = (By.ID, 'Jobs_PagedJobList_PrevPageLink')
    job_titles = (By.CSS_SELECTOR, ".sr-panel__title")
    submit_resume_message = (By.ID, "Jobs_PagedJobList_OpenSubmission")


class JobSearch(Elements, Common):
    def __init__(self, driver):
        super().__init__(driver)

    def get_last_page_index(self):
        page_number_range_elem = self.driver.find_element_by_locator(self.page_number)
        return int(page_number_range_elem.text.split(" ")[-1])

    def find_job(self, title="", random_job=False):
        # TODO Need to enhance random Job apply to page through all pages and not only take a job from the first page
        last_page = self.get_last_page_index()

        def get_title_elem(_title="", _random=False):
            title_elems = self.driver.find_elements_by_locator(self.job_titles)
            if _random:
                title_elem = random.choice([title_elem for title_elem in title_elems])
                return title_elem, title_elem.text
            return [title_elem for title_elem in title_elems if title_elem.text == _title]

        if random_job:
            return get_title_elem(_random=True)
        else:
            result = get_title_elem(_title=title)

        if not result:
            for i in range(last_page):
                next_page_btn_elem = self.driver.find_element_by_locator(self.next_page)
                self.driver.execute_script("arguments[0].click();", next_page_btn_elem)
                result = get_title_elem(_title=title)
                if result:
                    return result[0]
        try:
            return result[0]
        except IndexError:
            return ""

    def open_job(self, job_elem):
        return self.driver.execute_script("arguments[0].click();", job_elem)

    def get_job_search_input_placeholder_text(self):
        elem = self.driver.find_element_by_locator(self.job_search_input_box)
        return elem.get_attribute("placeholder")

    def get_submit_resume_message(self):
        return self.driver.find_element_by_locator(self.submit_resume_message).text

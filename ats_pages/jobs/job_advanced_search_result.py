from common.common import Common
from selenium.webdriver.common.by import By
from test_data.test_data_details import JobData
import time


class Elements:
    result_sheet = (By.ID, 'bulkActionItemResultsTable')
    saved_job_search_name = (By.CSS_SELECTOR, "[id='pageHeader']>div>div>h1")
    filter_label = (By.CSS_SELECTOR, "[id='appliedFilters']>div>h3")
    # check_box = (By.NAME, "bulkActionItemId")
    pagination_parent = (By.ID, "bulkActionItemPager")
    pagination_tags = (By.TAG_NAME, "li")
    next_page = (By.ID, "bulkActionItemsPagerButton_next")
    next_page_tip = (By.CSS_SELECTOR, "[title='Next Page']")


class JobAdvancedSearchResult(Common, Elements):
    def __init__(self, driver):
        super().__init__(driver)

    def verify_is_job_search_result_page(self):
        elm = self.driver.find_element_by_locator(self.saved_job_search_name)
        self.__comparing(elm.text, JobData.job_data.get("saved_job_search_name"))

        elm = self.driver.find_element_by_locator(self.filter_label)
        self.__comparing(elm.text, JobData.job_data.get("filter_label"))

        return

    def open_job(self, internal_job_title):
        def _find_job_name(_job_name):
            all_hrefs = self.get_all_hrefs()
            for elm in all_hrefs:
                if elm.get_attribute("text") == internal_job_title:
                    self.do_click(elm)
                    return True

        # check if result record exists
        elm_result_sheet = self.driver.find_element_by_locator(self.result_sheet)
        elms = elm_result_sheet.find_elements(By.NAME, "bulkActionItemId")
        assert len(elms) != 0, "Job Search returns 0 result."

        result = _find_job_name(internal_job_title)
        if result is not True:
            pagination_parent_elm = self.driver.find_element_by_locator(self.pagination_parent)
            pagination_parent_elms = pagination_parent_elm.find_elements(*self.pagination_tags)
            total_pages = len(pagination_parent_elms[1:-1])
            # if only 1 page, then finish
            if total_pages == 1:
                raise Exception(f"Job Name: {internal_job_title} not found.")

            next_page_elm_tip = self.driver.find_element_by_locator(self.next_page_tip)
            next_page_elm = self.driver.find_element_by_locator(self.next_page)
            while next_page_elm_tip.get_attribute("class") != "active":
                self.do_click(next_page_elm)
                time.sleep(1)
                result = _find_job_name(_job_name=internal_job_title)
                if result is True:
                    return True
            else:
                raise Exception(f"Job Name: {internal_job_title} not found.")

    def __comparing(self, source, target):
        if source == target:
            self.sr_logger.logger.info(f"-- {source} is correct")
            assert source == target
        else:
            self.sr_logger.logger.error(f"@@ {source} is NOT correct")

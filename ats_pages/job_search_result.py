from ats_pages.base import BasePage
from selenium.webdriver.common.by import By
from test_data.test_data_details import JobData


class Elements:
    result_sheet = (By.ID, 'bulkActionItemResultsTable')
    saved_job_search_name = (By.CSS_SELECTOR, "[id='pageHeader']>div>div>h1")
    filter_label = (By.CSS_SELECTOR, "[id='appliedFilters']>div>h3")


class JobSearchResult(BasePage, Elements):
    def __init__(self, driver):
        super().__init__(driver)

    def verify_is_job_search_result_page(self):
        elm = self.driver.find_element_by_locator(self.saved_job_search_name)
        self.__comparing(elm.text, JobData.job_data.get("saved_job_search_name"))

        elm = self.driver.find_element_by_locator(self.filter_label)
        self.__comparing(elm.text, JobData.job_data.get("filter_label"))

        return

    def select_a_result(self, internal_job_title):
        elm = self.driver.find_element_by_locator(self.result_sheet)
        elms = elm.find_elements(By.CSS_SELECTOR, "[data-page='1']>tr>td")
        assert len(elms) != 0, "Job Search returns 0 result."
        for elm in elms:
            if elm.text == internal_job_title:
                self.do_click(elm)
                return
        else:
            assert False, "Job Search results does NOT have {0}".format(internal_job_title)

    def __comparing(self, source, target):
        if source == target:
            self.sr_logger.logger.info(f"-- {source} is correct")
        else:
            self.sr_logger.logger.error(f"@@ {source} is NOT correct")

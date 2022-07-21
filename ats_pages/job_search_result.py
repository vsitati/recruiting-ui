from ats_pages.base import BasePage
from selenium.webdriver.common.by import By


class Elements:
    result_sheet = (By.ID, 'bulkActionItemResultsTable')


class JobSearchResult(BasePage, Elements):
    def __init__(self, driver):
        super().__init__(driver)

    def select_a_result(self, internal_job_title):
        elm = self.driver.find_element_by_locator(self.result_sheet)
        elms = elm.find_elements(By.CSS_SELECTOR, "[data-page='1']>tr>td")
        for elm in elms:
            if elm.text == internal_job_title:
                self.do_click(elm)
                return

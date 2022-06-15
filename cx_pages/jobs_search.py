import allure
from cx_pages.base import BasePage
from selenium.webdriver.common.by import By


class Elements:
    job_search_input_box = (By.ID, 'Jobs_JobSearch_SearchInput')
    page_number = (By.ID, 'Jobs_PagedJobList_CurrentPageText')
    next_page = (By.ID, 'Jobs_PagedJobList_NextLink')
    prev_page = (By.ID, 'Jobs_PagedJobList_PrevPageLink')
    job_titles = (By.CSS_SELECTOR, ".sr-panel__title")


class JobSearch(Elements, BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        # self.driver = driver

    def get_last_page_index(self):
        page_number_range_elem = self.driver.find_element_by_locator(self.page_number)
        return int(page_number_range_elem.text.split(" ")[-1])

    def find_job(self, title):
        last_page = self.get_last_page_index()

        def get_title_elem(_title):
            title_elems = self.driver.find_elements_by_locator(self.job_titles)
            return [title_elem for title_elem in title_elems if title_elem.text == _title]

        result = get_title_elem(_title=title)

        if not result:
            for i in range(last_page):
                next_page_btn_elem = self.driver.find_element_by_locator(self.next_page)
                self.driver.execute_script("arguments[0].click();", next_page_btn_elem)
                result = get_title_elem(_title=title)
                if result:
                    return result[0]
        return result[0]

    def open_job(self, job_elem):
        return self.driver.execute_script("arguments[0].click();", job_elem)

from selenium.webdriver.common.by import By
from ats_pages.base import BasePage


class Elements:
    edit_search = (By.XPATH, "//span[contains(@data-expandlabel, 'Edit Search')]")
    filter_status = (By.ID, "isActive")
    apply_filter_btn = (By.ID, "applyFiltersLabel")


class JobAdvancedSearch(BasePage, Elements):
    def __init__(self, driver):
        super().__init__(driver)

    def click_edit_search(self):
        return self.do_click(self.driver.find_element_by_locator(self.edit_search))

    def select_from_status_dropdown(self, text):
        return self.select_from_dropdown(self.filter_status, text=text)

    def click_apply_filter_btn(self):
        return self.do_click(self.driver.find_element_by_locator(self.apply_filter_btn))

    def filter_by_status(self, text):
        self.click_edit_search()
        self.select_from_status_dropdown(text)
        self.click_apply_filter_btn()

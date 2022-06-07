import allure
from ats_pages.base import BasePage
from helpers.utils import do_click
from selenium.webdriver.common.by import By


class Elements:
    edit_search = (By.XPATH, "//span[contains(@data-expandlabel, 'Edit Search')]")
    filter_status = (By.ID, "isActive")
    apply_filter_btn = (By.ID, "applyFiltersLabel")


class AdvancedSearch(BasePage, Elements):
    def __init__(self, driver):
        super().__init__(driver)

    def click_edit_search(self):
        return do_click(self.driver.find_element_by_locator(self.edit_search))

    def go_to_advanced_search(self):
        self.click_jobs()
        return self.click_jobs_advanced_search()

    def open_edit_search(self):
        self.go_to_advanced_search()
        return self.click_edit_search()

    def select_from_status_dropdown(self, text):
        return self.select_from_dropdown(self.filter_status, text=text)

    def click_apply_filter_btn(self):
        return do_click(self.driver.find_element_by_locator(self.apply_filter_btn))

from common.common import Common
from selenium.webdriver.common.by import By


class Elements:
    apply_filter_btn = (By.ID, "applyFilters")
    clear_filter_btn = (By.ID, "clearFilters")
    # edit_search = (By.XPATH, "//span[contains(@data-expandlabel, 'Edit Search')]")
    edit_search = (By.CSS_SELECTOR, "[data-expandlabel='Edit Search'][data-collapselabel='Hide Filters']")
    candidate_name = (By.ID, "fullName")
    current_stage = (By.ID, "hiringStageId_input")
    entered_in_the_last = (By.ID, "createdDateInterval")
    country = (By.ID, "countryCode_input")
    state = (By.ID, "regionCode")
    recruiting_manager = (By.ID, "recruitingManagerId_input")
    sort_by = (By.ID, "sortBy")
    sort_by_order = (By.ID, "sortByDirection")


class CandidateAdvancedSearchEdit(Common, Elements):
    def __init__(self, driver):
        super().__init__(driver)

    def click_apply_filter_btn(self):
        self.go_click(self.apply_filter_btn)
        return

    def click_clear_filter_btn(self):
        return self.go_click(self.clear_filter_btn)

    def click_edit_search(self):
        return self.do_click(self.driver.find_element_by_locator(self.edit_search))

    def enter_candidate_name(self, name):
        return self.enter_text(self.candidate_name, name)

    def select_current_stage(self, current_stage):
        return self.select_auto_complete(self.current_stage, current_stage)

    def select_country(self, country):
        return self.select_auto_complete(self.country, country)

    def select_state(self, state):
        return self.select_from_dropdown(self.state, state)

    def select_recruiting_manager(self, recruiting_manager):
        return self.select_auto_complete(self.recruiting_manager, recruiting_manager)

    def enter_entered_in_the_last(self, date):
        return self.enter_text(self.entered_in_the_last, date)

    def select_sort_by(self, sort_by):
        self.select_from_dropdown(self.sort_by, sort_by)
        return

    def select_sort_by_order(self, sort_by_order):
        return self.select_from_dropdown(self.sort_by_order, sort_by_order)

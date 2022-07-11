from ats_pages.base import BasePage
from selenium.webdriver.common.by import By


class Elements:
    # Priority
    time_measurement = (By.ID, "datemode")
    no_more_than = (By.ID, "addday")
    no_less_than = (By.ID, "lessday")

    # Buttons
    save_btn = (By.ID, "submitModalPriority")
    close_btn = (By.ID, "priorityDialogModalClose")


class JobPriority(BasePage, Elements):
    def __init__(self, driver):
        super().__init__(driver)

    def fill_out(self):
        # Priority
        self.select_dropdown_element(self.time_measurement, "time_measurement")
        self.enter_text_element(self.no_more_than, "no_more_than")
        self.enter_text_element(self.no_less_than, "no_less_than")

        # Buttons
        self.go_click(self.save_btn)

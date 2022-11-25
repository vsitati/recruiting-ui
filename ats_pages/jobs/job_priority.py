from common.common import Common
from selenium.webdriver.common.by import By
from test_data.test_data_details import JobData


class Elements:
    # Priority
    time_measurement = (By.ID, "datemode")
    no_more_than = (By.ID, "addday")
    no_less_than = (By.ID, "lessday")

    # Buttons
    continue_btn = (By.CSS_SELECTOR, "[type='submit']")
    save_btn = (By.ID, "submitModalPriority")
    close_btn = (By.ID, "priorityDialogModalClose")


class JobPriority(Common, Elements):
    def __init__(self, driver):
        super().__init__(driver)

    def setup_priority(self):
        # Priority
        self.select_from_dropdown(self.time_measurement, JobData.job_data.get("time_measurement"))
        self.enter_text(self.no_more_than, JobData.job_data.get("no_more_than"))
        self.enter_text(self.no_less_than, JobData.job_data.get("no_less_than"))

        # Buttons
        self.go_click(self.continue_btn)

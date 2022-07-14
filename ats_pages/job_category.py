from ats_pages.base import BasePage
from selenium.webdriver.common.by import By
from test_data.test_data_details import JobData


class Elements:
    # Priority
    radio_list = (By.CSS_SELECTOR, "[class='category-radio-list'] [class='categoryRadio']")

    # Buttons
    save_btn = (By.CSS_SELECTOR, ".lifesuite__button.lifesuite__float-right.primary")
    cancel_btn = (By.CSS_SELECTOR, "[class='lifesuite__button lifesuite__float-right']")


class JobCategory(BasePage, Elements):
    def __init__(self, driver):
        super().__init__(driver)

    def select_one(self):
        # Category
        self.click_radio_list(self.radio_list, JobData.job_data.get("radio_list"))

        # Button
        self.go_click(self.save_btn)
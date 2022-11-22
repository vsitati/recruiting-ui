from common.common import Common
from selenium.webdriver.common.by import By
from test_data.test_data_details import JobData


class Elements:
    # Priority
    radio_list_create = (By.CSS_SELECTOR, "[id='categories'] [class='categoryRadio']")
    radio_list_edit = (By.CSS_SELECTOR, "[class='category-radio-list'] [class='categoryRadio']")

    # Buttons
    continue_btn = (By.ID, "jobform4_continue_2")
    save_btn = (By.CSS_SELECTOR, ".lifesuite__button.lifesuite__float-right.primary")
    cancel_btn = (By.CSS_SELECTOR, "[class='lifesuite__button lifesuite__float-right']")


class JobCategory(Common, Elements):
    def __init__(self, driver):
        super().__init__(driver)

    def select_category(self):
        # Category
        self.click_radio_list(self.radio_list_create, JobData.job_data.get("category_radio_list"))

        # Button
        self.go_click(self.continue_btn)

    def update_category(self):
        # Category
        self.click_radio_list(self.radio_list_edit, JobData.job_data.get("category_radio_list_edit"))

        # Button
        self.go_click(self.save_btn)

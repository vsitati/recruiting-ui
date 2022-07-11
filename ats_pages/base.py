from common.common import Common
from test_data.test_data_details import JobData


class BasePage(Common):
    def __init__(self, driver):
        super().__init__(driver)

    def select_dropdown_element(self, locator, text):
        return self.select_from_dropdown(locator, JobData.job_data.get(text))

    def select_multiselect_list_element(self, locator, text):
        return self.select_multiselect_list(locator, JobData.job_data.get(text))

    def enter_text_element(self, locator, text):
        return self.enter_text(locator, JobData.job_data.get(text))

    def enter_richtext_element(self, locator, text):
        self.enter_richtext(locator, JobData.job_data.get(text))

    def enter_richtext_integer_element(self, locator, text):
        self.enter_richtext_integer(locator, JobData.job_data.get(text))

    def click_radio_yes_no_element(self, locator, isYes):
        return self.click_radio_yes_no(locator, JobData.job_data.get(isYes))

    def click_radio_list_element(self, locator, text):
        return self.click_radio_list(locator, JobData.job_data.get(text))

    def check_checkbox_element(self, locator, isCheck):
        return self.checkk_checkbox(locator, JobData.job_data.get(isCheck))

    def pck_datepicker_element(self, locator, text):
        return self.pick_datepicker(locator, JobData.job_data.get(text))

    def select_auto_complete_element(self, locator, text):
        return self.select_auto_complete(locator, JobData.job_data.get(text))

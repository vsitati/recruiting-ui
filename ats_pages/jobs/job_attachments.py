from common.common import Common
from selenium.webdriver.common.by import By
from test_data.test_data_details import JobData


class Elements:
    upload_files_btn = (By.ID, "uploadFilesButton")
    remove_selected_btn = (By.ID, "removeButton")
    check_all_files = (By.ID, "checkAll")
    continue_btn = (By.CSS_SELECTOR, "[type='submit']")
    cancel_btn = (By.XPATH, "//span[.='Cancel']")
    # cancel_btn = (By.CSS_SELECTOR, "div.ui-button-group:nth-child(3) > button:nth-child(1)")

    # Upload Attachments dialog box
    file = (By.ID, "selectedFile")
    description = (By.ID, "fileDescription")
    upload_file_btn = (By.CLASS_NAME, "ui-button-text")


class JobAttachments(Common, Elements):
    def __init__(self, driver):
        super().__init__(driver)

    def upload_file(self):
        self.go_click(self.upload_files_btn)
        elm = self.driver.find_element_by_locator(Elements.file)
        upload_file = JobData.job_data.get("upload_file")
        elm.send_keys(upload_file)

        self.enter_text(self.description, JobData.job_data.get("attachment_description"))
        self.go_click(self.upload_file_btn)

        self.go_click(self.continue_btn)

    def update_file(self):
        self.go_click(self.upload_files_btn)
        elm = self.driver.find_element_by_locator(Elements.file)
        upload_file = JobData.job_data.get("upload_file_edit")
        elm.send_keys(upload_file)

        self.enter_text(self.description, JobData.job_data.get("attachment_description"))
        self.go_click(self.upload_file_btn)

        self.go_click(self.cancel_btn)

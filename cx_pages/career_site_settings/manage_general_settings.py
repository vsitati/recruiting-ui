import allure
from common.common import Common
from functools import partial
from helpers.utils import BaseError
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class Elements:
    active_cbox = (By.ID, "Admin_JobBoardsEdit__JobBoardActive")
    enable_job_alert_cbox = (By.ID, "Admin_JobBoardsEdit__JobAlertEnabled")
    enable_add_this_plugin_cbox = (By.ID, "Admin_JobBoardsEdit__AddThisEnabled")
    hide_company_name_cbox = (By.ID, "Admin_JobBoardsEdit__HideJobListCompanyName")
    enable_captcha_cbox = (By.ID, "Admin_JobBoardsEdit__EnableRecaptcha")
    default_portal_language = (By.ID, "Admin_JobBoardsEdit__DefaultLocale")
    save_btn = (By.ID, "Admin_JobBoardsEdit__SaveButton")
    open_submission_switch = (By.ID, "Admin_OpenSubmissionForms__OpenSubmissionEnabled")
    open_submission_savebtn = (By.ID, "Admin_OpenSubmissionForms__SaveButton")


class ManageGeneralSettings(Elements, Common):
    def __init__(self, driver):
        super().__init__(driver)

    def select_portal_language(self, language):
        select = Select(self.driver.find_element_by_locator(self.default_portal_language))
        return select.select_by_visible_text(language)

    def change_portal_default_language(self, language):
        languages = dict(
            german=partial(self.select_portal_language, "Deutsch (German) [de]"),
            english=partial(self.select_portal_language, "English (English) [en]"),
            spanish=partial(self.select_portal_language, "español (Spanish) [es]"),
            french=partial(self.select_portal_language, "français (French) [fr]")
        )

        try:
            return languages.get(language)()
        except TypeError:
            raise BaseError(f"Valid languages: {list(language.keys())}")

    def click_cx_settings_save_btn(self):
        elem = self.driver.find_element_by_locator(self.save_btn)
        self.driver.execute_script("arguments[0].scrollIntoView();", elem)
        return self.do_click(elem)

    def open_submission_choice(self):
        checkbox = self.driver.find_element_by_locator(self.open_submission_switch)
        if checkbox.is_selected():
            checkbox.click()
        else:
            return self.driver.find_element_by_locator(self.open_submission_switch)

    def click_save_button(self,):
        savebtnopensubmission = self.driver.find_element_by_locator(self.open_submission_savebtn)
        self.driver.execute_script("arguments[0].scrollIntoView();", savebtnopensubmission)
        return self.do_click(savebtnopensubmission)

    def open_submission_click(self):
        checkbox = self.driver.find_element_by_locator(self.open_submission_switch)
        checkbox.click()
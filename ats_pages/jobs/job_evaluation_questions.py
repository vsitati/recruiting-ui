from common.common import Common
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with
from test_data.test_data_details import JobData


class Elements:
    select_checkbox = "evalquestionid"
    select_question_quickly_btn = (By.ID, "selectQuestionsQuicklyButton")
    update_question_settings_btn = (By.ID, "updateQuestionSettingsButton")
    return_to_job_lists_btn = ".lifesuite__button.lifesuite__float-right"
    save_btn = (By.XPATH, "//span[text()='Save']")


class JobEvaluationQuestions(Common, Elements):
    def __init__(self, driver):
        super().__init__(driver)

    def select_cqe(self):
        # open the link
        text = JobData.job_data.get("cqe")
        elm_link = self.driver.find_element_by_locator((By.LINK_TEXT, text))
        self.do_click(elm_link)
        # check a checkbox
        elm_checkbox = self.driver.find_element(locate_with(By.NAME, self.select_checkbox).below(elm_link))
        self.do_click(elm_checkbox)
        # click select question quickly button
        self.go_click(self.select_question_quickly_btn)
        # click return to job list button
        elm_btn = self.driver.find_element_by_locator(self.update_question_settings_btn)
        elm = self.driver.find_element(locate_with(By.CSS_SELECTOR, self.return_to_job_lists_btn).to_left_of(elm_btn))
        self.do_click(elm)

    def update_cqe(self):
        # open the link
        text = JobData.job_data.get("cqe_edit")
        elm_link = self.driver.find_element_by_locator((By.LINK_TEXT, text))
        self.do_click(elm_link)
        # check a checkbox
        elm_checkbox = self.driver.find_element(locate_with(By.NAME, self.select_checkbox).below(elm_link))
        self.do_click(elm_checkbox)
        # click return to job list button
        elm_btn = self.driver.find_element_by_locator(self.update_question_settings_btn)
        self.do_click(elm_btn)

        self.go_click(self.save_btn)

        elm_btn = self.driver.find_element_by_locator(self.update_question_settings_btn)
        elm = self.driver.find_element(locate_with(By.CSS_SELECTOR, self.return_to_job_lists_btn).to_left_of(elm_btn))
        self.do_click(elm)

    def click_return_to_job_lists_btn(self):
        self.go_click(self.return_to_job_lists_btn)

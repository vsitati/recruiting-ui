from common.common import Common
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from enum import auto


class Elements:
    quick_search_btn = (By.ID, 'quick_search_button')
    quick_search_text = (By.ID, 'quick_search_input')
    ellipses_menu_btn_on_job_details = (By.CSS_SELECTOR,
                                        "[class='oh__menu-icon lifesuite__button--dropdown oh__menu-button']"
                                        ">[class='oh__icon-button lifesuite__float-right']")
    ellipses_menu_btn_on_job_edit = (By.CSS_SELECTOR,
                                        "[class='oh__icon-button lifesuite__float-right richTextValidatorIgnore']"
                                        ">[class='richTextValidatorIgnore']")
    ellipses_menu_btn_on_candidate_search = (By.CSS_SELECTOR, ".fas.fa-ellipsis-v.fa-2x.richTextValidatorIgnore")


class PageHeader(Common, Elements):
    def __init__(self, driver):
        super().__init__(driver)

    # object_types = Enum('Types', ('Jobs Candidates'))

    class EllipsesMenu(enumerate):
        # Job Details page
        Print = "Print"
        EditThisJob = "Edit This Job"
        PostNewJob = "Post New Job"
        CloneThisJob = "Clone this Job"
        RequisitionDetails = "Requisition Details"
        SeeHotMatches = "See Hot Matches"
        ReturnCancel = "Return / Cancel"
        # Job Editing page
        ReturnToJobPostings = "Return to Job Postings"
        EditJobPostingPositionDetails = "Edit Job Posting - Position Details"
        EditJobPostingDepartmentBudgetDetails = "Edit Job Posting - Department & Budget Details"
        EditJobPostingPositionPriority = "Edit Job Posting - Priority"
        EditJobPostingPositionCategory = "Edit Job Posting - Category"
        EditJobPostingPositionAttachments = "Edit Job Posting - Attachments"
        EditJobPostingPositionEvaluationQuestions = "Edit Job Posting - Evaluation Questions"
        RequisitionApprovalDetails = "Requisition Approval Details"
        # Candidate Search page
        Columns = "Columns"

    class OnPage(enumerate):
        Job_Details = auto()
        Job_Edit = auto()
        Candidate_Search = auto()

    def quick_search(self, search_object, search_input=""):
        elm = self.driver.find_element_by_locator(self.quick_search_btn)
        if elm.text.lower() != search_object.lower():
            self.do_click(elm)

        elm = self.driver.find_element_by_locator(self.quick_search_text)
        elm.send_keys(search_input)
        elm.send_keys(Keys.ENTER)

    def select_ellipses_menu(self, ellipses_menu: EllipsesMenu, on_page: OnPage):
        if on_page == self.OnPage.Job_Details:
            self.go_click(self.ellipses_menu_btn_on_job_details)
        elif on_page == self.OnPage.Job_Edit:
            self.go_click(self.ellipses_menu_btn_on_job_edit)
        elif on_page == self.OnPage.Candidate_Search:
            self.go_click(self.ellipses_menu_btn_on_candidate_search)

        elm_link = self.driver.find_element_by_locator((By.LINK_TEXT, ellipses_menu))
        self.do_click(elm_link)

        return

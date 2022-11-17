from common.common import Common
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys


class Elements:
    search_btn = (By.ID, 'quick_search_button')
    search_text = (By.ID, 'quick_search_input')
    ellipses_menu_btn_on_job_details = (By.CSS_SELECTOR,
                                        "[class='oh__menu-icon lifesuite__button--dropdown oh__menu-button']"
                                        ">[class='oh__icon-button lifesuite__float-right']")
    ellipses_menu_btn_on_job_edit = (By.CSS_SELECTOR,
                                     "[class='oh__icon-button lifesuite__float-right richTextValidatorIgnore']"
                                     ">[class='richTextValidatorIgnore']")


class PageHeader(Common, Elements):
    def __init__(self, driver):
        super().__init__(driver)

    # object_types = Enum('Types', ('Jobs Candidates'))

    class EllipsesMenu(enumerate):
        Print = "Print"
        EditThisJob = "Edit This Job"
        PostNewJob = "Post New Job"
        CloneThisJob = "Clone this Job"
        RequisitionDetails = "Requisition Details"
        SeeHotMatches = "See Hot Matches"
        ReturnCancel = "Return / Cancel"
        ReturntoJobPostings = "Return to Job Postings"
        EditJobPostingPositionDetails = "Edit Job Posting - Position Details"
        EditJobPostingDepartmentBudgetDetails = "Edit Job Posting - Department & Budget Details"
        EditJobPostingPositionPriority = "Edit Job Posting - Priority"
        EditJobPostingPositionCategory = "Edit Job Posting - Category"
        EditJobPostingPositionAttachments = "Edit Job Posting - Attachments"
        EditJobPostingPositionEvaluationQuestions = "Edit Job Posting - Evaluation Questions"
        RequisitionApprovalDetails = "Requisition Approval Details"

    def quick_search(self, search_object, search_input=""):
        elm = self.driver.find_element_by_locator(self.search_btn)
        if elm.text != search_object:
            self.do_click(elm)

        elm = self.driver.find_element_by_locator(self.search_text)
        elm.send_keys(search_input)
        elm.send_keys(Keys.ENTER)

    def select_ellipses_menu(self, ellipses_menu: EllipsesMenu, flg = "job_details"):
        if flg == "job_details":
            self.go_click(self.ellipses_menu_btn_on_job_details)
        else:
            self.go_click(self.ellipses_menu_btn_on_job_edit)

        elm_link = self.driver.find_element_by_locator((By.LINK_TEXT, ellipses_menu))
        self.do_click(elm_link)

        return

from ats_pages.base import BasePage
from selenium.webdriver.common.by import By
from enum import Enum


class LeftMenus(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    class DialogButtons(Enum):
        Save_Search_Save = "saveSearchModalSave"
        Save_Search_Close = "saveSearchModalClose"

    class Elements:
        menu_icon = (By.ID, 'topMenu-menuItem-icon')
        menu_text = (By.ID, 'topMenu-menuItem-itemText')

        dashboards = (By.ID, 'link_Dashboards-svgIcon')
        dashboards_candidates = (By.ID, 'link_CandidatesDashboard-itemText')
        dashboards_jobs = (By.ID, 'link_JobsDashboard-itemText')
        dashboards_recruiter = (By.ID, 'link_RecruiterDashboard-itemText')

        jobs = (By.ID, 'link_Jobs')
        jobs_advanced_search = (By.ID, 'link_JobSearch-itemText')
        create_job_postings = (By.ID, 'link_CreatePosting-itemText')
        manage_requisitions = (By.ID, 'link_Requisitions-itemText')
        track_all_jobs = (By.ID, 'link_TrackAllJobs-itemText')
        view_job_offers = (By.ID, 'link_JobOffers-itemText')

        Candidates = [By.ID, 'link_Candidates']
        Candidates_Advanced_Search = (By.ID, 'link_CandidateSearch-itemText')
        EEO_AA_info = [By.ID, 'link_EEOAAInfo']
        Employee_Referrals = [By.ID, "link_EmployeeReferrals-itemText"]
        Folders = [By.ID, "link_Folders-itemText"]
        Interviews = [By.ID, "link_Interviews-itemText"]
        Recycle_Bin = [By.ID, "link_RecycleBin-itemText"]
        Review_Requests = [By.ID, "link_ReviewRequests-itemText"]
        Reviews_Status = [By.ID, "link_ReviewsStatus-itemText"]
        Upload = [By.ID, "link_Upload-itemText"]

        Reports = [By.ID, 'link_Reports']
        EEO_Reports = [By.ID, 'link_EEOReports-itemText']
        Job_Cycle_Time = [By.ID, 'link_JobCycleTime-itemText']
        Manage_Report_Access = [By.ID, 'link_ManageReportAccess-itemText']
        My_Reports = [By.ID, 'link_MyReports-itemText']
        OFCCP_Reports = [By.ID, 'link_OFCCPReports-itemText']
        Report_Builder = [By.ID, 'link_ReportBuilder-itemText']
        Resource_Analysis = [By.ID, 'link_ResourceAnalysis-itemText']

        Administration = [By.ID, 'link_Administration']
        AAP_Job_Group = [By.ID, 'link_AAPJobGroup-itemText']
        Background_Checking = [By.ID, 'link_BackgroundChecking-itemText']
        Business_Units = [By.ID, 'link_BusinessUnits-itemText']
        CCE_Templates = [By.ID, 'link_CCETemplates-itemText']
        Company_Locations = [By.ID, 'link_CompanyLocations-itemText']
        CQE = [By.ID, 'link_CQE-itemText']
        Departments = [By.ID, 'link_Departments-itemText']
        Fee_Agencies = [By.ID, 'link_FeeAgencies-itemText']
        Job_Categories = [By.ID, 'link_JobCategories-itemText']
        Job_Templates = [By.ID, 'link_JobTemplates-itemText']
        Manage_Resources = [By.ID, 'link_ManageResources-itemText']
        Offer_Rejection_Letters = [By.ID, 'link_OfferRejectionLetters-itemText']
        Settings = [By.ID, 'link_Settings-itemText']
        User_Accounts = [By.ID, 'link_UserAccounts-itemText']

        Help = [By.ID, 'link_Help']

    def click_left_nav(self, leftnav_main: Elements, leftnav_sub = ""):
        self.open_menu()
        elm = self.driver.find_element_by_locator(leftnav_main)
        if elm.get_attribute("aria-expanded") == "false":
            self.do_click(self.driver.find_element_by_locator(leftnav_main))
        if leftnav_sub:
            self.do_click(self.driver.find_element_by_locator(leftnav_sub))

    def open_menu(self):
        if not self.driver.find_element_by_locator(self.Elements.menu_text).is_displayed():
            return self.do_click(self.driver.find_element_by_locator(self.Elements.menu_icon))
        return True

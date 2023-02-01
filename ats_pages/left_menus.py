from common.common import Common
from selenium.webdriver.common.by import By
import time
from selenium.common import ElementNotInteractableException, ElementClickInterceptedException


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

    candidates = [By.ID, 'link_Candidates']
    candidates_advanced_search = (By.ID, 'link_CandidateSearch-itemText')
    eeo_aa_info = [By.ID, 'link_EEOAAInfo']
    employee_referrals = [By.ID, "link_EmployeeReferrals-itemText"]
    folders = [By.ID, "link_Folders-itemText"]
    interviews = [By.ID, "link_Interviews-itemText"]
    recycle_Bin = [By.ID, "link_RecycleBin-itemText"]
    review_Requests = [By.ID, "link_ReviewRequests-itemText"]
    reviews_Status = [By.ID, "link_ReviewsStatus-itemText"]
    upload = [By.ID, "link_Upload-itemText"]

    reports = [By.ID, 'link_Reports']
    eeo_reports = [By.ID, 'link_EEOReports-itemText']
    job_cycle_time = [By.ID, 'link_JobCycleTime-itemText']
    manage_report_access = [By.ID, 'link_ManageReportAccess-itemText']
    my_reports = [By.ID, 'link_MyReports-itemText']
    ofccp_reports = [By.ID, 'link_OFCCPReports-itemText']
    report_builder = [By.ID, 'link_ReportBuilder-itemText']
    resource_analysis = [By.ID, 'link_ResourceAnalysis-itemText']

    administration = [By.ID, 'link_Administration']
    aap_job_group = [By.ID, 'link_AAPJobGroup-itemText']
    background_checking = [By.ID, 'link_BackgroundChecking-itemText']
    business_units = [By.ID, 'link_BusinessUnits-itemText']
    cce_templates = [By.ID, 'link_CCETemplates-itemText']
    company_locations = [By.ID, 'link_CompanyLocations-itemText']
    cqe = [By.ID, 'link_CQE-itemText']
    departments = [By.ID, 'link_Departments-itemText']
    fee_agencies = [By.ID, 'link_FeeAgencies-itemText']
    job_categories = [By.ID, 'link_JobCategories-itemText']
    job_templates = [By.ID, 'link_JobTemplates-itemText']
    manage_resources = [By.ID, 'link_ManageResources-itemText']
    offer_rejection_letters = [By.ID, 'link_OfferRejectionLetters-itemText']
    settings = [By.ID, 'link_Settings-itemText']
    user_accounts = [By.ID, 'link_UserAccounts-itemText']
    left_nav_attr = "aria-expanded"

    help = [By.ID, 'link_Help']


class LeftMenus(Common, Elements):
    def __init__(self, driver):
        super().__init__(driver)

    def click_left_nav(self, element):
        self.open_menu()
        time.sleep(self.sleep_time)  # TODO: find a better way to wait
        return self.do_click(self.driver.find_element_by_locator(element))

    def click_left_nav_sub(self, element):
        return self.do_click(self.driver.find_element_by_locator(element))

    def open_menu(self):
        if not self.driver.find_element_by_locator(self.menu_text).is_displayed():
            return self.do_click(self.driver.find_element_by_locator(self.menu_icon))
        return True

    def click_left_nav_switch(self, element):
        self.open_menu()
        menu_text = ''
        while not menu_text:
            try:
                menu_text = self.get_text(element)
                menu_item = self.driver.find_element_by_locator(element)
                return self.do_click(menu_item)
            except (ElementNotInteractableException, ElementClickInterceptedException):
                self.sr_logger.logger.info("The above is a correct exception catch.")
                continue

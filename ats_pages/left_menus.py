import allure
from helpers.utils import do_click
from selenium.webdriver.common.by import By


class Elements:
    menu_icon = (By.ID, 'topMenu-menuItem-icon')
    menu_text = (By.ID, 'topMenu-menuItem-itemText')
    dashboards = (By.ID, 'link_Dashboards-svgIcon')
    dashboards_candidates = (By.ID, 'link_CandidatesDashboard-itemText')
    dashboards_jobs = (By.ID, 'link_JobsDashboard-itemText')
    dashboards_recruiter = (By.ID, 'link_RecruiterDashboard-itemText')
    jobs = (By.ID, 'link_Jobs-itemIcon')
    jobs_advanced_search = (By.ID, 'link_JobSearch-itemText')
    create_job_postings = (By.ID, 'link_CreatePosting-itemText')
    manage_requisitions = (By.ID, 'link_Requisitions-itemText')
    track_all_jobs = (By.ID, 'link_TrackAllJobs-itemText')
    view_job_offers = (By.ID, 'link_JobOffers-itemText')


class LeftMenus(Elements):
    def __init__(self, driver):
        self.driver = driver

    def open_menu(self):
        if not self.driver.find_element_by_locator(self.menu_text).is_displayed():
            return do_click(self.driver.find_element_by_locator(self.menu_icon))
        return True

    def click_dashboard_jobs(self):
        return do_click(self.driver.find_element_by_locator(self.dashboards_jobs))

    def click_jobs(self):
        return do_click(self.driver.find_element_by_locator(self.jobs))
    
    def click_jobs_advanced_search(self):
        return do_click(self.driver.find_element_by_locator(self.jobs_advanced_search))

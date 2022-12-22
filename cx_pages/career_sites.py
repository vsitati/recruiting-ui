from common.common import Common
from selenium.webdriver.common.by import By


class Elements:
    career_site = (By.CSS_SELECTOR, '.sr-career-site-list-banner')
    career_site_settings = (By.CSS_SELECTOR, '.sr-career-site-settings')
    board_lists = (By.ID, 'Admin_JobBoardsList_BoardList')
    career_site_title = (By.CSS_SELECTOR, '.sr-career-site-title')


class CareerSites(Elements, Common):
    def __init__(self, driver):
        super().__init__(driver)

    def get_career_sites(self, site_section):

        if site_section == "external":
            career_sites_parent, *_ = self.driver.find_elements_by_locator(self.board_lists)
        else:
            # Internal
            *_, career_sites_parent = self.driver.find_elements_by_locator(self.board_lists)

        # Career Site URL
        career_site_elems = career_sites_parent.find_elements(*self.career_site)
        career_sites = [site.get_attribute("href") for site in career_site_elems]

        # Career Site Settings URL
        career_sites_setting_elems = career_sites_parent.find_elements(*self.career_site_settings)
        career_sites_settings = [site_setting.get_attribute("href") for site_setting in career_sites_setting_elems]

        # Career Site Title
        career_site_title_elems = career_sites_parent.find_elements(*self.career_site_title)
        career_site_titles = [career_site_title.text for career_site_title in career_site_title_elems]
        return list(zip(career_site_titles, career_sites, career_sites_settings))

    @staticmethod
    def filter_career_site(data, site_name="", visible=True):
        if not data:
            return False

        if visible:
            # ('UFT Auto - zNeksnGNrD', 'https://cx-qa.silkroad-eng.com/qaautomationonly/mXNZbGUopHElCSouHZXDQGPaSMZXCn'
            # 'https://cx-qa.silkroad-eng.com/qaautomationonly/admin/JobBoards/Options?portalId=2404')
            result = [info for info in data if info[0] == site_name and info[1] is not None]
            return result[0]
        else:
            # ('UFT Auto - ZDNRwcfLjQ', None,
            # 'https://cx-qa.silkroad-eng.com/qaautomationonly/admin/JobBoards/Edit?portalId=0&portalCode=1605')
            return [info for info in data if info[1] is None]
            # TODO Need to add site name here, to publish a specific portal

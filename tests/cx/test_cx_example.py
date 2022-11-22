import pytest
import allure
from common.common import Common
from cx_pages.career_sites import CareerSites
from cx_pages.jobs_search import JobSearch
from cx_pages.career_site_settings import CareerSiteSettings
from cx_pages.login import Login


@pytest.mark.usefixtures("setup")
class TestCandidateExperience:
    @allure.title("CX Example Tests")
    @allure.description("Get Page Title")
    def test_get_page_title(self, get_test_info):
        login = Login(driver=self.driver)
        login.do_login(env_info=get_test_info)

        page = Common(self.driver)
        assert page.get_title() == "Career Sites - QA Automation Only"

    @allure.description("Navigate to a Job Search Page for a given Job Portal")
    def test_go_to_job_search_page(self, get_test_info):
        login = Login(driver=self.driver)
        login.do_login(env_info=get_test_info)

        cs = CareerSites(driver=self.driver)
        data = cs.get_career_sites(site_section="external")
        result = cs.filter_career_site(data=data, site_name="Corporate Career Portal")
        name, portal, settings = result
        cs.open_url(portal)
        assert cs.get_title() == "QA Automation Only - SilkRoad Talent Activation"

        js = JobSearch(driver=self.driver)
        job_elem = js.find_job(title="Customer Service Representative")
        js.open_job(job_elem=job_elem)
        assert "Customer Service Representative" in js.get_title()

    @allure.description("Select a random job")
    def test_select_random_job(self, get_test_info):
        login = Login(driver=self.driver)
        login.do_login(env_info=get_test_info)

        cs = CareerSites(driver=self.driver)
        data = cs.get_career_sites(site_section="external")
        result = cs.filter_career_site(data=data, site_name="Corporate Career Portal")
        name, portal, settings = result
        cs.open_url(portal)
        assert cs.get_title() == "QA Automation Only - SilkRoad Talent Activation"

        js = JobSearch(driver=self.driver)
        job_elem, job_title = js.find_job(random_job=True)
        js.open_job(job_elem=job_elem)
        assert job_title in js.get_title()

    @allure.description("Select a random job")
    def test_open_career_site_settings(self, get_test_info):
        login = Login(driver=self.driver)
        login.do_login(env_info=get_test_info)

        cs = CareerSites(driver=self.driver)
        data = cs.get_career_sites(site_section="external")
        result = cs.filter_career_site(data=data, site_name="Corporate Career Portal")
        name, portal, settings = result
        cs.open_url(settings)
        assert cs.get_h2_tag_name() == "Career Site Settings"

        css = CareerSiteSettings(driver=self.driver)
        css.open_setting().get("fee_agency_job_details_page")()

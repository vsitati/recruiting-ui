import pytest
import allure
from test_data.test_data_details import JobData
from ats_pages.login.login import Login
from ats_pages.page_header import PageHeader
from ats_pages.jobs.job_advanced_search_result import JobAdvancedSearchResult
from ats_pages.jobs.job_position_details_view import JobPositionDetailsView

from cx_pages.login import Login as CX_Login    # import cx_pages.login
from cx_pages.cx_jobs_details import CXJobDetails
from cx_pages.career_sites import CareerSites
from cx_pages.jobs_search import JobSearch

from time import sleep


@pytest.mark.usefixtures("setup")
class TestJobVerify:

    @pytest.mark.dependency(
        depends=["tests/ats/jobs/test_job_1_create.py::TestJobCreate::test_job_create"],
        scope='session')
    @allure.title("ATS Verify Job Creation")
    @allure.description("Verify the Job in ATS - JIRA: RND-7269")
    @pytest.mark.xfail()
    def test_job_verify_in_ats(self, get_test_info):
        login = Login(driver=self.driver)
        login.do_login(get_test_info)

        search_input = JobData.job_data.get("internal_job_title")
        page_header = PageHeader(self.driver)
        page_header.quick_search("jobs", search_input)

        job_search_result = JobAdvancedSearchResult(self.driver)
        job_search_result.verify_is_job_search_result_page()
        job_search_result.open_job(search_input)

        job_position_details_view = JobPositionDetailsView(self.driver)
        job_position_details_view.verify_header()
        job_position_details_view.verify_all_fields()

        sleep(Login.sleep_time)
        job_search_result.verify_is_job_search_result_page()

        return

    @pytest.mark.dependency(
        depends=["tests/ats/jobs/test_job_1_create.py::TestJobCreate::test_job_create"],
        scope='session')
    @allure.title("ATS Verify Job Creation")
    @allure.description("Verify the Job in CX - JIRA: RND-7321")
    @pytest.mark.xfail()
    def test_job_verify_in_cx(self, get_test_info):
        # The following is to verify the CX page - External
        cx_login = CX_Login(self.driver)     # cx_login = cx_pages.login.Login(self.driver)
        cx_login.do_login(get_test_info)

        cx_career_sites = CareerSites(self.driver)
        data = cx_career_sites.get_career_sites(site_section="external")
        result = cx_career_sites.filter_career_site(data=data, site_name="Corporate Career Portal")
        name, portal_url, settings_url = result
        cx_career_sites.open_url(portal_url)
        assert cx_career_sites.get_title() == "QA Automation Only - SilkRoad Talent Activation"

        cx_job_search = JobSearch(self.driver)
        job_elem, job_title = cx_job_search.find_job(title=JobData.job_data.get("posted_job_title"))
        cx_job_search.open_job(job_elem=job_elem)
        assert job_title in cx_job_search.get_title()

        cx_job_details = CXJobDetails(self.driver)
        cx_job_details.verify_page_title(JobData.job_data.get("posted_job_title"))

        # The following is to verify the CX page - Internal
        cx_login.new_tab()
        cx_login.do_login(get_test_info)

        data = cx_career_sites.get_career_sites(site_section="internal")
        result = cx_career_sites.filter_career_site(data=data, site_name="Internal Career Page")
        name, portal_url, settings_url = result
        cx_career_sites.open_url(portal_url)
        assert cx_career_sites.get_title() == "QA Automation Only - SilkRoad Talent Activation"

        job_elem, job_title = cx_job_search.find_job(title=JobData.job_data.get("posted_job_title"))
        cx_job_search.open_job(job_elem=job_elem)
        assert job_title in cx_job_search.get_title()

        cx_login.close_tab()
        return

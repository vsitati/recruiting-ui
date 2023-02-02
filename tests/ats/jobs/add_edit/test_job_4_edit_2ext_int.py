import pytest
import allure
from test_data.test_data_details import JobData
from ats_pages.login.login import Login
from ats_pages.page_header import PageHeader
from ats_pages.jobs.job_advanced_search_result import JobAdvancedSearchResult
from ats_pages.jobs.job_position_details_view import JobPositionDetailsView
from ats_pages.jobs.job_position_details import JobPositionDetails

import cx_pages.login
from cx_pages.cx_jobs_details import CXJobDetails
from cx_pages.career_sites import CareerSites
from cx_pages.jobs_search import JobSearch


@pytest.mark.usefixtures("setup")
class TestJobEdit2ExtInt:

    @allure.title("ATS Edit a Job to External")
    @allure.description("Edit the Job in ATS - JIRA: RND-7327")
    def test_job_edit_2ext(self, get_test_info):
        login = Login(self.driver)
        login.do_login(get_test_info)

        search_input = "Customer Service Representative"

        page_header = PageHeader(self.driver)
        page_header.quick_search("jobs", search_input)

        job_search_result = JobAdvancedSearchResult(self.driver)
        job_search_result.verify_is_job_search_result_page()
        job_search_result.open_job(search_input)

        job_position_details_view = JobPositionDetailsView(self.driver)
        job_position_details_view.verify_header()

        page_header.select_ellipses_menu(page_header.EllipsesMenu.EditThisJob, page_header.OnPage.Job_Details)

        job_position_details = JobPositionDetails(self.driver)
        job_position_details.edit_job_posting_status(JobData.job_data.get("posting_status_external"))
        job_position_details_view.verify_header()
        job_position_details_view.verify_posting_status("External")

        # The following is to verify the CX page - existing in External
        cx_login = cx_pages.login.Login(self.driver)
        cx_login.new_tab()
        cx_login.do_login(get_test_info)

        cx_career_sites = CareerSites(self.driver)
        data = cx_career_sites.get_career_sites(site_section="external")
        result = cx_career_sites.filter_career_site(data=data, site_name="Corporate Career Portal")
        name, portal_url, settings_url = result
        cx_career_sites.open_url(portal_url)
        assert cx_career_sites.get_title() == "QA Automation Only - SilkRoad Talent Activation"

        cx_job_search = JobSearch(self.driver)
        job_elem, job_title = cx_job_search.find_job(title=search_input)
        cx_job_search.open_job(job_elem=job_elem)
        assert job_title in cx_job_search.get_title()

        cx_job_details = CXJobDetails(self.driver)
        cx_job_details.verify_page_title(search_input)

        # The following is to verify the CX page - NOT existing in Internal
        cx_login.new_tab()
        cx_login.do_login(get_test_info)

        data = cx_career_sites.get_career_sites(site_section="internal")
        result = cx_career_sites.filter_career_site(data=data, site_name="Internal Career Page")
        name, portal_url, settings_url = result
        cx_career_sites.open_url(portal_url)
        assert cx_career_sites.get_title() == "QA Automation Only - SilkRoad Talent Activation"

        result = cx_job_search.find_job(title=search_input)
        assert result == ""

        cx_login.close_tab()
        cx_login.switch_tab()
        cx_login.close_tab()
        return

    @allure.title("ATS Edit a Job to Internal")
    @allure.description("Edit the Job in ATS - JIRA: RND-7328")
    def test_job_edit_2int(self, get_test_info):
        login = Login(self.driver)
        login.do_login(get_test_info)

        search_input = "Customer Service Representative"

        page_header = PageHeader(self.driver)
        page_header.quick_search("jobs", search_input)

        job_search_result = JobAdvancedSearchResult(self.driver)
        job_search_result.verify_is_job_search_result_page()
        job_search_result.open_job(search_input)

        job_position_details_view = JobPositionDetailsView(self.driver)
        job_position_details_view.verify_header()

        page_header.select_ellipses_menu(page_header.EllipsesMenu.EditThisJob, page_header.OnPage.Job_Details)

        job_position_details = JobPositionDetails(self.driver)
        job_position_details.edit_job_posting_status(JobData.job_data.get("posting_status_internal"))
        job_position_details_view.verify_header()
        job_position_details_view.verify_posting_status("Internal")

        # The following is to verify the CX page - existing in Internal
        cx_login = cx_pages.login.Login(self.driver)
        cx_login.new_tab()
        cx_login.do_login(get_test_info)

        cx_career_sites = CareerSites(self.driver)
        data = cx_career_sites.get_career_sites(site_section="internal")
        result = cx_career_sites.filter_career_site(data=data, site_name="Internal Career Page")
        name, portal_url, settings_url = result
        cx_career_sites.open_url(portal_url)
        assert cx_career_sites.get_title() == "QA Automation Only - SilkRoad Talent Activation"

        cx_job_search = JobSearch(self.driver)
        job_elem, job_title = cx_job_search.find_job(title=search_input)
        cx_job_search.open_job(job_elem=job_elem)
        assert job_title in cx_job_search.get_title()

        cx_job_details = CXJobDetails(self.driver)
        cx_job_details.verify_page_title(search_input)

        # The following is to verify the CX page - NOT existing in External
        cx_login.new_tab()
        cx_login.do_login(get_test_info)

        data = cx_career_sites.get_career_sites(site_section="external")
        result = cx_career_sites.filter_career_site(data=data, site_name="Corporate Career Portal")
        name, portal_url, settings_url = result
        cx_career_sites.open_url(portal_url)
        assert cx_career_sites.get_title() == "QA Automation Only - SilkRoad Talent Activation"

        result = cx_job_search.find_job(title=search_input)
        assert result == ""

        cx_login.close_tab()
        cx_login.switch_tab()
        cx_login.close_tab()
        return

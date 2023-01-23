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
class TestJobClone:

    @allure.title("ATS Clone a Job")
    @allure.description("Clone the Job in ATS - JIRA: RND-7347")
    def test_job_clone(self, get_test_info):
        login = Login(self.driver)
        login.do_login(get_test_info)

        search_input = JobData.job_data.get("internal_job_title")

        page_header = PageHeader(self.driver)
        page_header.quick_search("jobs", search_input)

        job_search_result = JobAdvancedSearchResult(self.driver)
        job_search_result.verify_is_job_search_result_page()
        job_search_result.open_job(search_input)

        job_position_details_view = JobPositionDetailsView(self.driver)
        job_position_details_view.verify_header()

        page_header.select_ellipses_menu(page_header.EllipsesMenu.CloneThisJob, page_header.OnPage.Job_Details)

        job_position_details = JobPositionDetails(self.driver)
        job_position_details.edit_job_title_clone()
        job_position_details_view.verify_header()

        # Verify the new cloned job on ATS
        search_input = JobData.job_data.get("internal_job_title_clone")
        page_header.quick_search("jobs", search_input)

        job_search_result = JobAdvancedSearchResult(self.driver)
        job_search_result.verify_is_job_search_result_page()
        job_search_result.open_job(search_input)

        job_position_details_view = JobPositionDetailsView(self.driver)
        job_position_details_view.verify_header()
        job_position_details_view.verify_posting_status("On Hold")

        return

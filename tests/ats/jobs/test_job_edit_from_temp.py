import pytest
import allure
from test_data.test_data_details import JobData
from ats_pages.login.login import Login
from ats_pages.page_header import PageHeader
from ats_pages.jobs.job_advanced_search_result import JobAdvancedSearchResult
from ats_pages.jobs.job_position_details_view import JobPositionDetailsView
from ats_pages.jobs.job_position_details import JobPositionDetails


@pytest.mark.usefixtures("setup")
class TestJobEditFromTemp:

    @allure.title("ATS Edit from Template")
    @allure.description("Edit the Job from a Template in ATS - JIRA: RND-7362")
    def test_job_edit_from_temp(self, get_test_info):
        login = Login(driver=self.driver)
        login.do_login(get_test_info)

        search_input = JobData.job_data.get("internal_job_title_clone")

        page_header = PageHeader(self.driver)
        page_header.quick_search("jobs", search_input)

        job_search_result = JobAdvancedSearchResult(self.driver)
        job_search_result.verify_is_job_search_result_page()
        job_search_result.open_job(search_input)

        job_position_details_view = JobPositionDetailsView(self.driver)
        job_position_details_view.verify_header()

        page_header.select_ellipses_menu(page_header.EllipsesMenu.EditThisJob)

        job_position_details = JobPositionDetails(self.driver)
        job_position_details.edit_job_template()
        job_position_details_view.verify_header()

        job_position_details_view.verify_from_temp()

        return

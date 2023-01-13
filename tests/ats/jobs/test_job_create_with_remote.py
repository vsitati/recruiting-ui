import pytest
import allure
from ats_pages.login.login import Login
from ats_pages.left_menus import LeftMenus
from ats_pages.page_header import PageHeader
from ats_pages.jobs.job_position_details import JobPositionDetails
from ats_pages.jobs.job_department_budget import JobDepartmentBudget
from ats_pages.jobs.job_priority import JobPriority
from ats_pages.jobs.job_category import JobCategory
from ats_pages.jobs.job_attachments import JobAttachments
from ats_pages.jobs.job_evaluation_questions import JobEvaluationQuestions
from ats_pages.jobs.job_advanced_search_result import JobAdvancedSearchResult
from ats_pages.jobs.job_position_details_view import JobPositionDetailsView

from test_data.test_data_details import JobData


@pytest.mark.usefixtures("setup")
class TestJobCreateWithRemote:
    @allure.title("ATS Create a Job with remote location")
    @allure.description("Create a Job with remote locations - JIRA: RND-7363")
    def test_job_create_with_remote(self, get_test_info):
        login = Login(driver=self.driver)
        login.do_login(get_test_info)

        left_menu = LeftMenus(self.driver)
        left_menu.click_left_nav(left_menu.jobs)
        left_menu.click_left_nav_sub(left_menu.create_job_postings)

        job_position_details = JobPositionDetails(self.driver)
        job_position_details.fill_out_required_job_details_fields()

        # job_position_details.select_remote_country()
        job_position_details.select_remote_state()

        # job_position_details.select_job_location_remote_state()
        job_position_details.select_job_location_remote_country()

        # job_position_details.select_job_temp_remote_state()
        job_position_details.select_job_temp_remote_country()

        job_position_details.click_continue()

        job_department_budget = JobDepartmentBudget(self.driver)
        job_department_budget.fill_out_required_job_departments_fields()

        job_priority = JobPriority(self.driver)
        job_priority.setup_required_priority()

        job_category = JobCategory(self.driver)
        job_category.select_category()
        # upon this step, the job is created

        job_attachments = JobAttachments(self.driver)
        job_attachments.upload_required_file()

        job_evaluation_questions = JobEvaluationQuestions(self.driver)
        job_evaluation_questions.click_return_to_job_lists_btn()

        # verify the remote job on Job Details page
        job_title = "Remote Job (Worldwide)"
        page_header = PageHeader(self.driver)
        page_header.quick_search("jobs", job_title)

        job_search_result = JobAdvancedSearchResult(self.driver)
        job_search_result.verify_is_job_search_result_page()
        job_search_result.open_job(job_title)

        job_position_details_view = JobPositionDetailsView(self.driver)
        job_position_details_view.verify_header()
        job_position_details_view.verify_remote_country(job_title)

        # Edit the remote job
        page_header.select_ellipses_menu(page_header.EllipsesMenu.EditThisJob)

        job_position_details.select_job_temp_remote_state()
        job_position_details.click_save()

        # verify the remote job on Job Details page
        job_position_details_view.verify_header()
        job_position_details_view.verify_remote_country("REMOTE, United States")

        return

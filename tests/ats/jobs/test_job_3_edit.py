import pytest
import allure
from test_data.test_data_details import JobData
from ats_pages.login.login import Login
from ats_pages.page_header import PageHeader
from ats_pages.jobs.job_advanced_search_result import JobAdvancedSearchResult
from ats_pages.jobs.job_position_details_view import JobPositionDetailsView
from ats_pages.jobs.job_position_details import JobPositionDetails
from ats_pages.jobs.job_department_budget import JobDepartmentBudget
from ats_pages.jobs.job_priority import JobPriority
from ats_pages.jobs.job_category import JobCategory
from ats_pages.jobs.job_attachments import JobAttachments
from ats_pages.jobs.job_evaluation_questions import JobEvaluationQuestions


@pytest.mark.usefixtures("setup")
class TestJobEdit:

    @pytest.mark.dependency(
        depends=["tests/ats/jobs/test_job_1_create.py::TestJobCreate::test_job_create"],
        scope='session')
    @allure.title("ATS Edit a Job")
    @allure.description("Edit the Job in ATS - JIRA: RND-7270")
    def test_job_edit(self, get_test_info):
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

        page_header.select_ellipses_menu(page_header.EllipsesMenu.EditThisJob, page_header.OnPage.Job_Details)

        job_position_details = JobPositionDetails(self.driver)
        job_position_details.edit_job_details_fields()
        job_position_details_view.verify_header()

        page_header.select_ellipses_menu(page_header.EllipsesMenu.EditThisJob, page_header.OnPage.Job_Details)
        page_header.select_ellipses_menu(page_header.EllipsesMenu.EditJobPostingDepartmentBudgetDetails,
                                         page_header.OnPage.Job_Edit)

        job_department_budget = JobDepartmentBudget(self.driver)
        job_department_budget.edit_job_departments()
        job_position_details_view.verify_header()

        page_header.select_ellipses_menu(page_header.EllipsesMenu.EditThisJob, page_header.OnPage.Job_Details)
        page_header.select_ellipses_menu(page_header.EllipsesMenu.EditJobPostingPositionPriority,
                                         page_header.OnPage.Job_Edit)

        job_priority = JobPriority(self.driver)
        job_priority.update_priority()

        page_header.select_ellipses_menu(page_header.EllipsesMenu.EditJobPostingPositionCategory,
                                         page_header.OnPage.Job_Edit)

        job_category = JobCategory(self.driver)
        job_category.update_category()

        page_header.select_ellipses_menu(page_header.EllipsesMenu.EditThisJob, page_header.OnPage.Job_Details)
        page_header.select_ellipses_menu(page_header.EllipsesMenu.EditJobPostingPositionAttachments,
                                         page_header.OnPage.Job_Edit)

        job_attachments = JobAttachments(self.driver)
        job_attachments.update_file()

        page_header.select_ellipses_menu(page_header.EllipsesMenu.EditThisJob, page_header.OnPage.Job_Details)
        page_header.select_ellipses_menu(page_header.EllipsesMenu.EditJobPostingPositionEvaluationQuestions,
                                         page_header.OnPage.Job_Edit)

        job_evaluation_questions = JobEvaluationQuestions(self.driver)
        job_evaluation_questions.update_cqe()

        return

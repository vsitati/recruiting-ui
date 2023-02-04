import pytest
import allure
from ats_pages.login.login import Login
from ats_pages.left_menus import LeftMenus
from ats_pages.jobs.job_position_details import JobPositionDetails
from ats_pages.jobs.job_department_budget import JobDepartmentBudget
from ats_pages.jobs.job_priority import JobPriority
from ats_pages.jobs.job_category import JobCategory
from ats_pages.jobs.job_attachments import JobAttachments
from ats_pages.jobs.job_evaluation_questions import JobEvaluationQuestions


@pytest.mark.usefixtures("setup")
class TestJobCreate:

    @pytest.mark.dependency()
    @allure.title("ATS Create a Job")
    @allure.description("Create a Standard Job - JIRA: RND-7268")
    @pytest.mark.xfail()
    def test_job_create(self, get_test_info):
        login = Login(driver=self.driver)
        login.do_login(get_test_info)

        left_menu = LeftMenus(self.driver)
        left_menu.click_left_nav(left_menu.jobs)
        left_menu.click_left_nav_sub(left_menu.create_job_postings)

        job_position_details = JobPositionDetails(self.driver)
        job_position_details.fill_out_all_job_details_fields()

        job_department_budget = JobDepartmentBudget(self.driver)
        job_department_budget.fill_out_all_job_departments_fields()

        job_priority = JobPriority(self.driver)
        job_priority.setup_priority()

        job_category = JobCategory(self.driver)
        job_category.select_category()
        # upon this step, the job is created

        job_attachments = JobAttachments(self.driver)
        job_attachments.upload_file()

        job_evaluation_questions = JobEvaluationQuestions(self.driver)
        job_evaluation_questions.select_cqe()

        return

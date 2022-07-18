import pytest
import allure
from ats_pages.login import Login
from ats_pages.left_menus import LeftMenus
from ats_pages.job_position_details import JobPositionDetails
from ats_pages.job_department_budget import JobDepartmentBudget
from ats_pages.job_priority import JobPriority
from ats_pages.job_category import JobCategory
from ats_pages.job_attachments import JobAttachments
from ats_pages.job_evaluation_questions import JobEvaluationQuestions


@pytest.mark.usefixtures("setup")
class TestATSCreateJob:
    @allure.title("ATS Create Job Tests")
    @allure.description("Create a Standard Job")
    def test_create_standard_job(self, get_test_info):
        login = Login(driver=self.driver)
        login.do_login(get_test_info)

        left_menu = LeftMenus(self.driver)
        left_menu.click_left_nav(left_menu.jobs)
        left_menu.click_left_nav_sub(left_menu.create_job_postings)

        job_position_details = JobPositionDetails(self.driver)
        job_position_details.fill_out_all()
        # job_position_details.fill_out_minimum()

        job_department_budget = JobDepartmentBudget(self.driver)
        job_department_budget.fill_out_all()

        job_priority = JobPriority(self.driver)
        job_priority.setup_priority()

        job_category = JobCategory(self.driver)
        job_category.select_a_category()

        job_attachments = JobAttachments(self.driver)
        job_attachments.upload_a_file()

        job_evaluation_questions = JobEvaluationQuestions(self.driver)
        job_evaluation_questions.select_a_cqe()

        return

    @pytest.mark.skip
    @allure.description("Verify the Job in ATS")
    def test_verify_job_in_ats(self, get_test_info):
        pass

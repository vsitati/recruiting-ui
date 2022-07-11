import pytest
import allure
from ats_pages.login import Login
from ats_pages.left_menus import LeftMenus
from ats_pages.job_position_details import JobPositionDetails
from ats_pages.job_department_budget import JobDepartmentBudget
from ats_pages.job_priority import JobPriority
from ats_pages.job_category import JobCategory


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
        # job_position_details.fill_out_all()
        job_position_details.fill_out_minimum()

        job_department_budget = JobDepartmentBudget(self.driver)
        job_department_budget.fill_out_all()

        job_priority = JobPriority(self.driver)
        job_priority.fill_out()

        job_category = JobCategory(self.driver)
        job_category.select_one()

        pass

    @pytest.mark.skip
    @allure.description("Verify the Job in ATS")
    def test_verify_job_in_ats(self, get_test_info):
        pass

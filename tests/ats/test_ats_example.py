import pytest
import allure
from ats_pages.jobs.job_advanced_search_edit import JobAdvancedSearchEdit
from ats_pages.login.login import Login
from ats_pages.left_menus import LeftMenus


@pytest.mark.usefixtures("setup")
class TestRecruitingAts:
    @allure.title("ATS Example Tests")
    @allure.description("Edit Search Filter")
    def test_edit_search_filter(self, get_test_info):
        login = Login(driver=self.driver)
        login.do_login(get_test_info)

        left_menu = LeftMenus(self.driver)
        left_menu.click_left_nav(left_menu.candidates)
        left_menu.click_left_nav_sub(left_menu.upload)

        job_advanced_search = JobAdvancedSearchEdit(self.driver)
        job_advanced_search.filter_by_status("Open")

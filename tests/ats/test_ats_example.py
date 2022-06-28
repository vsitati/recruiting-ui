import pytest
import allure
from ats_pages.jobs_advanced_search import JobAdvancedSearch
from ats_pages.login import Login
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
        # left_menu.click_jobs_advanced_search()

        # jobs_advanced_search = JobAdvancedSearch(self.driver)
        # jobs_advanced_search.filter_by_status("Open")

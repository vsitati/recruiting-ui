import pytest
import allure
from ats_pages.jobs_advanced_search import JobAdvancedSearch
from ats_pages.login import Login
from ats_pages.left_menus import LeftMenus


@pytest.mark.usefixtures("setup")
class TestRecruitingAts:
    @allure.title("ATS Example Tests")
    @allure.description("Edit Search Filter")
    def test_edit_search_filter(self, config):
        login = Login(driver=self.driver)
        login.do_login(config)

        left_menu = LeftMenus(self.driver)
        left_menu.click_left_nav(left_menu.Elements.Candidates, left_menu.Elements.Upload)
        # left_menu.click_jobs_advanced_search()

        jobs_advanced_search = JobAdvancedSearch(self.driver)
        jobs_advanced_search.fileter_by_status("Open")

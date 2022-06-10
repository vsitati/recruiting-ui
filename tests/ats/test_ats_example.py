import pytest
import allure
from ats_pages.jobs_advanced_search import AdvancedSearch


@pytest.mark.usefixtures("setup")
class TestRecruitingAts:
    @allure.title("ATS Example Tests")
    @allure.description("Edit Search Filter")
    def test_edit_search_filter(self):
        _as = AdvancedSearch(driver=self.driver)
        _as.open('https://qarecruiting01-openhire.silkroad-eng.com/')
        _as.do_login(username='UFT_RM_01', password='Gators2012')
        _as.open_edit_search()
        _as.select_from_status_dropdown(text="Open")
        _as.click_apply_filter_btn()

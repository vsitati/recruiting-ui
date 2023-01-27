import pytest
import allure
from time import sleep
from ats_pages.login.login import Login
from ats_pages.page_header import PageHeader
from ats_pages.ellipses_columns import EllipsesColumns
from ats_pages.left_menus import LeftMenus
from ats_pages.candidates.candidate_advanced_search_edit import CandidateAdvancedSearchEdit
from ats_pages.candidates.advanced_search import CandidateAdvancedSearch
from test_data.test_data_details import CandidateData


@pytest.mark.usefixtures("setup")
class TestCandidateAdvancedSearch:

    @allure.title("Candidate Search: sorting columns")
    @allure.description("JIRA: RND-7440; TestRail: C270")
    def test_candidate_search_sorting(self, get_test_info):
        login = Login(driver=self.driver)
        login.do_login(get_test_info)

        left_menu = LeftMenus(self.driver)
        left_menu.click_left_nav(left_menu.candidates)
        left_menu.click_left_nav_sub(left_menu.candidates_advanced_search)
        sleep(left_menu.sleep_time)

        candidate_advanced_search = CandidateAdvancedSearch(self.driver)
        candidate_advanced_search.sort_candidate_column_header("Candidate", "desc")
        candidate_advanced_search.sort_candidate_column_header("Candidate", "asc")

        candidate_advanced_search.sort_candidate_column_header("Job Title", "asc")
        candidate_advanced_search.sort_candidate_column_header("Job Title", "desc")

        candidate_advanced_search.sort_candidate_column_header("Current Stage", "asc")
        candidate_advanced_search.sort_candidate_column_header("Current Stage", "desc")

        candidate_advanced_search.sort_candidate_column_header("Enter Date", "asc", "date")
        candidate_advanced_search.sort_candidate_column_header("Enter Date", "desc", "date")
        return

    @allure.title("Candidate Search: candidate name")
    @allure.description("JIRA: RND-7432; TestRail: C265")
    def test_candidate_search_candidate_name(self, get_test_info):
        login = Login(driver=self.driver)
        login.do_login(get_test_info)

        left_menu = LeftMenus(self.driver)
        left_menu.click_left_nav(left_menu.candidates)
        left_menu.click_left_nav_sub(left_menu.candidates_advanced_search)

        candidate_advanced_search_edit = CandidateAdvancedSearchEdit(self.driver)
        candidate_advanced_search_edit.click_edit_search()
        candidate_advanced_search_edit.click_clear_filter_btn()

        candidate_name = "Aaron"
        candidate_advanced_search_edit.enter_candidate_name(candidate_name)

        candidate_advanced_search_edit.click_apply_filter_btn()

        candidate_advanced_search = CandidateAdvancedSearch(self.driver)
        col_list = candidate_advanced_search.get_candidate_column_values("Candidate")
        candidate_advanced_search.verify_value_exist(candidate_name, col_list)

        return

    @allure.title("Candidate Search: enter date")
    @allure.description("JIRA: RND-7433; TestRail: c266")
    def test_candidate_search_enter_date(self, get_test_info):
        login = Login(driver=self.driver)
        login.do_login(get_test_info)

        left_menu = LeftMenus(self.driver)
        left_menu.click_left_nav(left_menu.candidates)
        left_menu.click_left_nav_sub(left_menu.candidates_advanced_search)
        sleep(left_menu.sleep_time)

        candidate_advanced_search_edit = CandidateAdvancedSearchEdit(self.driver)
        candidate_advanced_search_edit.click_edit_search()
        candidate_advanced_search_edit.click_clear_filter_btn()

        entered_in_the_last = 10
        candidate_advanced_search_edit.enter_entered_in_the_last(entered_in_the_last)

        candidate_advanced_search_edit.click_apply_filter_btn()

        candidate_advanced_search = CandidateAdvancedSearch(self.driver)
        col_list = candidate_advanced_search.get_candidate_column_values("Enter Date")
        candidate_advanced_search.compare_date_range(entered_in_the_last, col_list, "older")

        return

    @allure.title("Candidate Search: Current Stage")
    @allure.description("JIRA: RND-7435; TestRail: c267")
    def test_candidate_search_current_stage(self, get_test_info):
        login = Login(driver=self.driver)
        login.do_login(get_test_info)

        left_menu = LeftMenus(self.driver)
        left_menu.click_left_nav(left_menu.candidates)
        left_menu.click_left_nav_sub(left_menu.candidates_advanced_search)

        candidate_advanced_search_edit = CandidateAdvancedSearchEdit(self.driver)
        candidate_advanced_search_edit.click_edit_search()
        candidate_advanced_search_edit.click_clear_filter_btn()

        current_stage = CandidateData.candidate_current_stage.get("offer_approval")
        candidate_advanced_search_edit.select_current_stage(current_stage)

        candidate_advanced_search_edit.click_apply_filter_btn()

        candidate_advanced_search = CandidateAdvancedSearch(self.driver)
        col_list = candidate_advanced_search.get_candidate_column_values("Current Stage")
        candidate_advanced_search.verify_value_exist(current_stage, col_list)

        return

    @allure.title("Candidate Search: Country")
    @allure.description("JIRA: RND-7436; TestRail: c268")
    def test_candidate_search_country(self, get_test_info):
        login = Login(driver=self.driver)
        login.do_login(get_test_info)

        left_menu = LeftMenus(self.driver)
        left_menu.click_left_nav(left_menu.candidates)
        left_menu.click_left_nav_sub(left_menu.candidates_advanced_search)
        sleep(left_menu.sleep_time)

        candidate_advanced_search_edit = CandidateAdvancedSearchEdit(self.driver)
        candidate_advanced_search_edit.click_edit_search()
        candidate_advanced_search_edit.click_clear_filter_btn()

        country = "Canada"
        candidate_advanced_search_edit.select_country(country)
        sleep(left_menu.sleep_time)

        candidate_advanced_search_edit.click_apply_filter_btn()

        page_header = PageHeader(self.driver)
        page_header.select_ellipses_menu(page_header.EllipsesMenu.Columns, page_header.OnPage.Candidate_Search)

        ellipses_columns = EllipsesColumns(self.driver)
        ellipses_columns.select_column(ellipses_columns.Columns.Country)
        ellipses_columns.click_apply()
        sleep(left_menu.sleep_time)

        candidate_advanced_search = CandidateAdvancedSearch(self.driver)
        col_list = candidate_advanced_search.get_candidate_column_values("Country")
        candidate_advanced_search.verify_value_exist(country, col_list)

        return

    @allure.title("Candidate Search: Country and State")
    @allure.description("JIRA: RND-7437; TestRail: c269")
    def test_candidate_search_country_state(self, get_test_info):
        login = Login(driver=self.driver)
        login.do_login(get_test_info)

        left_menu = LeftMenus(self.driver)
        left_menu.click_left_nav(left_menu.candidates)
        left_menu.click_left_nav_sub(left_menu.candidates_advanced_search)
        sleep(left_menu.sleep_time)

        candidate_advanced_search_edit = CandidateAdvancedSearchEdit(self.driver)
        candidate_advanced_search_edit.click_edit_search()
        candidate_advanced_search_edit.click_clear_filter_btn()

        country = "United States"
        candidate_advanced_search_edit.select_country(country)
        sleep(left_menu.sleep_time)

        state = "New Hampshire"
        candidate_advanced_search_edit.select_state(state)
        sleep(left_menu.sleep_time)

        candidate_advanced_search_edit.click_apply_filter_btn()

        page_header = PageHeader(self.driver)
        page_header.select_ellipses_menu(page_header.EllipsesMenu.Columns, page_header.OnPage.Candidate_Search)

        ellipses_columns = EllipsesColumns(self.driver)
        ellipses_columns.select_column(ellipses_columns.Columns.Country)
        ellipses_columns.select_column(ellipses_columns.Columns.State)
        ellipses_columns.click_apply()
        sleep(left_menu.sleep_time)

        candidate_advanced_search = CandidateAdvancedSearch(self.driver)
        col_list = candidate_advanced_search.get_candidate_column_values("Country")
        candidate_advanced_search.verify_value_exist(country, col_list)
        col_list = candidate_advanced_search.get_candidate_column_values("State")
        candidate_advanced_search.verify_value_exist(state, col_list)

        return

    @allure.title("Candidate Search: recruiting manager")
    @allure.description("JIRA: RND-7438; TestRail: c264")
    def test_candidate_search_recruiting_manager(self, get_test_info):
        login = Login(driver=self.driver)
        login.do_login(get_test_info)

        left_menu = LeftMenus(self.driver)
        left_menu.click_left_nav(left_menu.candidates)
        left_menu.click_left_nav_sub(left_menu.candidates_advanced_search)
        sleep(left_menu.sleep_time)

        candidate_advanced_search_edit = CandidateAdvancedSearchEdit(self.driver)
        candidate_advanced_search_edit.click_edit_search()
        candidate_advanced_search_edit.click_clear_filter_btn()

        recruiting_manager = "auto_rm_01 Silkroad"
        candidate_advanced_search_edit.select_recruiting_manager(recruiting_manager)
        sleep(left_menu.sleep_time)

        candidate_advanced_search_edit.click_apply_filter_btn()

        page_header = PageHeader(self.driver)
        page_header.select_ellipses_menu(page_header.EllipsesMenu.Columns, page_header.OnPage.Candidate_Search)

        ellipses_columns = EllipsesColumns(self.driver)
        ellipses_columns.select_column(ellipses_columns.Columns.RecruitingManager)
        ellipses_columns.click_apply()
        sleep(left_menu.sleep_time)

        candidate_advanced_search = CandidateAdvancedSearch(self.driver)
        col_list = candidate_advanced_search.get_candidate_column_values("Recruiting Manager")
        candidate_advanced_search.verify_value_exist(recruiting_manager, col_list)

        return

    @allure.title("Candidate Search: sort by")
    @allure.description("JIRA: RND-7439; TestRail: c5469")
    def test_candidate_search_sort_by(self, get_test_info):
        login = Login(driver=self.driver)
        login.do_login(get_test_info)

        left_menu = LeftMenus(self.driver)
        left_menu.click_left_nav(left_menu.candidates)
        left_menu.click_left_nav_sub(left_menu.candidates_advanced_search)
        sleep(left_menu.sleep_time)

        candidate_advanced_search_edit = CandidateAdvancedSearchEdit(self.driver)
        candidate_advanced_search_edit.click_edit_search()
        candidate_advanced_search_edit.click_clear_filter_btn()

        sort_by = "Tracking Code"
        candidate_advanced_search_edit.select_sort_by(sort_by)
        candidate_advanced_search_edit.select_sort_by_order("Descending")

        candidate_advanced_search_edit.click_apply_filter_btn()

        page_header = PageHeader(self.driver)
        page_header.select_ellipses_menu(page_header.EllipsesMenu.Columns, page_header.OnPage.Candidate_Search)

        ellipses_columns = EllipsesColumns(self.driver)
        ellipses_columns.select_column(ellipses_columns.Columns.TrackingCode)
        ellipses_columns.click_apply()
        sleep(left_menu.sleep_time)

        candidate_advanced_search = CandidateAdvancedSearch(self.driver)
        col_list = candidate_advanced_search.get_candidate_column_values(sort_by)
        candidate_advanced_search.verify_ordering(col_list, "desc")

        return
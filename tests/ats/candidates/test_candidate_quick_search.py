import pytest
import allure
from ats_pages.login.login import Login
from ats_pages.page_header import PageHeader
from ats_pages.candidates.advanced_search import CandidateAdvancedSearch
from helpers.utils import BaseError
from common.common import Common
from time import sleep


@pytest.mark.usefixtures("setup")
class TestCandidateQuickSearch:

    @allure.title("Candidate Quick Search for All")
    @allure.description("JIRA: RND-7463; TestRail: C296")
    def test_candidate_quick_search_all(self, get_test_info):
        login = Login(driver=self.driver)
        login.do_login(get_test_info)

        page_header = PageHeader(self.driver)
        page_header.quick_search("Candidates")
        sleep(page_header.sleep_time)

        candidate_advanced_search = CandidateAdvancedSearch(self.driver)
        candidate_advanced_search.verify_is_candidate_search_result_page()
        record_count = candidate_advanced_search.get_advanced_search_count()
        assert record_count != 0, f"-- Candidate Search returns {record_count} records."
        Common.sr_logger.logger.info(f"-- Candidate Search returns {record_count} records.")

    @allure.title("Candidate Quick Search for Some")
    @allure.description("JIRA: RND-7464; TestRail: C298")
    def test_candidate_quick_search_some(self, get_test_info):
        login = Login(driver=self.driver)
        login.do_login(get_test_info)

        candidate_name = "Aaron"
        page_header = PageHeader(self.driver)
        page_header.quick_search("Candidates", candidate_name)

        candidate_advanced_search = CandidateAdvancedSearch(self.driver)
        candidate_advanced_search.verify_is_candidate_search_result_page()
        col_list = candidate_advanced_search.get_candidate_column_values("Candidate")
        candidate_advanced_search.verify_value_exist(candidate_name, col_list)
        return

    @pytest.mark.skip(reason="Jason to fix")
    @allure.title("Candidate Quick Search for All")
    @allure.description("JIRA: RND-7465; TestRail: C297")
    def test_candidate_quick_search_none(self, get_test_info):
        login = Login(driver=self.driver)
        login.do_login(get_test_info)

        candidate_name = "xyz"
        page_header = PageHeader(self.driver)
        page_header.quick_search("Candidates", candidate_name)
        sleep(page_header.sleep_time)

        candidate_advanced_search = CandidateAdvancedSearch(self.driver)
        candidate_advanced_search.verify_is_candidate_search_result_page()
        record_count = candidate_advanced_search.get_advanced_search_count()
        assert record_count == 0, f"Search result should be 0, but returns {record_count}."
        Common.sr_logger.logger.info("-- Candidate Search returns 0 record correctly.")

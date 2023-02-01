import pytest
import allure
from ats_pages.login.login import Login
from ats_pages.page_header import PageHeader
from ats_pages.jobs.job_advanced_search_result import JobAdvancedSearchResult
from ats_pages.candidates.advanced_search import CandidateAdvancedSearch
from helpers.utils import BaseError
from common.common import Common
from time import sleep


@pytest.mark.usefixtures("setup")
class TestJobQuickSearch:

    @allure.title("Job Quick Search for All")
    @allure.description("JIRA: RND-7458; TestRail: c237")
    def test_job_quick_search_all(self, get_test_info):
        login = Login(driver=self.driver)
        login.do_login(get_test_info)

        page_header = PageHeader(self.driver)
        page_header.quick_search("Jobs")
        sleep(page_header.sleep_time)

        job_advanced_search_result = JobAdvancedSearchResult(self.driver)
        job_advanced_search_result.verify_is_job_search_result_page()
        record_count = job_advanced_search_result.verify_record_count()
        Common.sr_logger.logger.info(f"-- DEBUG: RECORD VALUE - {record_count}")
        if int(record_count) == 0:
            raise BaseError(f"Search result should return some records, but only {record_count}.")
        else:
            Common.sr_logger.logger.info(f"-- Job Search returns {record_count} records.")

    @allure.title("Job Quick Search for Some")
    @allure.description("JIRA: RND-7459; TestRail: c238")
    def test_job_quick_search_some(self, get_test_info):
        login = Login(driver=self.driver)
        login.do_login(get_test_info)

        job_title = "Auto_Internal_Job"
        page_header = PageHeader(self.driver)
        page_header.quick_search("Jobs", job_title)

        job_advanced_search_result = JobAdvancedSearchResult(self.driver)
        job_advanced_search_result.verify_is_job_search_result_page()
        candidate_advanced_search = CandidateAdvancedSearch(self.driver)

        col_list = candidate_advanced_search.get_candidate_column_values("Internal Job Title")
        candidate_advanced_search.verify_value_exist(job_title, col_list)
        return

    @allure.title("Candidate Quick Search for None")
    @allure.description("JIRA: RND-7460; TestRail: c299")
    def test_job_quick_search_none(self, get_test_info):
        login = Login(driver=self.driver)
        login.do_login(get_test_info)

        job_title = "xyz"
        page_header = PageHeader(self.driver)
        page_header.quick_search("Jobs", job_title)
        sleep(page_header.sleep_time)

        job_advanced_search_result = JobAdvancedSearchResult(self.driver)
        job_advanced_search_result.verify_is_job_search_result_page()
        record_count = job_advanced_search_result.verify_record_count()
        if int(record_count) == 0:
            Common.sr_logger.logger.info("-- Job Search returns 0 record correctly.")
        else:
            raise BaseError(f"Search result should be 0, but returns {record_count}.")

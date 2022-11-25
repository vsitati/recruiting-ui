import pytest
import allure
from cx_pages.career_sites import CareerSites
from cx_pages.jobs_search import JobSearch
from cx_pages.login import Login
from ats_pages.login.login import Login as AtsLogin
from cx_pages.cx_quick_apply import QuickApply
from test_data.test_data_details import TestData
from ats_pages.left_menus import LeftMenus
from ats_pages.candidates.advanced_search import CandidateAdvancedSearch
from ats_pages.candidates.candidate_resume_profile import CandidateResumeProfile


@pytest.mark.usefixtures("setup")
class TestQuickApplyExternal:
    @allure.title("Candidate Apply - QuickApply - External Portal")
    @allure.description("Random Job Quick Apply")
    def test_random_job_quick_apply_external(self, get_test_info):
        login = Login(driver=self.driver)
        login.do_login(env_info=get_test_info)

        cs = CareerSites(driver=self.driver)
        data = cs.get_career_sites(site_section="external")
        result = cs.filter_career_site(data=data, site_name="Corporate Career Portal")
        name, portal, settings = result
        cs.open_url(portal)
        assert cs.get_title() == "QA Automation Only - SilkRoad Talent Activation"

        js = JobSearch(driver=self.driver)
        job_elem, job_title = js.find_job(random_job=True)
        js.open_job(job_elem=job_elem)
        assert job_title in js.get_title()

        qa = QuickApply(driver=self.driver)
        form_details = TestData.quick_apply_form_data
        qa.click_cx_job_apply_btn()
        qa.fill_in_quick_apply_form(**form_details)
        assert qa.get_h2_tag_name() == "Thank You for Applying"

        # Login to ATS
        ats_login = AtsLogin(driver=self.driver)
        ats_login.do_login(get_test_info)

        left_menu = LeftMenus(driver=self.driver)
        left_menu.click_left_nav(left_menu.candidates)
        left_menu.click_left_nav(left_menu.candidates_advanced_search)
        cas = CandidateAdvancedSearch(driver=self.driver)
        candidate_name = f"{form_details.get('firstname')} {form_details.get('lastname')}"
        cas.open_candidate_profile(candidate_name=candidate_name)

        crp = CandidateResumeProfile(driver=self.driver)
        assert crp.verify_candidate_name(candidate_name=candidate_name) is True
        assert crp.verify_candidate_email(candidate_email=form_details.get('email')) is True

import time

import pytest
import allure

from ats_pages.administration.fee_agencies import FeeAgencies
from cx_pages.jobs_search import JobSearch
from config import Config
from ats_pages.login.login import Login as AtsLogin
from cx_pages.cx_quick_apply import QuickApply
from test_data.test_data_details import SrTestData
from ats_pages.left_menus import LeftMenus
from ats_pages.candidates.advanced_search import CandidateAdvancedSearch
from ats_pages.candidates.candidate_resume_profile import CandidateResumeProfile
from helpers.utils import get_basename_from_file_path


@pytest.mark.regression_grp_f
@pytest.mark.usefixtures("setup")
class TestFeeAgencyQuickApplyDoNotAllowSameJobDuplicates:
    @allure.description("Fee Agency Quick Apply Do not allow same job duplicates")
    def test_fee_agency_quick_apply_do_not_allow_same_job_duplicates(self, get_test_info):
        # Login to ATS as RM
        login = AtsLogin(driver=self.driver)
        login.do_login(get_test_info)

        assert login.is_element_visible(locator=login.quick_search_text) is True

        # Navigate to Administration->Fee Agency
        left_menu = LeftMenus(self.driver)
        left_menu.click_left_nav(left_menu.administration)
        left_menu.click_left_nav_sub(left_menu.fee_agencies)

        # Open Fee Agency Profile
        fee_agency = FeeAgencies(self.driver)
        fee_agency.open_fee_agency_profile(fee_agency_name="Apple One")
        fee_agency_email = fee_agency.get_fee_agency_email()
        fee_agency.get_duplicate_option()
        fee_agency.save_button_duplicate()
        fee_agency.open_fee_agency_profile(fee_agency_name="Apple One")

        # Login To Cx
        cx_link = fee_agency.get_cx_link(site_name="CorporateCareerPortal")
        fee_agency.open_url(cx_link)

        fee_agency.login_to_fee_agency(fee_agency_email)
        assert fee_agency.get_title() == "QA Automation Only - SilkRoad Talent Activation"

        # Apply to Job
        js = JobSearch(driver=self.driver)
        job_elem, job_title = js.find_job(random_job=True)
        js.open_job(job_elem=job_elem)
        assert job_title in js.get_title()

        qa = QuickApply(driver=self.driver)
        td = SrTestData()
        form_details = td.get_quick_apply_form_data(parent_folder=Config.env_config["path_to_resumes"])
        qa.click_cx_job_apply_btn()
        qa.fill_in_quick_apply_form(**form_details)
        assert qa.get_success_message() == "Thank You for the Submittal"

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
        assert crp.verify_candidate_name() == candidate_name
        assert crp.verify_candidate_email() == f"{form_details.get('email')}"
        assert crp.verify_source() == "Apple One"

        crp.open_attachment_tab()
        crp.get_attachment_names()
        attachments = crp.get_attachment_names()
        assert get_basename_from_file_path(file_path=form_details.get("file_path")) in attachments

        # Navigate to Administration->Fee Agency
        left_menu = LeftMenus(self.driver)
        left_menu.click_left_nav(left_menu.administration)
        left_menu.click_left_nav(left_menu.fee_agencies)
        # Open Fee Agency Profile
        fee_agency = FeeAgencies(self.driver)
        fee_agency.open_fee_agency_profile(fee_agency_name="Apple One")
        fee_agency_email = fee_agency.get_fee_agency_email()

        # Login To Cx
        cx_link = fee_agency.get_cx_link(site_name="CorporateCareerPortal")
        fee_agency.open_url(cx_link)

        fee_agency.login_to_fee_agency(fee_agency_email)
        assert fee_agency.get_title() == "QA Automation Only - SilkRoad Talent Activation"

        # Apply to the same Job second time
        second_job_elem, second_job_title = js.find_job(title=job_title)
        js.open_job(job_elem=second_job_elem)
        assert second_job_title in js.get_title()

        qa.click_cx_job_apply_btn()
        qa.fill_in_quick_apply_form(**form_details)

        assert fee_agency.candidate_already_exists() == "Candidate Already Exists"

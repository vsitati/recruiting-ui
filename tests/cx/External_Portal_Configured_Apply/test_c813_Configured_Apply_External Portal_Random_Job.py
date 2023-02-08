from time import sleep

import allure
import pytest

from common.common_configured_apply import CommonConfiguredApply
# from cx_pages.career_site_settings.career_site_settings import CareerSiteSettings
from ats_pages.candidates.advanced_search import CandidateAdvancedSearch
from ats_pages.candidates.candidate_resume_profile import CandidateResumeProfile
from ats_pages.left_menus import LeftMenus
from ats_pages.login.login import Login as AtsLogin
from cx_pages.career_site_settings.career_site_settings import CareerSiteSettings
from cx_pages.career_site_settings.manage_application_form_settings import ManageApplicationFormSettings
from cx_pages.career_sites import CareerSites
from cx_pages.jobs_search import JobSearch
from cx_pages.login import Login
from helpers.utils import get_basename_from_file_path


@pytest.mark.usefixtures("setup")
class TestConfiguredApplyExternalPortalRandomJob:
    @allure.description("Test Configured Apply External Portal Random Job")
    def test_configured_apply_external_portal_random_job(self, get_test_info):
        language = "english"
        login = Login(driver=self.driver)
        login.do_login(env_info=get_test_info)

        cs = CareerSites(driver=self.driver)
        data = cs.get_career_sites(site_section="external")
        result = cs.filter_career_site(data=data, site_name="Corporate Career Portal")
        name, portal_url, settings_url = result
        cs.open_url(settings_url)

        # Career Site Settings
        css = CareerSiteSettings(driver=self.driver)
        css.open_setting(setting="application_form")
        css.custom_apply_form_switch()
        os_link = css.get_all_hrefs(specific_href="ApplicationForm")
        css.open_url(os_link)
        css.names_pages()
        css.click_add_options_button()
        css.options_to()
        css.click_save_button_modal()
        css.save_page()
        css.container_function()
        publish_form = css.get_all_hrefs(link_text="PageGroupPublish")
        css.open_url(publish_form)
        css.options_to()
        css.click_save_button_modal()
        css.save_page()

        # css.extract_data()
        # js = JobSearch(driver=self.driver)
        # job_elem, job_title = js.find_job(random_job=True)
        # js.open_job(job_elem=job_elem)
        # assert job_title in js.get_title()
        #
        # css.open_url(publish_form)
        mafs = ManageApplicationFormSettings(driver=self.driver)
        form_name = css.extract_data()  # this is the form name you generate
        mafs.configure_application_form(form_name=form_name, function="visibility", view=True)
        css.container_function()
        css.publish_button_click()
        mafs.enable_application_form_type()

        cs.open_url(portal_url)
        assert cs.get_title() == "QA Automation Only - SilkRoad Talent Activation"

        js = JobSearch(driver=self.driver)
        job_elem, job_title = js.find_job(random_job=True)
        js.open_job(job_elem=job_elem)
        assert job_title in js.get_title()
        mafs.click_cx_multi_job_apply_btn()

        first_name, last_name = mafs.random_name_generator()
        email = mafs.random_email_generator()
        form_details = mafs.fill_apply_form_data(first_name, last_name, email, "path/to/file",
                                                 mafs.random_phone_generator(),
                                                 "Jr.", "A.", "123 Main St.")
        mafs.final_job_apply_btn()
        assert mafs.get_success_message() == "VIEW OTHER OPENINGS"
        # Login to ATS
        ats_login = AtsLogin(driver=self.driver)
        ats_login.do_login(get_test_info)
        #
        left_menu = LeftMenus(driver=self.driver)
        left_menu.click_left_nav(left_menu.candidates)
        left_menu.click_left_nav(left_menu.candidates_advanced_search)
        cas = CandidateAdvancedSearch(driver=self.driver)
        candidate_name = first_name
        cas.open_candidate_profile(candidate_name=candidate_name)
        input("wstwt4r")
        crp = CandidateResumeProfile(driver=self.driver)
        assert crp.verify_candidate_name() == candidate_name
        assert crp.verify_candidate_email() == f"{form_details.get('email')}"
        #
        crp.open_attachment_tab()
        crp.get_attachment_names()
        attachments = crp.get_attachment_names()
        assert get_basename_from_file_path(file_path=form_details.get("file_path")) in attachments

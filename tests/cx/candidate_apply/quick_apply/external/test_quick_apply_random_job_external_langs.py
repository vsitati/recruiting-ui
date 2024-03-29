import pytest
import allure
from cx_pages.career_sites import CareerSites
from cx_pages.jobs_search import JobSearch
from cx_pages.login import Login
from config import Config
from ats_pages.login.login import Login as AtsLogin
from cx_pages.cx_quick_apply import QuickApply
from test_data.test_data_details import SrTestData
from ats_pages.candidates.advanced_search import CandidateAdvancedSearch
from ats_pages.candidates.candidate_resume_profile import CandidateResumeProfile
from helpers.utils import get_basename_from_file_path
from cx_pages.career_site_settings.manage_general_settings import ManageGeneralSettings
from cx_pages.career_site_settings.career_site_settings import CareerSiteSettings
from cx_pages.career_site_settings.manage_languages import ManageLanguages
from cx_pages.career_site_settings.manage_application_form_settings import ManageApplicationFormSettings


@pytest.mark.regression_grp_e
@pytest.mark.usefixtures("setup")
class TestQuickApplyRandomJobExternalLangs:
    @pytest.mark.parametrize("language", ["french", "spanish", "german"])
    @allure.description("Random Job Quick Apply External - foreign languages: TestRail: c839, c840, c841")
    def test_random_job_quick_apply_external_langs(self, get_test_info, language):
        login = Login(driver=self.driver)
        login.do_login(env_info=get_test_info)

        cs = CareerSites(driver=self.driver)
        data = cs.get_career_sites(site_section="external")
        result = cs.filter_career_site(data=data, site_name="Corporate Career Portal")
        name, portal_url, settings_url = result
        cs.open_url(settings_url)

        # Career Site Settings
        css = CareerSiteSettings(driver=self.driver)
        css.open_setting(setting="general")

        # Manage Settings
        mgs = ManageGeneralSettings(driver=self.driver)
        mgs.change_portal_default_language(language=language)
        mgs.click_cx_settings_save_btn()

        css.open_setting(setting="languages")
        ml = ManageLanguages(driver=self.driver)
        ml.set_given_langauge_to_default_only(language=language, enable=True)
        ml.click_language_setting_save_btn()

        # Enable Quick Apply
        css.open_setting(setting="application_form")
        mafs = ManageApplicationFormSettings(driver=self.driver)
        mafs.manage_application_form()

        cs.open_url(portal_url)

        js = JobSearch(driver=self.driver)
        text_data = SrTestData.cx_portal_language_text.get(language, "")
        assert text_data.get("search_input_placeholder_text") == js.get_job_search_input_placeholder_text()
        assert text_data.get("submit_resume_message") == js.get_submit_resume_message()

        job_elem, job_title = js.find_job(random_job=True)
        js.open_job(job_elem=job_elem)
        assert job_title in js.get_title()

        qa = QuickApply(driver=self.driver)
        td = SrTestData()
        form_details = td.get_quick_apply_form_data(parent_folder=Config.env_config["path_to_resumes"])
        qa.click_cx_job_apply_btn()

        assert qa.get_firstname_label_text() == text_data.get("firstname_label")
        assert qa.get_lastname_label_text() == text_data.get("lastname_label")
        assert qa.get_email_label_text() == text_data.get("email_label")
        assert qa.get_choose_file_btn_label_text() == text_data.get("choose_file_btn_label")

        qa.fill_in_quick_apply_form(**form_details)
        assert qa.get_success_message() == text_data.get("application_successful_message")

        # Login to ATS
        ats_login = AtsLogin(driver=self.driver)
        ats_login.do_login(get_test_info)

        cas = CandidateAdvancedSearch(driver=self.driver)
        candidate_name = f"{form_details.get('firstname')} {form_details.get('lastname')}"
        cas.open_candidate_profile(candidate_name=candidate_name)

        crp = CandidateResumeProfile(driver=self.driver)
        assert crp.verify_candidate_name() == candidate_name
        assert crp.verify_candidate_email() == f"{form_details.get('email')}"

        crp.open_attachment_tab()
        crp.get_attachment_names()
        attachments = crp.get_attachment_names()
        assert get_basename_from_file_path(file_path=form_details.get("file_path")) in attachments

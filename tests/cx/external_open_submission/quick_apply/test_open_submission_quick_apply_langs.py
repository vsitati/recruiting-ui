import pytest
import allure
from cx_pages.career_sites import CareerSites
from cx_pages.jobs_search import JobSearch
from cx_pages.login import Login
from config import Config
from ats_pages.login.login import Login as AtsLogin
from cx_pages.cx_quick_apply import QuickApply
from test_data.test_data_details import SrTestData
from ats_pages.left_menus import LeftMenus
from ats_pages.candidates.advanced_search import CandidateAdvancedSearch
from ats_pages.candidates.candidate_resume_profile import CandidateResumeProfile
from helpers.utils import get_basename_from_file_path
from cx_pages.career_site_settings.manage_general_settings import ManageGeneralSettings
from cx_pages.career_site_settings.career_site_settings import CareerSiteSettings
from cx_pages.career_site_settings.manage_languages import ManageLanguages
from utils.drivers import Drivers


@pytest.mark.usefixtures("setup")
class TestQuickApplyOpenSubmissionLangs:

    @pytest.mark.parametrize("lang", ["French", "Spanish", "German"])
    @allure.description("Quick Apply Open Submission foreign languages, TestRail c805, c807, c890, ")
    def test_random_job_quick_apply_open_submission_langs(self, get_test_info, lang):
        if lang == "French":
            submit_resume_message = \
                "Vous ne trouvez pas l'offre que vous recherchez ?Soumettre votre curriculum vitae / CV."
            success_message = "Merci d’avoir soumis votre curriculum vitae"
        elif lang == "Spanish":
            submit_resume_message = "¿No encuentras la oportunidad perfecta? Enviar su CV/currículum."
            success_message = "Gracias por enviar su CV/currículum vitae"
        elif lang == "German":
            submit_resume_message = "Haben Sie keine passende Stelle gefunden? Reichen Sie Ihren Lebenslauf ein."
            success_message = "Danke das Sie Ihren Lebenslauf eingereicht haben"
        else:
            raise Exception("Please use French, Spanish or German")

        language = lang
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
        cs.open_url(portal_url)
        assert cs.get_title() == "QA Automation Only - SilkRoad Talent Activation"

        config = Config.env_config
        driver2 = Drivers.get_driver(config, language)
        cs2 = CareerSites(driver=driver2)
        cs2.open_url(portal_url)
        assert cs2.get_title() == "QA Automation Only - SilkRoad Talent Activation"

        js = JobSearch(driver=self.driver)
        assert js.get_submit_resume_message() == submit_resume_message
        os_link = js.get_all_hrefs(specific_href="QuickApply")
        js.open_url(os_link)

        qa = QuickApply(driver=self.driver)
        td = SrTestData()
        form_details = td.get_quick_apply_form_data(parent_folder=Config.env_config["path_to_resumes"])
        qa.fill_in_quick_apply_form(**form_details)
        assert qa.get_success_message() == success_message

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

        crp.open_attachment_tab()
        crp.get_attachment_names()
        attachments = crp.get_attachment_names()
        assert get_basename_from_file_path(file_path=form_details.get("file_path")) in attachments

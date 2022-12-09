import pytest
import allure
from cx_pages.career_sites import CareerSites
from cx_pages.jobs_search import JobSearch
from cx_pages.login import Login
from cx_pages.cx_quick_apply import QuickApply
from cx_pages.career_site_settings.manage_general_settings import ManageGeneralSettings
from cx_pages.career_site_settings.career_site_settings import CareerSiteSettings
from cx_pages.career_site_settings.manage_languages import ManageLanguages
from utils.drivers import Drivers
from config import Config


@pytest.mark.usefixtures("setup")
class TestQuickApplyRandomJobExternalDefaultPortalLanguageScenario2:
    @allure.description("Random Job Quick Apply External Default Portal Language Scenario 2")
    def test_random_job_quick_apply_external_default_portal_language_scenario2(self, get_test_info):
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
        css.open_setting(setting="general")

        # Manage Settings
        mgs = ManageGeneralSettings(driver=self.driver)
        mgs.change_portal_default_language(language=language)
        mgs.click_cx_settings_save_btn()

        css.open_setting(setting="languages")
        ml = ManageLanguages(driver=self.driver)
        ml.enable_language("english", enable=True)
        ml.enable_language("french", enable=True)
        ml.click_language_setting_save_btn()

        # start a new driver, so we can confirm in different browser language
        # todo find a better way of doing this than launching a new browser

        config = Config.env_config
        driver2 = Drivers.get_driver(config, "french")
        cs = CareerSites(driver=driver2)
        cs.open_url(portal_url)
        assert cs.get_title() == "QA Automation Only - SilkRoad Talent Activation"

        js = JobSearch(driver=driver2)
        job_elem, job_title = js.find_job(random_job=True)
        js.open_job(job_elem=job_elem)
        assert job_title in js.get_title()

        qa = QuickApply(driver=driver2)
        qa.click_cx_job_apply_btn()
        assert qa.get_file_upload_instructions_text() == "Téléchargez un fichier doc, docx, htm, html, odt, pdf, " \
                                                         "rtf ou txt. La pièce jointe doit être inférieure à 10 Mo."

        driver2.quit()

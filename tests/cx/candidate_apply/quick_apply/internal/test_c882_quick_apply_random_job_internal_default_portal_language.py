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


@pytest.mark.regression_grp_e
@pytest.mark.usefixtures("setup")
class TestQuickApplyRandomJobInternalDefaultPortalLanguage:
    @allure.description("Random Job Quick Apply Internal Default Portal Language")
    def test_random_job_quick_apply_internal_default_portal_language(self, get_test_info):
        language = "english"
        login = Login(driver=self.driver)
        login.do_login(env_info=get_test_info)

        cs = CareerSites(driver=self.driver)
        data = cs.get_career_sites(site_section="internal")
        result = cs.filter_career_site(data=data, site_name="Internal Career Page")
        name, portal_url, settings_url = result
        cs.open_url(settings_url)

        # Career Site Settings
        css = CareerSiteSettings(driver=self.driver)
        css.open_setting(setting="general", site="internal")

        # Manage Settings
        mgs = ManageGeneralSettings(driver=self.driver)
        mgs.change_portal_default_language(language=language)
        mgs.click_cx_settings_save_btn()

        css.open_setting(setting="languages", site="internal")
        ml = ManageLanguages(driver=self.driver)
        ml.set_given_langauge_to_default_only(language=language, enable=True)
        ml.click_language_setting_save_btn()

        # start a new driver, so we can confirm in different browser language

        config = Config.env_config
        driver2 = Drivers.get_driver(config, "french")
        cs2 = CareerSites(driver=driver2)
        cs2.open_url(portal_url)
        assert cs2.get_title() == "QA Automation Only - SilkRoad Talent Activation"

        js = JobSearch(driver=driver2)
        job_elem, job_title = js.find_job(random_job=True)
        js.open_job(job_elem=job_elem)
        assert job_title in js.get_title()

        qa = QuickApply(driver=driver2)
        qa.click_cx_job_apply_btn()
        assert qa.get_file_upload_instructions_text() == "Upload a doc, docx, htm, html, odt, pdf, rtf, or txt " \
                                                         "file. Attachment must be less than 10 MB."

        driver2.quit()

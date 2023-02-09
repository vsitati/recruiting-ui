import pytest
import allure
from cx_pages.career_sites import CareerSites
from cx_pages.jobs_search import JobSearch
from cx_pages.login import Login
from cx_pages.career_site_settings.manage_general_settings import ManageGeneralSettings
from cx_pages.career_site_settings.career_site_settings import CareerSiteSettings
from cx_pages.career_site_settings.manage_languages import ManageLanguages
from cx_pages.career_site_settings.manage_application_form_settings import ManageApplicationFormSettings


@pytest.mark.regression_grp_h
@pytest.mark.usefixtures("setup")
class TestQuickApplyOpenSubmissionDisabled:
    @allure.description("Quick Apply Open Submission Disabled")
    def test_random_job_quick_apply_open_submission_disabled(self, get_test_info, assertion=None):
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
        css.open_setting(setting="open_submission")

        # Manage Settings
        mgs = ManageGeneralSettings(driver=self.driver)
        mgs.open_submission_choice()
        mgs.click_save_button()

        # Disable open submission and assert the link is not present on the page
        css.open_setting(setting="languages")
        ml = ManageLanguages(driver=self.driver)
        ml.set_given_langauge_to_default_only(language=language, enable=True)
        ml.click_language_setting_save_btn()

        # Enable Quick Apply
        css.open_setting(setting="application_form")
        mafs = ManageApplicationFormSettings(driver=self.driver)
        mafs.manage_application_form()

        cs.open_url(portal_url)
        assert cs.get_title() == "QA Automation Only - SilkRoad Talent Activation"
        js = JobSearch(driver=self.driver)
        assert "Not finding the perfect opportunity? Submit Your Resume/CV." not in js.get_page_source()
        self.driver.back()
        css.open_setting(setting="open_submission")
        mgs.open_submission_click()
        mgs.click_save_button()
        cs.open_url(portal_url)

        # confirm open submission link is present on the web page
        js = JobSearch(driver=self.driver)
        assert js.get_submit_resume_message() == "Not finding the perfect opportunity? Submit Your Resume/CV."

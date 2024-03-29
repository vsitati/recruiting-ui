import pytest
import allure
from cx_pages.career_sites import CareerSites
from cx_pages.jobs_search import JobSearch
from cx_pages.login import Login
from cx_pages.cx_quick_apply import QuickApply
from cx_pages.career_site_settings.manage_general_settings import ManageGeneralSettings
from cx_pages.career_site_settings.career_site_settings import CareerSiteSettings
from cx_pages.career_site_settings.manage_languages import ManageLanguages
from cx_pages.career_site_settings.manage_application_form_settings import ManageApplicationFormSettings


@pytest.mark.regression_grp_f
@pytest.mark.usefixtures("setup")
class TestQuickApplyRandomJobExternalFormNotCompleted:
    @allure.description("C11 - Random Job Quick Apply External Form Not Completed")
    def test_random_job_quick_apply_external_form_not_completed(self, get_test_info):
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
        ml.set_given_langauge_to_default_only(language=language, enable=True)
        ml.click_language_setting_save_btn()

        # Enable Quick Apply
        css.open_setting(setting="application_form")
        mafs = ManageApplicationFormSettings(driver=self.driver)
        mafs.manage_application_form()

        cs.open_url(portal_url)
        assert cs.get_title() == "QA Automation Only - SilkRoad Talent Activation"

        js = JobSearch(driver=self.driver)
        job_elem, job_title = js.find_job(random_job=True)
        js.open_job(job_elem=job_elem)
        assert job_title in js.get_title()

        qa = QuickApply(driver=self.driver)
        qa.click_cx_job_apply_btn()
        apply_elem = qa.driver.find_element_by_locator(qa.apply_btn)
        qa.driver.execute_script("arguments[0].scrollIntoView();", apply_elem)
        qa.do_click(apply_elem)

        assert qa.get_invalid_firstname_error_text() == "\"First Name\" is required."
        assert qa.get_invalid_lastname_error_text() == "\"Last Name\" is required."
        assert qa.get_invalid_email_error_text() == "\"Email Address\" is required."
        assert qa.get_invalid_resume_error_text() == "Please upload a Resume/CV file."

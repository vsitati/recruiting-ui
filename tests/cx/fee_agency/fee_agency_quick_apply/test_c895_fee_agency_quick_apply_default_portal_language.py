import pytest
import allure

from ats_pages.administration.fee_agencies import FeeAgencies
from cx_pages.career_site_settings.career_site_settings import CareerSiteSettings
from cx_pages.career_site_settings.manage_general_settings import ManageGeneralSettings
from cx_pages.career_site_settings.manage_languages import ManageLanguages
from cx_pages.career_sites import CareerSites
from cx_pages.jobs_search import JobSearch
from config import Config
from ats_pages.login.login import Login as AtsLogin
from cx_pages.cx_quick_apply import QuickApply
from cx_pages.login import Login
from ats_pages.left_menus import LeftMenus
from utils.drivers import Drivers


@pytest.mark.regression_grp_e
@pytest.mark.usefixtures("setup")
class TestFeeAgencyQuickApplyDefaultPortalLanguage:
    @allure.description("C895 - Fee Agency Quick Apply Default Portal Language")
    def test_fee_agency_quick_apply_default_portal_language(self, get_test_info):
        # Set CX Portal Language to English and disable all other languages
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

        # Login to ATS as RM
        login = AtsLogin(driver=self.driver)
        login.do_login(get_test_info)

        assert login.is_element_visible(locator=login.quick_search) is True

        # Navigate to Administration->Fee Agency
        left_menu = LeftMenus(driver=self.driver)
        left_menu.click_left_nav(left_menu.administration)
        left_menu.click_left_nav_sub(left_menu.fee_agencies)

        # Open Fee Agency Profile
        fee_agency = FeeAgencies(driver=self.driver)
        fee_agency.open_fee_agency_profile(fee_agency_name="Apple One")
        fee_agency_email = fee_agency.get_fee_agency_email()
        cx_link = fee_agency.get_cx_link(site_name="CorporateCareerPortal")

        # Login To Cx with different browser language and validate language is English
        config = Config.env_config
        driver2 = Drivers.get_driver(config, "french")
        fe2 = FeeAgencies(driver=driver2)
        fe2.open_url(cx_link)

        fe2.login_to_fee_agency(fee_agency_email)
        assert fe2.get_title() == "QA Automation Only - SilkRoad Talent Activation"

        js = JobSearch(driver=driver2)
        job_elem, job_title = js.find_job(random_job=True)
        js.open_job(job_elem=job_elem)
        assert job_title in js.get_title()

        qa = QuickApply(driver=driver2)
        qa.click_cx_job_apply_btn()
        assert qa.get_file_upload_instructions_text() == "Upload a doc, docx, htm, html, odt, pdf, rtf, or txt " \
                                                         "file. Attachment must be less than 10 MB."
        driver2.quit()

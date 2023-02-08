import allure
from helpers.utils import BaseError
from functools import partial
from common.common import Common
from selenium.webdriver.common.by import By
from common.common_configured_apply import CommonConfiguredApply


class Elements:
    career_site_settings_list = (By.CSS_SELECTOR, ".sr-wrapper.sr-wrapper--large")


class CareerSiteSettings(Elements, CommonConfiguredApply, Common):
    def __init__(self, driver):
        super().__init__(driver)

    def get_career_site_setting_link(self, setting):
        all_href_elems = self.get_all_hrefs()
        setting_link, *_ = [href_elem.get_attribute("href")
                            for href_elem in all_href_elems
                            if href_elem.get_attribute("title") == setting]
        return setting_link

    def open_setting(self, setting, site="external"):
        # External Career Site Settings
        if site == "external":
            settings = dict(
                general=partial(self.open_url, self.get_career_site_setting_link(setting="General")),
                colors=partial(self.open_url, self.get_career_site_setting_link(setting="Colors")),
                font=partial(self.open_url, self.get_career_site_setting_link(setting="Font")),
                presubmission_text=partial(self.open_url,
                                           self.get_career_site_setting_link(setting="Presubmission Text")),
                fee_agency_presubmission_text=partial(self.open_url, self.get_career_site_setting_link(
                    setting="Fee Agency Presubmission Text")),
                google_integrations=partial(self.open_url,
                                            self.get_career_site_setting_link(setting="Google Integrations")),
                footer=partial(self.open_url, self.get_career_site_setting_link(setting="Footer")),
                social_media=partial(self.open_url, self.get_career_site_setting_link(setting="Social Media")),
                cookie_policy_acknowledgement=partial(self.open_url, self.get_career_site_setting_link(
                    setting="Cookie Policy Acknowledgement")),
                application_form=partial(self.open_url, self.get_career_site_setting_link(setting="Application Form")),
                fee_agency_application_form=partial(self.open_url, self.get_career_site_setting_link(
                    setting="Fee Agency Application Form")),
                open_submission=partial(self.open_url, self.get_career_site_setting_link(setting="Open Submission")),
                job_details_page=partial(self.open_url, self.get_career_site_setting_link(setting="Job Details Page")),
                fee_agency_job_details_page=partial(self.open_url, self.get_career_site_setting_link(
                    setting="Fee Agency Job Details Page")),
                job_list=partial(self.open_url, self.get_career_site_setting_link(setting="Job List")),
                email=partial(self.open_url, self.get_career_site_setting_link(setting="Email")),
                images=partial(self.open_url, self.get_career_site_setting_link(setting="Images")),
                languages=partial(self.open_url, self.get_career_site_setting_link(setting="Languages")),
                gdpr=partial(self.open_url, self.get_career_site_setting_link(setting="GDPR"))
            )
        else:
            # Internal Career Site Settings
            settings = dict(
                general=partial(self.open_url, self.get_career_site_setting_link(setting="General")),
                colors=partial(self.open_url, self.get_career_site_setting_link(setting="Colors")),
                font=partial(self.open_url, self.get_career_site_setting_link(setting="Font")),
                presubmission_text=partial(self.open_url,
                                           self.get_career_site_setting_link(setting="Presubmission Text")),
                google_integrations=partial(self.open_url,
                                            self.get_career_site_setting_link(setting="Google Integrations")),
                footer=partial(self.open_url, self.get_career_site_setting_link(setting="Footer")),
                social_media=partial(self.open_url, self.get_career_site_setting_link(setting="Social Media")),
                cookie_policy_acknowledgement=partial(self.open_url, self.get_career_site_setting_link(
                    setting="Cookie Policy Acknowledgement")),
                application_form=partial(self.open_url, self.get_career_site_setting_link(setting="Application Form")),
                job_details_page=partial(self.open_url, self.get_career_site_setting_link(setting="Job Details Page")),
                job_list=partial(self.open_url, self.get_career_site_setting_link(setting="Job List")),
                email=partial(self.open_url, self.get_career_site_setting_link(setting="Email")),
                images=partial(self.open_url, self.get_career_site_setting_link(setting="Images")),
                languages=partial(self.open_url, self.get_career_site_setting_link(setting="Languages")),
                gdpr=partial(self.open_url, self.get_career_site_setting_link(setting="GDPR"))
            )

        try:
            return settings.get(setting)()
        except TypeError:
            raise BaseError(f"Valid Settings: {list(settings.keys())}")

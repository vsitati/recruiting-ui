import pytest
import allure

from ats_pages.administration.fee_agencies import FeeAgencies
from ats_pages.login.login import Login as AtsLogin
from ats_pages.left_menus import LeftMenus


@pytest.mark.usefixtures("setup")
class TestFeeAgencyQuickApplyInvalidEmailAddress:
    @allure.description("Fee Agency Quick Apply Invalid Email Address")
    def test_fee_agency_quick_apply_invalid_email_address(self, get_test_info):
        # Login to ATS as RM
        login = AtsLogin(driver=self.driver)
        login.do_login(get_test_info)

        assert login.is_element_visible(locator=login.quick_search) is True

        # Navigate to Administration->Fee Agency
        left_menu = LeftMenus(self.driver)
        left_menu.click_left_nav(left_menu.administration)
        left_menu.click_left_nav_sub(left_menu.fee_agencies)

        # Open Fee Agency Profile
        fee_agency = FeeAgencies(self.driver)
        fee_agency.open_fee_agency_profile(fee_agency_name="Apple One")
        fee_agency_email = fee_agency.get_fee_agency_empty_email()

        # Login To Cx
        cx_link = fee_agency.get_cx_link(site_name="CorporateCareerPortal")
        fee_agency.open_url(cx_link)
        fee_agency.login_to_fee_agency(fee_agency_email)
        assert r"""Email Address" is required.""" in fee_agency.get_page_source()

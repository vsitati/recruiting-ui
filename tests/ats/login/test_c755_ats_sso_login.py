import pytest
import allure
from ats_pages.login.login import Login
from test_data.test_data_details import SrTestData


@pytest.mark.usefixtures("setup")
class TestAtsSsoLogin:
    @pytest.mark.skip(reason="User not setup in env")
    @allure.title("C755 - ATS SSO Login Tests")
    @allure.description("Login via SSO with a valid user")
    def test_can_login_with_active_sso_user(self, get_test_info):
        username, password = SrTestData.data[get_test_info.get("company")]["users"]["sso"]
        sso_credentials = dict(password=password, username=username)
        login = Login(driver=self.driver)
        login.do_login(get_test_info, cred=sso_credentials, sso=True)
        sso_link, *_ = login.get_all_hrefs()
        login.do_click(sso_link)
        login.switch_tab()

        assert login.is_element_visible(locator=login.quick_search) is True

    @pytest.mark.skip(reason="User not setup in env")
    @allure.description("Scenario Login via SSO with a invalid/non-existing user")
    def test_cannot_login_with_an_invalid_sso_user(self, get_test_info):
        username, password = SrTestData.data[get_test_info.get("company")]["users"]["sso_invalid_username"]
        invalid_credentials = dict(password=password, username=username)
        login = Login(driver=self.driver)
        login.do_login(get_test_info, cred=invalid_credentials, sso=True)

        error_msg = login.get_text(locator=login.sso_login_error)
        assert error_msg == SrTestData.sso_validation.get("sso_invalid_username_error", "")

    @pytest.mark.skip(reason="User not setup in env")
    @allure.description("Scenario Login via SSO with an inactive user with SSO enabled")
    def test_cannot_login_with_an_inactive_sso_user(self, get_test_info):
        username, password = SrTestData.data[get_test_info.get("company")]["users"]["sso_inactive_username"]
        invalid_credentials = dict(password=password, username=username)
        login = Login(driver=self.driver)
        login.do_login(get_test_info, cred=invalid_credentials, sso=True)

        error_msg = login.get_text(locator=login.sso_login_error)
        assert error_msg == SrTestData.sso_validation.get("sso_inactive_user_error", "")

    @pytest.mark.skip(reason="User not setup in env")
    @allure.description("Login via SSO with an active user with SSO disabled")
    def test_cannot_login_with_an_active_sso_disabled_user(self, get_test_info):
        username, password = SrTestData.data[get_test_info.get("company")]["users"]["sso_disabled_active_username"]
        invalid_credentials = dict(password=password, username=username)
        login = Login(driver=self.driver)
        login.do_login(get_test_info, cred=invalid_credentials, sso=True)

        error_msg = login.get_text(locator=login.sso_login_error)
        assert error_msg == SrTestData.sso_validation.get("sso_inactive_user_error", "")

    @pytest.mark.skip(reason="User not setup in env")
    @allure.description("Login via SSO with an inactive user with SSO disabled")
    def test_cannot_login_with_an_inactive_sso_disabled_user(self, get_test_info):
        username, password = SrTestData.data[get_test_info.get("company")]["users"]["sso_disabled_inactive_username"]
        invalid_credentials = dict(password=password, username=username)
        login = Login(driver=self.driver)
        login.do_login(get_test_info, cred=invalid_credentials, sso=True)

        error_msg = login.get_text(locator=login.sso_login_error)
        assert error_msg == SrTestData.sso_validation.get("sso_inactive_and_disabled_error", "")

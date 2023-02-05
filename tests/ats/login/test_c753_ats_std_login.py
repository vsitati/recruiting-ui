import pytest
import allure
from ats_pages.login.login import Login
from test_data.test_data_details import SrTestData


@pytest.mark.regression_grp_d
@pytest.mark.usefixtures("setup")
class TestAtsStandardLogin:
    @allure.title("C753 - ATS Standard Login Tests")
    @allure.description(" Scenario Login with an Active User with valid credentials")
    def test_can_login_with_active_rm_user(self, get_test_info):
        login = Login(driver=self.driver)
        login.do_login(get_test_info)

        assert login.is_element_visible(locator=login.quick_search) is True

    @pytest.mark.smoke
    @allure.description("Scenario Login with an Inactive User with valid credentials")
    def test_cannot_login_with_an_inactive_user(self, get_test_info):
        username, password = SrTestData.data[get_test_info.get("company")]["users"]["inactive"]
        invalid_credentials = dict(password=password, username=username)
        login = Login(driver=self.driver)
        login.do_login(get_test_info, cred=invalid_credentials)

        error_msg = login.get_text(locator=login.login_error)
        assert error_msg == SrTestData.login_validation.get("inactive_login_error", "")

    @pytest.mark.smoke
    @allure.description("Scenario Login with an Active User with an invalid username")
    def test_cannot_login_with_an_invalid_username(self, get_test_info):
        username, password = SrTestData.data[get_test_info.get("company")]["users"]["invalid_username"]
        invalid_credentials = dict(password=password, username=username)
        login = Login(driver=self.driver)
        login.do_login(get_test_info, cred=invalid_credentials)

        error_msg = login.get_text(locator=login.login_error)
        assert error_msg == SrTestData.login_validation.get("invalid_username_password_error", "")

    @allure.description("Scenario Login with an Active User with an invalid password")
    def test_cannot_login_with_an_invalid_password(self, get_test_info):
        username, password = SrTestData.data[get_test_info.get("company")]["users"]["invalid_password"]
        invalid_credentials = dict(password=password, username=username)
        login = Login(driver=self.driver)
        login.do_login(get_test_info, cred=invalid_credentials)

        error_msg = login.get_text(locator=login.login_error)
        assert error_msg == SrTestData.login_validation.get("invalid_username_password_error", "")
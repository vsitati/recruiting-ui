import pytest
import allure
from ats_pages.login import Login
from ats_pages.left_menus import LeftMenus
from test_data.test_data_details import TestData


@pytest.mark.usefixtures("setup")
class TestRecruitingAts:
    @allure.title("ATS Standard Login Tests")
    @allure.description("Can login with an active RM user role")
    def test_can_login_with_active_rm_user(self, get_test_info):
        login = Login(driver=self.driver)
        login.do_login(get_test_info)

        assert login.is_element_visible(locator=login.quick_search) is True

    @allure.description("Cannot login with an invalid username")
    def test_cannot_login_with_an_invalid_username(self, get_test_info):
        invalid_credentials = dict(username="non_existing")
        login = Login(driver=self.driver)
        login.do_login(get_test_info, cred=invalid_credentials)

        error_msg = login.get_text(locator=login.login_error)
        assert error_msg == TestData.login_validation.get("credentials_error", "")

    @allure.description("Cannot login with an invalid password")
    def test_cannot_login_with_an_invalid_password(self, get_test_info):
        invalid_credentials = dict(password="non_existing")
        login = Login(driver=self.driver)
        login.do_login(get_test_info, cred=invalid_credentials)

        error_msg = login.get_text(locator=login.login_error)
        assert error_msg == TestData.login_validation.get("credentials_error", "")

    @allure.description("Cannot login with an inactive user")
    def test_cannot_login_with_an_inactive_user(self, get_test_info):
        username, password = TestData.data[get_test_info.get("company")]["users"]["inactive"]
        invalid_credentials = dict(password=password, username=username)
        login = Login(driver=self.driver)
        login.do_login(get_test_info, cred=invalid_credentials)

        error_msg = login.get_text(locator=login.login_error)
        assert error_msg == TestData.login_validation.get("inactive_login_error", "")


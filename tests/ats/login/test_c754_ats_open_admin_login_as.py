import pytest
import allure
from openadmin_pages.login import Login
from openadmin_pages.user_management import UserManagement
from test_data.test_data_details import SrTestData


@pytest.mark.usefixtures("setup")
class TestOpenAdminLoginAs:
    @allure.title("C754 - ATS Open Admin Login as")
    @allure.description("Scenario Login As a user from Open Admin")
    def test_can_login_as(self, get_test_info):
        get_test_info["ats"] = "openadmin"
        login = Login(driver=self.driver)
        login.do_login(get_test_info)

        assert login.is_element_visible(locator=login.openadmin_banner) is True

        user_management = UserManagement(driver=self.driver)
        user_management.do_loginas(get_test_info)

        user_management.switch_tab()
        assert login.is_element_visible(locator=user_management.quick_search) is True

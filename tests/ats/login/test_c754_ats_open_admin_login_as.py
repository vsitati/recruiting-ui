import pytest
import allure
from openadmin_pages.login import Login
from openadmin_pages.user_management import UserManagement
from test_data.test_data_details import TestingData


@pytest.mark.usefixtures("setup")
class TestOpenAdminLoginAs:
    @allure.title("C754 - ATS Open Admin Login as")
    @allure.description("Scenario Login As a user from Open Admin")
    def test_can_login_as(self, get_test_info):
        login = Login(driver=self.driver)
        login.do_login(get_test_info)

        assert login.is_element_visible(locator=login.openadmin_banner) is True

        loginAs = UserManagement(driver=self.driver)
        loginAs.do_loginas(get_test_info)

        loginAs.switch_tab(self)
        assert login.is_element_visible(locator=loginAs.quick_search) is True
import pytest
import allure
from ats_pages.login import Login


@pytest.mark.usefixtures("setup")
class CandidateResumePage:
    @allure.title("ATS Candidate Resume Page")
    @allure.description("Can View the Candidate Resume Page")
    def test_can_login_with_active_rm_user(self, get_test_info):
        login = Login(driver=self.driver)
        login.do_login(get_test_info)

        assert login.is_element_visible(locator=login.quick_search) is True

    @allure.description("CCE Correspondence")
    def cce_correspondence(self, get_test_info):
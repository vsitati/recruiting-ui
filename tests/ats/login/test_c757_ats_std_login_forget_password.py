import pytest
import allure
from ats_pages.login.login import Login
from ats_pages.login.forget_password import ForgetPassword


@pytest.mark.usefixtures("setup")
class TestAtsStdLoginForgetPassword:
    @allure.title("ATS Standard Login Tests - Forget Password")
    @allure.description("Can open the forget password link")
    def test_can_open_forget_password_link(self, get_test_info):
        login = Login(driver=self.driver)
        ats_url = login.get_env_url(info=get_test_info, app="ats")
        login.open_url(url=ats_url)
        login.click_forget_password()
        fp = ForgetPassword(driver=self.driver)
        assert fp.forget_password_heading() == "Forgot your password?"
        assert fp.verify_instruction_text() is True

    @allure.description("Cannot submit with an empty username on forget password page")
    def test_cannot_submit_with_empty_username_on_forget_password(self, get_test_info):
        login = Login(driver=self.driver)
        ats_url = login.get_env_url(info=get_test_info, app="ats")
        login.open_url(url=ats_url)
        login.click_forget_password()
        fp = ForgetPassword(driver=self.driver)
        fp.click_submit_btn()
        assert fp.verify_empty_field_error_msg() == "This field is required."

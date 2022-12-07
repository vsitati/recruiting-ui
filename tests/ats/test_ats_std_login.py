import pytest
import allure
from ats_pages.login.login import Login
from ats_pages.login.forget_password import ForgetPassword
from ats_pages.login.change_password import ChangePassword
from test_data.test_data_details import SrTestData


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
        assert error_msg == SrTestData.login_validation.get("credentials_error", "")

    @allure.description("Cannot login with an invalid password")
    def test_cannot_login_with_an_invalid_password(self, get_test_info):
        invalid_credentials = dict(password="non_existing")
        login = Login(driver=self.driver)
        login.do_login(get_test_info, cred=invalid_credentials)

        error_msg = login.get_text(locator=login.login_error)
        assert error_msg == SrTestData.login_validation.get("credentials_error", "")

    @allure.description("Cannot login with an inactive user")
    def test_cannot_login_with_an_inactive_user(self, get_test_info):
        username, password = SrTestData.data[get_test_info.get("company")]["users"]["inactive"]
        invalid_credentials = dict(password=password, username=username)
        login = Login(driver=self.driver)
        login.do_login(get_test_info, cred=invalid_credentials)

        error_msg = login.get_text(locator=login.login_error)
        assert error_msg == SrTestData.login_validation.get("inactive_login_error", "")

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

    @allure.description("Can submit a valid username")
    @pytest.mark.dependency()
    def test_can_submit_a_valid_username(self, get_test_info):
        user, *_ = SrTestData.data[get_test_info.get("company")]["users"]["for_password_change"]
        login = Login(driver=self.driver)
        ats_url = login.get_env_url(info=get_test_info, app="ats")
        login.open_url(url=ats_url)
        login.click_forget_password()
        fp = ForgetPassword(driver=self.driver)
        fp.enter_text(locator=fp.username, text=user)
        fp.click_submit_btn()
        assert fp.verify_account_verification_text() is True
        body, attachments = fp.read_mailbox(subject_search_text="Reset Your Password")
        assert body != ''
        assert "change_me" in body
        assert "Username: change_me" in body
        assert "IP Address" in body
        assert attachments == []

    @allure.description("Cannot submit with an empty new password field")
    def test_cannot_submit_empty_new_password_fields(self):
        cp = ChangePassword(driver=self.driver)
        body, *_ = cp.read_mailbox(subject_search_text="Reset Your Password")
        assert body != ''
        reset_password_url = cp.extract_url(body_content=body)
        cp.open_url(url=reset_password_url)
        cp.click_submit_btn()
        assert cp.verify_empty_field_error_msg() == "This field is required."

    @allure.description("Cannot submit with mismatched passwords")
    def test_cannot_submit_mismatched_passwords(self):
        cp = ChangePassword(driver=self.driver)
        body, *_ = cp.read_mailbox(subject_search_text="Reset Your Password")
        assert body != ''
        reset_password_url = cp.extract_url(body_content=body)
        cp.open_url(url=reset_password_url)
        cp.do_change_password(new_password="silkroad2022", confirm_password="silkroad2")
        assert cp.get_mismatched_text() == "Your passwords do not match."

    @allure.description("Cannot submit where the password characters length are less than 8")
    def test_cannot_submit_passwords_with_length_less_than_eight_characters(self):
        cp = ChangePassword(driver=self.driver)
        body, *_ = cp.read_mailbox(subject_search_text="Reset Your Password")
        assert body != ''
        reset_password_url = cp.extract_url(body_content=body)
        cp.open_url(url=reset_password_url)
        cp.do_change_password(new_password="silk", confirm_password="sil")
        assert cp.verify_empty_field_error_msg() == "Please enter at least 8 characters."

    @allure.description("Can submit new password")
    @pytest.mark.dependency(depends=["TestRecruitingAts::test_can_submit_a_valid_username"])
    def test_can_submit_new_passwords(self):
        cp = ChangePassword(driver=self.driver)
        body, *_ = cp.read_mailbox(subject_search_text="Reset Your Password")
        assert body != ''
        reset_password_url = cp.extract_url(body_content=body)
        cp.open_url(url=reset_password_url)
        # TODO Must add a random name generator
        cp.do_change_password(new_password="Silkroad2022", confirm_password="silkroad2022")
        assert cp.get_password_change_success_msg() == SrTestData.change_password_success_msg
        body, attachments = cp.read_mailbox(subject_search_text="SilkRoad Recruiting password changed successfully")
        assert body != ''
        assert "change_me" in body
        assert SrTestData.changed_password_success_email_body_text.format(user="change_me") in body
        assert attachments == []

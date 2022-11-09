import allure
from cx_pages.base import BasePage
from selenium.webdriver.common.by import By
import pytest


class Elements:
    applicationurl = "{domain}"


class QuickApply(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def test_main(self):
        useridentifier = self.find_element(By.CSS_SELECTOR, "#SuperAdmin_AdminLogin_EmailAddress")
        useridentifier.send_keys("vsitati")

        #  Click 'Password' and input password
        password = self.find_element(By.CSS_SELECTOR, "#SuperAdmin_AdminLogin_Password")
        password.click()

        password = self.find_element(By.CSS_SELECTOR, "#SuperAdmin_AdminLogin_Password")
        password.send_keys("@w3b4dm25N")

        # Click 'SuperAdmin_AdminLogin_SubmitButton'
        superadmin_adminlogin_submitbutton = self.find_element(By.CSS_SELECTOR, "#SuperAdmin_AdminLogin_SubmitButton")
        superadmin_adminlogin_submitbutton.click()

        # Click 'Lucee QA 01'
        lucee_qa_01 = self.find_element(By.CSS_SELECTOR, "#SuperAdmin_CustomerLogin-luceeqa01")
        lucee_qa_01.click()

        # Click 'qa_visibility'
        qa_visibility = self.find_element(By.XPATH, "/html/body/article/section[2]/div/div[4]/a[1]/div/i")
        qa_visibility.click()

        # Click 'Click_Senior Accountant'
        click_senior_accountant = self.find_element(By.XPATH, "/html/body/div[3]/section[2]/article[1]/a/div[1]")
        click_senior_accountant.click()

        # Click 'click_apply'
        click_apply = self.find_element(By.XPATH, "/html/body/div[3]/section[4]/div/a")
        click_apply.click()

        # Click 'FirstName'
        firstname = self.find_element(By.XPATH, "/html/body/div[3]/section[3]/div/form/div[3]/div[1]/input")
        firstname.click()

        # Type 'John' in 'FirstName'
        firstname = self.find_element(By.XPATH, "/html/body/div[3]/section[3]/div/form/div[3]/div[1]/input")
        firstname.send_keys("John")

        # Click 'LastName'
        lastname = self.find_element(By.XPATH, "/html/body/div[3]/section[3]/div/form/div[3]/div[2]/input")
        lastname.click()

        # Type 'Doe' in 'LastName'
        lastname = self.find_element(By.XPATH, "/html/body/div[3]/section[3]/div/form/div[3]/div[2]/input")
        lastname.send_keys("Doe")

        # Click 'Email'
        email = self.find_element(By.CSS_SELECTOR, "#Apply_ApplyToJob_Email")
        email.click()

        # Type 'johndoe@doe.com' in 'Email'
        email = self.find_element(By.CSS_SELECTOR, "#Apply_ApplyToJob_Email")
        email.send_keys("johndoe@doe.com")

        # Click 'Click_resume_upload'
        click_resume_upload = self.find_element(By.CSS_SELECTOR, "#Apply_ApplyToJob_File")
        click_resume_upload.click()

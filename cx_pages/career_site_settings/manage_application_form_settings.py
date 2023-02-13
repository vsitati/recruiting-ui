import random
import string

import allure
from selenium.webdriver.common.by import By

from common.common import Common
from config import Config
from helpers.utils import get_resumes


class Elements:
    quick_apply_radio_btn = (By.ID, "Admin_ApplicationForms__CustomApplyFormFalse")
    custom_apply_radio_btn = (By.ID, "Admin_ApplicationForms__CustomApplyFormTrue")
    application_form_save_btn = (By.ID, "Admin_ApplicationForms__SaveButton")
    configured_application_forms_parent = (By.CSS_SELECTOR, ".sr-panel.sr-panel--with-meta-and-button-set")
    configured_application_forms_functions = (By.CSS_SELECTOR, ".sr-panel__meta.sr-panel__button-set")
    function_btn = (By.CSS_SELECTOR, ".material-icons.sr-button__icon")
    publish_modal_btn = (By.ID, "Admin_JobBoards_ApplicationForms_Modal_Primary_Button")
    cancel_modal_btn = (By.ID, "Admin_JobBoards_ApplicationForms_Modal_Cancel_Link")
    publish_form = (By.CSS_SELECTOR, "a[title='Publish application form']")
    edit_form = (By.CSS_SELECTOR, "a[title='Edit application form']")
    clone_form = (By.CSS_SELECTOR, "a[title='Clone application form']")
    delete_form = (By.CSS_SELECTOR, "a[title='Delete application form']")
    view_form = (By.CSS_SELECTOR, "a[title='View application form']")
    apply_success_heading = (By.ID, "Apply_Success_JobsLink")
    firstname = (By.ID, 'FirstName')
    firstname_label = (By.XPATH, "//label[@for='Apply_ApplyToJob_FirstName']")
    lastname = (By.ID, 'LastName')
    lastname_label = (By.XPATH, "//label[@for='Apply_ApplyToJob_LastName']")
    email = (By.ID, 'EmailAddress')
    email_label = (By.XPATH, "//label[@for='Apply_ApplyToJob_Email']")
    apply_btn = (By.ID, 'Apply_ApplyToJob_SubmitButton')
    choose_file_btn = (By.ID, 'Apply_ApplyToJob_File')
    name_prefix = (By.ID, "NamePrefix")
    suffix_name = (By.ID, "NameSuffix")
    secondary_phone_number = (By.ID, "SecondaryPhoneNumber")
    country_code = (By.ID, "CountryCode")
    address_line_two = (By.ID, "AddressLine2")
    middle_name = (By.ID, "MiddleName")
    file_path = (By.ID, "File")
    submit_button_final = (By.ID, "MultiForm_Apply_FinishButton")


class ManageApplicationFormSettings(Elements, Common):
    def __init__(self, driver):
        super().__init__(driver)

    @staticmethod
    def is_checked(element):
        if not element.get_attribute("checked") == "checked":
            return False
        else:
            return True

    def enable_application_form_type(self, enable_quick_apply=False):
        if enable_quick_apply:
            elem = self.driver.find_element_by_locator(self.quick_apply_radio_btn)
            if not self.is_checked(element=elem):
                self.do_click(elem)
        else:
            elem = self.driver.find_element_by_locator(self.custom_apply_radio_btn)
            if not self.is_checked(element=elem):
                self.do_click(elem)

        save_btn_elem = self.driver.find_element_by_locator(self.application_form_save_btn)
        self.driver.execute_script("arguments[0].scrollIntoView();", save_btn_elem)
        return self.do_click(save_btn_elem)

    def configure_application_form(self, form_name, function, view=False):
        form_name_index = ""
        all_forms_elems = self.driver.find_elements_by_locator(self.configured_application_forms_parent)
        for index, all_forms_elem in enumerate(all_forms_elems):
            if form_name in all_forms_elem.text:
                form_name_index = index
                break

        if form_name_index:
            all_forms_elem = all_forms_elems[form_name_index]
            if not view:
                function_btn_elems = all_forms_elem.find_elements(*self.function_btn)
                if function == "publish":
                    function = "publish_form"

                for function_btn_elem in function_btn_elems:
                    if function in function_btn_elem.text:
                        self.driver.execute_script("arguments[0].scrollIntoView();", function_btn_elem)
                        self.do_click(function_btn_elem)
                        return form_name
                return "Available functions for configuring forms: publish, edit, clone and delete."

            function_btn_elems = all_forms_elem.find_elements(*self.function_btn)
            for function_btn_elem in function_btn_elems:
                print(function_btn_elem.text)
                if function in function_btn_elem.text:
                    self.driver.execute_script("arguments[0].scrollIntoView();", function_btn_elem)
                    self.do_click(function_btn_elem)
                    return form_name
                return "Available functions for View application form: visibility.\n" \
                       f"or the form name \'{form_name}\' is an unpublished name.\n" \
                       "Only published form names can be used"

        return f"Form name {form_name} not found."

    @allure.step('Fill in Configured Apply Form')
    def fill_apply_form_data(self, firstname, lastname, email, file_path, secondary_phone_number, suffix_name,
                             middle_name, address_line_two):
        firstname_field = self.driver.find_element_by_locator(self.firstname)
        firstname_field.send_keys(firstname)

        lastname_field = self.driver.find_element_by_locator(self.lastname)
        lastname_field.send_keys(lastname)

        email_field = self.driver.find_element_by_locator(self.email)
        email_field.send_keys(email)

        file_path_field = self.driver.find_element_by_locator(self.file_path)
        file_path = get_resumes(parent_folder=Config.env_config["path_to_resumes"])
        file_path_field.send_keys(file_path)

        secondary_phone_number_field = self.driver.find_element_by_locator(self.secondary_phone_number)
        secondary_phone_number_field.send_keys(secondary_phone_number)

        suffix_name_field = self.driver.find_element_by_locator(self.suffix_name)
        suffix_name_field.send_keys(suffix_name)

        middle_name_field = self.driver.find_element_by_locator(self.middle_name)
        middle_name_field.send_keys(middle_name)

        address_line_two_field = self.driver.find_element_by_locator(self.address_line_two)
        address_line_two_field.send_keys(address_line_two)

    def click_cx_multi_job_apply_btn(self):
        element = self.driver.find_element_by_locator(self.multi_form_apply_button)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        return self.do_click(element)

    def final_job_apply_btn(self):
        element = self.driver.find_element_by_locator(self.submit_button_final)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        return self.do_click(element)

    def random_phone_generator(self):
        ph_no = [str(random.randint(6, 9))]
        for i in range(1, 10):
            ph_no.append(str(random.randint(0, 9)))

        return "".join(ph_no)

    def random_name_generator(self):
        alphabet = string.ascii_letters
        first_name_length = random.randint(3, 10)
        last_name_length = random.randint(3, 10)

        first_name = "".join(random.choice(alphabet) for i in range(first_name_length))
        last_name = "".join(random.choice(alphabet) for i in range(last_name_length))

        return first_name, last_name

    def get_success_message(self):
        return self.driver.find_element_by_locator(self.apply_success_heading).text

    def random_email_generator(self):
        alphabet = string.ascii_lowercase
        email_length = random.randint(6, 20)
        domain_length = random.randint(5, 10)

        email = "".join(random.choice(alphabet) for i in range(email_length))
        domain = "".join(random.choice(alphabet) for i in range(domain_length))

        return f"{email}@{domain}.com"


class ConfiguredApplyForm(Elements, Common):
    def __init__(self, driver):
        super().__init__(driver)

    def get_configured_apply_form_data(self, parent_folder, specify_resume="", file_ext=""):
        resume = get_resumes(parent_folder=parent_folder, specify_resume=specify_resume, file_ext=file_ext)
        self.get_configured_apply_form_data["file_path"] = resume
        return self.get_configured_apply_form_data

    def get_success_message(self):
        return self.driver.find_element_by_locator(self.apply_success_heading).text

    def select_drop_down_configured_apply(self):
        self.driver.find_element_by_locator(self.name_prefix).click()
        available_items = self.driver.find_elements_by_locator(self.name_prefix)
        for x in available_items:
            if x.text == "Mr.":
                x.click()
            break

    def select_drop_down_country_residence(self):
        self.driver.find_element_by_locator(self.name_prefix).click()
        available_items = self.driver.find_elements_by_locator(self.country_code)
        for x in available_items:
            if x.text == "United States":
                x.click()
            break

    def click_cx_multi_job_apply_btn(self):
        element = self.driver.find_element_by_locator(self.multi_form_apply_button)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        return self.do_click(element)

import random
import secrets
import string
from time import sleep

import allure
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from common.common import Common


class ElementsConfiguredApply:
    custom_apply_form = (By.ID, "Admin_ApplicationForms__CustomApplyFormTrue")
    Admin_ApplicationForms_SaveButton = (By.ID, "Admin_ApplicationForms__SaveButton")
    Admin_ApplicationForm_Name = (By.ID, "Admin_ApplicationForm__Name")
    Admin_Application_Form_Description = (By.ID, "Admin_ApplicationForm__Description")
    icon_add_options = (
        By.XPATH, "//a[@data-action='addField']/i[contains(@class, 'material-icons sr-button__icon') and text()='add']")
    fields = (By.CLASS_NAME, "material-icons sr-button__icon")
    page_title = (By.ID, "page_1")
    first_name_configured_apply = (By.ID, "application_field_FirstName")
    last_name_configured_apply = (By.ID, "application_field_LastName")
    email_id_configured_apply = (By.ID, "application_field_EmailAddress")
    application_form_modal = (By.ID, "Admin_ApplicationForm_Modal__ApplicationField")
    modal_primary_button = (By.ID, "Admin_ApplicationForm_Modal__Modal_Primary_Button")
    save_button_modal = (By.ID, "Admin_ApplicationForm__SaveButton")
    cancel_button_modal = (By.ID, "Admin_ApplicationForm_Modal__Modal_Outside_Cancel_Link")
    configure_field_parent = (By.CSS_SELECTOR, ".sr-modal__container")
    page_title_extract = (By.CSS_SELECTOR, ".sr-panel__title")
    page_name_configured_apply = (By.ID, "Admin_ApplicationForm__Name")
    container = (By.CSS_SELECTOR, ".sr-panel.sr-panel--with-meta-and-button-set")
    publish_form_button = (By.ID, "Admin_JobBoards_ApplicationForms_Modal_Primary_Button")
    publish_button = (By.ID, "Admin_JobBoards_ApplicationForms_Modal_Primary_Button")


class CommonConfiguredApply(ElementsConfiguredApply, Common):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.headers = {"Content-Type": "application/json"}
        self.regex = 'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*(),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'

    def extract_data(self):
        div = self.driver.find_element_by_locator(self.page_title_extract)
        data = div.text
        return data

    def custom_apply_form_switch(self):
        radio_button = self.driver.find_element_by_locator(self.custom_apply_form)
        if not radio_button.is_selected():
            # If not selected, click the radio button to select it
            radio_button.click()

    def container_function(self):
        publisher = self.driver.find_element(By.CSS_SELECTOR, "a[title='Publish application form']")
        self.driver.execute_script("arguments[0].scrollIntoView();", publisher)
        publisher.click()
        #sleep(2.0)
        sleep(1.0)
        try:
            publisher = self.driver.find_element_by_locator(By.CSS_SELECTOR, "a[title='Publish application form']")
            self.driver.execute_script("arguments[0].scrollIntoView(true);", publisher)
            sleep(1.0)
            publisher.click()
            sleep(2.0)
        except Exception as e:
            print("publish button not found", e)
        sleep(1.0)
        try:
            publisher = self.driver.find_element_by_locator(By.CSS_SELECTOR, "a[title='Publish application form']")
            self.driver.execute_script("arguments[0].scrollIntoView(true);", publisher)
            sleep(1.0)
            publisher.click()
            sleep(2.0)
        except Exception as e:
            print("publish button not found", e)

    @staticmethod
    def generate_string(page_name):
        letters = string.ascii_letters
        page_name = ''.join(random.choice(letters) for i in range(len(page_name)))
        return page_name

    def application_forms_save_button(self):
        elem = self.driver.find_element_by_locator(self.Admin_ApplicationForms_SaveButton)
        self.driver.execute_script("arguments[0].scrollIntoView();", elem)
        elem.click()

    def click_add_options_button(self):
        elem = self.driver.find_element_by_locator(self.icon_add_options)
        self.driver.execute_script("arguments[0].scrollIntoView();", elem)
        elem.click()

    def click_opt_group(self):
        elem = self.driver.find_element_by_locator(self.application_form_modal)
        self.driver.execute_script("arguments[0].scrollIntoView();", elem)
        elem.click()

    def click_save_button_modal(self):
        button = self.driver.find_element_by_locator(self.modal_primary_button)
        self.driver.execute_script("arguments[0].scrollIntoView();", button)
        button.click()

    def page_title_fill(self):
        page_title_fill = self.driver.find_element_by_locator(self.page_title)
        page_title_fill.send_keys()

    def names_pages(self):
        page_name = self.generate_string("abcdefghijkLMNOPQRSTUVWXYZ")
        page_name_element = self.driver.find_element_by_locator(self.page_name_configured_apply)
        page_name_element.send_keys(page_name)

    def save_page(self):
        sleep(0.5)
        try:
            button = self.driver.wait_for_element_to_be_clickable(self.save_button_modal)
            self.driver.execute_script("arguments[0].scrollIntoView(true);", button)
            button.click()
            sleep(2.0)
            input("we have saved the page")
        except Exception as e:
            print("Error occurred while clicking the button: ", e)

    def publish_button_click(self):
        try:
            button = self.driver.wait_for_element_to_be_clickable(self.publish_button)
            self.driver.execute_script("arguments[0].scrollIntoView(true);", button)
            button.click()
        except Exception as e:
            print("Error occurred while clicking the button: ", e)

    @allure.step("Add all options External configured apply")
    def opt_group_select(self):
        parent_modal_elem = self.driver.find_element_by_locator(self.configure_field_parent)
        select_element = parent_modal_elem.find_element(*self.application_form_modal)
        select = Select(select_element)

        len_options = len(select.options)
        for index in range(len_options):
            if index == len_options - 1:
                return True
            self.driver.find_element_by_locator(self.configure_field_parent)
            try:
                select.select_by_index(index)
            except NoSuchElementException:
                pass
            primary_btn = self.driver.wait_for_element_to_be_clickable(self.modal_primary_button)
            sleep(0.2)
            self.driver.execute_script("arguments[0].scrollIntoView();", primary_btn)
            parent_modal_elem.find_element(*self.modal_primary_button).click()
            self.driver.wait_for_element_to_be_clickable(self.icon_add_options)
            sleep(0.1)
            self.click_add_options_button()
            sleep(0.1)
        return False

    def options_to(self):
        parent_modal_elem = self.driver.find_element_by_locator(self.configure_field_parent)
        select_element = parent_modal_elem.find_element(*self.application_form_modal)
        select = Select(select_element)

        for index in range(5):
            try:
                select.select_by_index(index)
            except NoSuchElementException:
                pass
            primary_btn = self.driver.wait_for_element_to_be_clickable(self.modal_primary_button)
            sleep(0.2)
            self.driver.execute_script("arguments[0].scrollIntoView();", primary_btn)
            parent_modal_elem.find_element(*self.modal_primary_button).click()
            self.driver.wait_for_element_to_be_clickable(self.icon_add_options)
            sleep(0.5)
            self.click_add_options_button()
            sleep(1.0)
        return False

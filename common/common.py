import base64
import os
import re
from time import sleep

import allure
from config import Config
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
from selenium.webdriver.common.by import By
import requests
from bs4 import BeautifulSoup
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.window import WindowTypes
from selenium.webdriver.support.ui import Select

from config import Config
from helpers.webdriver_listener import WebDriverListener


class Elements:
    quick_search = (By.ID, 'quick_search_input')
    empty_field_validation_msg = (By.XPATH, ".//span[@class = 'help-block']")
    submit_btn = (By.ID, "submitButton")
    richtext = (By.ID, 'tinymce')
    auto_complete = (By.CSS_SELECTOR, "[role='listbox'] [class='ui-corner-all']")
    datepicker = (By.CSS_SELECTOR, "[id='ui-datepicker-div'] [class^='ui-datepicker-close']")
    openadmin_banner = (By.CLASS_NAME, 'ui-layout-banner')
    cx_apply_btn = (By.ID, "Base_BackToJobs_ApplyLink")
    cx_multiform_apply_btn = (By.ID, "Base_BackToJobs_Multiform_ApplyLink")
    multi_form_apply_button = (By.ID, "Base_BackToJobs_Multiform_ApplyLink")
    all_hrefs = (By.XPATH, "//a[@href]")
    cx_settings_back_btn = (By.ID, "Admin_BackLink")
    cx_view_other_job_openings = (By.ID, "Apply_Success_JobsLink")
    custom_apply_form = (By.ID, "Admin_ApplicationForms__CustomApplyFormTrue")
    Admin_ApplicationForms_SaveButton = (By.ID, "Admin_ApplicationForms__SaveButton")
    Admin_ApplicationForm_Name = (By.ID, "Admin_ApplicationForm__Name")
    Admin_Application_Form_Description = (By.ID, "Admin_ApplicationForm__Description")
    icon_add_options = (By.XPATH, "//a[@data-action='addField']/i[contains(@class, 'material-icons sr-button__icon') and text()='add']")
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


class Common(Elements):
    """ In the common class we define all common functionality """

    def __init__(self, driver):
        self.driver = driver
        self.headers = {"Content-Type": "application/json"}
        self.regex = 'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*(),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'

    sr_logger = WebDriverListener()
    sleep_time = 1

    @staticmethod
    def parse_email_body(body):
        parsed_result = BeautifulSoup(body, "html.parser")
        text = parsed_result.get_text()
        return [x.strip() for x in text.split('\n') if x.strip()]

    @staticmethod
    def get_request(url, headers):
        # TODO Add try except to catch non json responses:  r.json()
        try:
            r = requests.get(url, headers=headers)
            return r.json()
        except requests.exceptions.ConnectionError:
            raise requests.exceptions.ConnectionError("Connection error to the Utility app. Check network or VPN")

    @staticmethod
    def get_mailbox_url():
        config = Config.env_config["env"]["utility"]
        env = config.get("env", "")
        protocol = config['url']['protocol']
        domain = config['url']['domain']
        path = config['endpoints']['mailbox']

        return f"{protocol}://{env}{domain}/{path}"

    @allure.step("Reading Utility Mailbox")
    def read_mailbox(self, subject_search_text="", sent_to="", timeout=2, email_index=0):
        # TODO Search by Sent_to
        increment = 0.5
        emails = []
        total_time = timeout / increment

        for i in range(int(total_time)):
            response = self.get_request(url=self.get_mailbox_url(), headers=self.headers)

            if subject_search_text and not sent_to:
                emails = [x for x in response if
                          subject_search_text in x["headers"]["Subject"].strip().replace("\r", "").replace("\n", "")]
            if sent_to and not subject_search_text:
                emails = [x for x in response if x["headers"]["To"] == sent_to]

            if subject_search_text and sent_to:
                emails = [x for x in response if
                          subject_search_text in x["headers"]["Subject"].strip().replace("\r", "").replace("\n", "")
                          and x["headers"]["To"] == sent_to]

            if emails:
                view_link = emails[email_index].get("viewLink", "")
                view_link_response = self.get_request(url=view_link, headers=self.headers)
                email_body = view_link_response.get("body", "")
                body_content = self.parse_email_body(body=email_body)
                return ' '.join(body_content), view_link_response.get("attachments", [])
            sleep(increment)
        return "", []

    @staticmethod
    def encoding_file(file_name):
        with open(file_name, 'rb') as binary_file:
            binary_file_data = binary_file.read()
            base64_encoded_data = base64.b64encode(binary_file_data)
            return base64_encoded_data.decode('utf-8')

    def compare_email_attachment(self, attachments, file_name):
        base_name = os.path.basename(file_name)
        for attachment in attachments:
            if base_name == attachment.get("fileName", ""):
                return attachment.get("content", "") == self.encoding_file(file_name=file_name)
        return False

    def extract_url(self, body_content):
        try:
            url, *_ = re.findall(self.regex, body_content)
            return url
        except ValueError:
            return ""

    @allure.step("Opening main page")
    def open_url(self, url):
        """
        Opens any valid URL
        :param url: The url you navigating too
        :return: Updated driver version
        """
        return self.driver.open(url=url)

    def select_from_dropdown(self, locator, text):
        """
        Select any given option from select type dropdown list
        :param locator: Locator element
        :param text: option from the dropdown
        """
        select = Select(self.driver.find_element_by_locator(locator))
        select.select_by_visible_text(text)

    def verify_dropdown_selection(self, locator, text):
        select = Select(self.driver.find_element_by_locator(locator))
        if select.first_selected_option.text == text:
            return True
        else:
            return False

    def select_multiselect_list(self, locator, text):
        elm = self.driver.find_element_by_locator(locator)
        my_select = Select(elm)
        for my_text in text:
            my_select.select_by_visible_text(my_text)

    @staticmethod
    def do_click(element):
        """
        Perform a click on a given element.
        :param element: The element to be clicked on.
        """
        try:
            return element.click()
        except StaleElementReferenceException:
            pass

    def go_click(self, locator):
        try:
            return self.driver.find_element_by_locator(locator).click()
        except StaleElementReferenceException:
            pass

    def get_title(self):
        return self.driver.title

    @staticmethod
    def get_env_url(info, app):
        endpoint = info.get(app)
        company = info.get("company")
        config = Config.env_config.get("env", {})
        protocol = config[app]['url']['protocol']
        domain = config[app]['url']['domain']
        path = config[app]['endpoints'][endpoint]

        if app == "cx":
            return f"{protocol}://{domain}/{company}{path}"
        else:
            return f"{protocol}://{company}{domain}{path}"

    # By Jason: NOT always correct, please use is_element_displayed
    def is_element_visible(self, locator):
        try:
            return self.driver.find_element_by_locator(locator) and True
        except Exception as e:  # TODO Need to add proper exception
            return False

    def is_element_displayed(self, locator):
        is_display = self.driver.find_element_by_locator(locator).is_displayed()
        if is_display:
            return True
        else:
            return False

    def get_text(self, locator):
        try:
            return self.driver.find_element_by_locator(locator).text
        except Exception as e:  # TODO Need to add proper exception
            return "Text not found"

    def verify_empty_field_error_msg(self):
        return self.driver.find_element_by_locator(self.empty_field_validation_msg).text

    # TODO: could just use do_click
    def click_submit_btn(self):
        self.do_click(self.driver.find_element_by_locator(self.submit_btn))

    def enter_text(self, locator, text):
        elm = self.driver.find_element_by_locator(locator)
        elm.clear()
        return elm.send_keys(text)

    def enter_richtext(self, locator, text):
        by, by_value = locator
        self.driver.switch_to.frame(by_value)
        elm = self.driver.find_element_by_locator(self.richtext)
        elm.clear()
        elm.send_keys(text)
        self.driver.switch_to.default_content()

    def enter_richtext_integer(self, locator, text):
        elm = self.driver.find_element_by_locator(locator)
        elm.send_keys(Keys.CONTROL + "a")
        elm.send_keys(Keys.DELETE)
        return elm.send_keys(text)

    # isCheck: True: Check; False: UnCheck
    def check_checkbox(self, locator, is_check):
        elm = self.driver.find_element_by_locator(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", elm)
        if elm.is_selected() != is_check:
            return self.do_click(elm)
        return

    # isCheck: True: Check; False: UnCheck
    def check_checkbox_custom(self, locator, is_check):
        boolean_dict = dict(
            true=True,
            false=False
        )

        elm = self.driver.find_element_by_locator(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", elm)
        checked = boolean_dict.get(elm.get_attribute("aria-checked"))
        if checked != is_check:
            return self.do_click(elm)
        return

    def click_radio_yes_no(self, yes_btn_elem, no_btn_elem, yes=False):
        yes_btn = self.driver.find_element_by_locator(yes_btn_elem)
        no_btn = self.driver.find_element_by_locator(no_btn_elem)

        if yes:
            if not yes_btn.get_attribute("checked") == "checked":  # If checked, then do nothing
                self.do_click(yes_btn)
        elif not yes:
            if not no_btn.get_attribute("checked") == "checked":  # If checked, then do nothing
                self.do_click(no_btn)

    def click_radio_list(self, locator, text):
        elms = self.driver.find_elements_by_locator(locator)
        for elm in elms:
            if text in elm.accessible_name:
                return self.do_click(elm)
        return

    def select_auto_complete(self, locator, text):
        elm = self.driver.find_element_by_locator(locator)
        elm.clear()
        # elm.send_keys(text)
        # sleep(self.sleep_time)  # TODO: find a better way to wait
        self.slow_typing(element=elm, text=text)
        elms = self.driver.find_elements_by_locator(self.auto_complete)
        for elm in elms:
            if text in elm.text:
                return self.do_click(elm)
        return

    def pick_datepicker(self, locator, text):
        self.enter_text(locator, text)
        sleep(self.sleep_time)
        return self.go_click(self.datepicker)

    def switch_tab(self, index=1):
        self.driver.switch_to.window(self.driver.window_handles[index])

    def new_tab(self):
        self.driver.switch_to.new_window(WindowTypes.TAB)

    def close_tab(self):
        self.driver.close()

    def get_all_hrefs(self, specific_href="", link_text=""):
        href_elms = self.driver.find_elements_by_locator(self.all_hrefs)
        if specific_href:
            for href_elm in href_elms:
                if specific_href in href_elm.get_attribute("href"):
                    return href_elm.get_attribute("href")
            return ""
        if link_text:
            for href_elm in href_elms:
                if href_elm.text == link_text:
                    return href_elm.get_attribute("href")
            return ""
        return href_elms

    def get_h2_tag_name(self):
        return self.driver.find_element_by_tag_name("h2").text

    def click_cx_job_apply_btn(self):
        return self.do_click(self.driver.find_element_by_locator(self.cx_apply_btn))


    def click_cx_settings_back_btn(self):
        elem = self.driver.find_element_by_locator(self.cx_settings_back_btn)
        self.driver.execute_script("arguments[0].scrollIntoView();", elem)
        return self.do_click(elem)

    def click_view_other_job_openings(self):
        return self.do_click(self.driver.find_element_by_locator(self.cx_view_other_job_openings))

    def get_page_source(self):
        return self.driver.page_source

    def quick_search(self, search_object, search_input=""):
        elm = self.driver.find_element_by_locator(self.quick_search_btn)
        if elm.text.lower() != search_object.lower():
            self.do_click(elm)

    def click_save_button_modal(self):
        button = self.driver.find_element_by_locator(self.modal_primary_button)
        self.driver.execute_script("arguments[0].scrollIntoView();", button)
        return self.do_click(button)

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

    def slow_typing(self, element, text):
        pass

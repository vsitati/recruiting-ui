import allure
from config import Config
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
import requests
from bs4 import BeautifulSoup
import re
from time import sleep
from selenium.webdriver import Keys


class Elements:
    quick_search = (By.ID, 'quick_search_input')
    empty_field_validation_msg = (By.XPATH, ".//span[@class = 'help-block']")
    submit_btn = (By.ID, "submitButton")
    richtext = (By.ID, 'tinymce')
    auto_complete = (By.CSS_SELECTOR, "[role='listbox'] [class='ui-corner-all']")
    datepicker = (By.CSS_SELECTOR, "[id='ui-datepicker-div'] [class^='ui-datepicker-close']")


class Common(Elements):
    """ In the common class we define all common functionality """
    def __init__(self, driver):
        self.driver = driver
        self.headers = {"Content-Type": "application/json"}
        self.regex = 'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*(),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'

    @staticmethod
    def parse_email_body(inbox):
        if inbox:
            first_result, *_ = inbox
            parsed_result = BeautifulSoup(first_result, "html.parser")

            if parsed_result.find_all('html'):
                html = parsed_result.find_all('html')
            else:
                html = parsed_result.find_all('pre')

            data, *_ = html
            text = data.get_text()
            # TODO Need to see if I can improve HTML text output
            return [x.strip() for x in text.split('\n') if x.strip()]
        return []  # if no results are found

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
    def read_mailbox(self, subject_search_text, timeout=2):
        increment = 0.5
        total_time = timeout / increment
        for i in range(int(total_time)):
            response = self.get_request(url=self.get_mailbox_url(), headers=self.headers)

            inbox = [x["body"] for x in response if
                     subject_search_text in x["headers"]["Subject"].strip().replace("\r", "").replace("\n", "")]
            if inbox:
                body_content = self.parse_email_body(inbox=inbox)
                return ' '.join(body_content)
            sleep(increment)
        return ""

    def extract_url(self, body_content):
        try:
            url, *_ = re.findall(self.regex, body_content)
            return url
        except ValueError:
            return ""

    @allure.step("Opening main page")
    def open(self, url):
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

    def is_element_visible(self, locator):
        try:
            return self.driver.find_element_by_locator(locator) and True
        except Exception as e:  # TODO Need to add proper exception
            return False

    def get_text(self, locator):
        try:
            return self.driver.find_element_by_locator(locator).text
        except Exception as e:  # TODO Need to add proper exception
            return "Text not found"

    def verify_empty_field_error_msg(self):
        return self.driver.find_element_by_locator(self.empty_field_validation_msg).text

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
    def click_checkbox(self, locator, isCheck):
        elm = self.driver.find_element_by_locator(locator)
        if elm.is_selected() != isCheck:
            self.do_click(elm)

    # isYes: True: Yes; False: No
    def click_radio(self, locator, isYes):
        if isYes:
            locator[1] = locator[1] + "1"
        else:
            locator[1] = locator[1] + "0"
        return self.go_click(locator)

    def click_auto_complete(self, locator, text):
        elm = self.driver.find_element_by_locator(locator)
        elm.clear()
        elm.send_keys(text)
        sleep(0.5)
        elms = self.driver.find_elements_by_locator(self.auto_complete)
        for elm in elms:
            if text in elm.text:
                self.do_click(elm)
                break

    def pick_datepicker(self, locator, text):
        self.enter_text(locator, text)
        sleep(0.5)
        return self.go_click(self.datepicker)

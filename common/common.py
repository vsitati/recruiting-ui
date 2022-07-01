import allure
from config import Config
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
import requests
from bs4 import BeautifulSoup
import re


class Elements:
    quick_search = (By.ID, 'quick_search_input')


class Common(Elements):
    """ In the common class we define all common functionality """
    def __init__(self, driver):
        self.driver = driver
        self.headers = {"Content-Type": "application/json"}
        self.regex = 'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'

    @staticmethod
    def parse_email_body(inbox):
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

    @staticmethod
    def get_request(url, headers):
        # TODO Add try except to catch auth or connection errors
        r = requests.get(url, headers=headers)
        return r.json()

    @staticmethod
    def get_mailbox_url():
        config = Config.env_config["env"]["utility"]
        env = config.get("env", "")
        protocol = config['url']['protocol']
        domain = config['url']['domain']
        path = config['endpoints']['mailbox']

        return f"{protocol}://{env}{domain}/{path}"

    @allure.step("Reading Utility Mailbox")
    def read_mailbox(self, subject_search_text):
        response = self.get_request(url=self.get_mailbox_url(), headers=self.headers)

        inbox = [x["body"] for x in response if
                 subject_search_text in x["headers"]["Subject"].strip().replace("\r", "").replace("\n", "")]
        body_content = self.parse_email_body(inbox=inbox)
        return ' '.join(body_content)

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
        except Exception as e:
            return False

    def get_text(self, locator):
        try:
            return self.driver.find_element_by_locator(locator).text
        except Exception as e:
            return "Text not found"

    def enter_text(self, element, text):
        return self.driver.find_element_by_locator(element).send_keys(text)

from selenium.webdriver.common.by import By

from common.common import Common
from helpers.utils import BaseError
import time


class Elements:
    check_box = (By.CLASS_NAME, "bulk-action-item-checkbox")
    fee_agency_email = (By.ID, "email")
    fee_agency_signin_email = (By.ID, "FeeAgency_SignIn__EmailAddress")
    fee_agency_signin_button = (By.ID, "FeeAgency_SignIn_Submit")
    invalid_email = "invalid_email@email.com" # find a better way to do this
    incorrect_email = "incorrect@"
    empty_email = ""


class FeeAgencies(Common, Elements):
    def __init__(self, driver):
        super().__init__(driver)

    def get_check_box_elem(self, fee_agency_name):

        def find_fee_agency_name(_fee_agency_name):
            check_box_elems = self.driver.find_elements_by_locator(self.check_box)
            for check_box_elem in check_box_elems:
                if check_box_elem.get_attribute("data-title") == _fee_agency_name:
                    return check_box_elem

        result = find_fee_agency_name(_fee_agency_name=fee_agency_name)
        if not result:
            # TODO need to add logging
            raise BaseError(f"Fee Agency: {fee_agency_name} not found.")
        return result

    def open_fee_agency_profile(self, fee_agency_name):
        elem = self.get_check_box_elem(fee_agency_name=fee_agency_name)
        title = elem.get_attribute("data-title")
        return self.open_url(self.get_all_hrefs(link_text=title))

    def get_cx_link(self, site_name):
        return self.get_all_hrefs(specific_href=site_name)

    def get_fee_agency_email(self):
        return self.driver.find_element_by_locator(self.fee_agency_email).get_attribute("value")

    def login_to_fee_agency(self, email_address):
        self.driver.find_element_by_locator(self.fee_agency_signin_email).send_keys(email_address)
        return self.do_click(self.driver.find_element_by_locator(self.fee_agency_signin_button))

    def get_fee_agency_invalid_email(self):
        return self.invalid_email

    def get_fee_agency_incorrect_email(self):
        return self.incorrect_email

    def get_fee_agency_empty_email(self):
        return self.empty_email

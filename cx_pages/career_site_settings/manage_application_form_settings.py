from common.common import Common
from selenium.webdriver.common.by import By


class Elements:
    quick_apply_radio_btn = (By.ID, "Admin_ApplicationForms__CustomApplyFormFalse")
    custom_apply_radio_btn = (By.ID, "Admin_ApplicationForms__CustomApplyFormTrue")
    application_form_save_btn = (By.ID, "Admin_ApplicationForms__SaveButton")


class ManageApplicationFormSettings(Elements, Common):
    def __init__(self, driver):
        super().__init__(driver)

    @staticmethod
    def is_checked(element):
        if not element.get_attribute("checked") == "checked":
            return False
        else:
            return True

    def manage_application_form(self, enable_quick_apply=True):
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

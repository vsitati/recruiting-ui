from common.common import Common
from selenium.webdriver.common.by import By


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


class ManageApplicationFormSettings(Elements, Common):
    def __init__(self, driver):
        super().__init__(driver)

    @staticmethod
    def is_checked(element):
        if not element.get_attribute("checked") == "checked":
            return False
        else:
            return True

    def enable_application_form_type(self, enable_quick_apply=True):
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
                if function == "clone":
                    function = "content_copy"

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

        #     if not view:
        #         match function:
        #             case "publish":
        #                 self.do_click(form_function_elem.find_element(*self.publish_form))
        #                 return form_name
        #             case "edit":
        #                 elem = form_function_elem.find_element(*self.edit_form)
        #                 self.open_url(elem.get_attribute("href"))
        #                 return form_name
        #             case "clone":
        #                 elem = form_function_elem.find_element(*self.clone_form)
        #                 self.open_url(elem.get_attribute("href"))
        #                 return form_name
        #             case "delete":
        #                 self.do_click(form_function_elem.find_element(*self.delete_form))
        #                 return form_name
        #             case _:
        #                 return "Available functions: publish, edit, clone and delete."
        #
        #     elem = form_function_elem.find_element(*self.view_form)
        #     self.open_url(elem.get_attribute("href"))
        #     return form_name
        #
        # return f"Form name {form_name} not found."





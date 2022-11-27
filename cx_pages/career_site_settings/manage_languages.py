import allure
from common.common import Common
from selenium.webdriver.common.by import By
from functools import partial
from helpers.utils import BaseError


class Elements:
    german_cbox = (By.ID, "Admin_Locales__115")
    english_cbox = (By.ID, "Admin_Locales__142")
    spanish_cbox = (By.ID, "Admin_Locales__250")
    french_cbox = (By.ID, "Admin_Locales__297")
    languages_setting_save_btn = (By.ID, "Admin_Locales__SaveButton")


class ManageLanguages(Elements, Common):
    def __init__(self, driver):
        super().__init__(driver)

    def enable_language(self, language="", get_languages=False, enable=True):
        languages = dict(
            german=partial(self.check_checkbox_custom, self.german_cbox, enable),
            english=partial(self.check_checkbox_custom, self.english_cbox, enable),
            spanish=partial(self.check_checkbox_custom, self.spanish_cbox, enable),
            french=partial(self.check_checkbox_custom, self.french_cbox, enable)
        )

        if get_languages:
            return list(languages.keys())

        try:
            return languages.get(language)()
        except TypeError:
            raise BaseError(f"Valid languages: {list(languages.keys())}")

    def set_given_langauge_to_default_only(self, language, enable=True):
        self.enable_language(language=language, enable=enable)
        if enable:
            support_languages = self.enable_language(get_languages=True)
            for support_language in support_languages:
                if support_language == language:
                    pass
                self.enable_language(language=support_language, enable=False)
            return True
        return True

    def click_language_setting_save_btn(self):
        elem = self.driver.find_element_by_locator(self.languages_setting_save_btn)
        self.driver.execute_script("arguments[0].scrollIntoView();", elem)
        return self.do_click(elem)



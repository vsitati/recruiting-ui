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


class ManageLanguages(Elements, Common):
    def __init__(self, driver):
        super().__init__(driver)

    def enable_language(self, language, enable=True):
        languages = dict(
            german=partial(self.check_checkbox_custom, self.german_cbox, enable),
            english=partial(self.check_checkbox_custom, self.english_cbox, enable),
            spanish=partial(self.check_checkbox_custom, self.spanish_cbox, enable),
            french=partial(self.check_checkbox_custom, self.french_cbox, enable)
        )
        try:
            return languages.get(language)()
        except TypeError:
            raise BaseError(f"Valid languages: {list(languages.keys())}")

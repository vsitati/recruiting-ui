from ats_pages.base import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys


class Elements:
    search_btn = (By.ID, 'quick_search_button')
    search_text = (By.ID, 'quick_search_input')


class PageHeader(BasePage, Elements):
    def __init__(self, driver):
        super().__init__(driver)

    # object_types = Enum('Types', ('Jobs Candidates'))

    def quick_search(self, search_object, search_input=""):
        elm = self.driver.find_element_by_locator(self.search_btn)
        if elm.text != search_object:
            self.do_click(elm)

        elm = self.driver.find_element_by_locator(self.search_text)
        elm.send_keys(search_input)
        elm.send_keys(Keys.ENTER)

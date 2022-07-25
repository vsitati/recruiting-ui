from cx_pages.base import BasePage
from selenium.webdriver.common.by import By


class Elements:
    pass


class CXJobDetails(Elements, BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def verify_page_title(self, expected_title):
        browser_title = self.get_title()
        self.sr_logger.logger.info(f"-- The browser is in CX now: {browser_title}")
        assert expected_title in browser_title, f"{expected_title} is NOT correct"
        return

from common.common import Common
from selenium.webdriver.common.by import By


class Elements:
    hiring_stages_chart = (By.ID, 'hiringStagesChart')
    top_sources_chart = (By.ID, 'topSourcesChart')


class Dashboard(Common, Elements):
    def __init__(self, driver):
        super().__init__(driver)

    def is_hiring_chart_visible(self):
        return self.driver.find_element_by_locator(self.hiring_stages_chart)

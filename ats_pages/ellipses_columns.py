from common.common import Common
from selenium.webdriver.common.by import By


class Elements:
    apply_btn = (By.ID, 'configurableColumnsModalApply')


class EllipsesColumns(Common, Elements):
    class Columns(enumerate):
        # Candidates
        Country = (By.ID, 'configurableColumncountry')
        State = (By.ID, "configurableColumnregion")
        TrackingCode = (By.ID, "configurableColumntrackingCode")
        RecruitingManager = (By.ID, "configurableColumnrecruitingManager")
        #Jobs

    def __init__(self, driver):
        super().__init__(driver)

    def click_apply(self):
        self.go_click(self.apply_btn)

    def select_column(self, column: Columns):
        elm = self.driver.find_element_by_locator(column)
        self.do_click(elm)

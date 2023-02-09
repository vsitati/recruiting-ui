from common.common import Common
from selenium.webdriver.common.by import By
from time import sleep


class Elements:
    apply_btn = (By.ID, 'configurableColumnsModalApply')
    remove_x = (By.CSS_SELECTOR, ".close.pull-right")


class EllipsesColumns(Common, Elements):
    class Columns(enumerate):
        # Candidates
        Country = (By.ID, 'configurableColumncountry')
        State = (By.ID, "configurableColumnregion")
        TrackingCode = (By.ID, "configurableColumntrackingCode")
        RecruitingManager = (By.ID, "configurableColumnrecruitingManager")
        #Jobs
        Status = (By.ID, 'configurableColumnisActive')
        PostingStatus = (By.ID, 'configurableColumnstatusLabel')
        AllLocations = (By.ID, 'configurableColumnallLocations')
        FarthestStage = (By.ID, 'configurableColumnfarthestStageName')
        EvergreenJob = (By.ID, 'configurableColumnisEvergreen')
        LastModified = (By.ID, 'configurableColumnmodifiedDate')
        PostedDate = (By.ID, 'configurableColumnpostingDate')

    def __init__(self, driver):
        super().__init__(driver)

    def click_apply(self):
        sleep(self.sleep_time)
        self.go_click(self.apply_btn)
        sleep(self.sleep_time * 3)

    def select_column(self, column: Columns):
        elm = self.driver.find_element_by_locator(column)
        self.do_click(elm)
        sleep(self.sleep_time)
        
    def remove_column(self, column: Columns):
        elm = self.driver.find_element_by_locator(column)
        elm = elm.find_element(*self.remove_x)
        self.do_click(elm)

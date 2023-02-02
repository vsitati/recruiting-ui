from selenium.webdriver.common.by import By
from common.common import Common
from helpers.utils import BaseError
import time
import datetime
from test_data.test_data_details import CandidateData


class Elements:
    check_box = (By.CSS_SELECTOR, ".resume-checkbox.bulk-action-item-checkbox")
    check_box1 = (By.NAME, "bulkActionItemId")
    next_page = (By.ID, "bulkActionItemsPagerButton_next")
    pagination_parent = (By.ID, "bulkActionItemPager")
    pagination_tags = (By.TAG_NAME, "li")
    result_sheet = (By.ID, 'bulkActionItemResultsTable')
    result_sheet_header = (By.XPATH, "//table[@id='bulkActionItemResultsTable']//th")
    result_sheet_column = (By.XPATH, "//table[@id='bulkActionItemResultsTable']//td")
    saved_candidate_search_name = (By.XPATH, "//div[@id='pageHeader']//h1")
    filter_label = (By.XPATH, "//div[@id='appliedFilters']//h3")
    record_count = (By.ID, "bulkActionItemsRecordCount")


class CandidateAdvancedSearch(Common, Elements):
    def __init__(self, driver):
        super().__init__(driver)

    def verify_is_candidate_search_result_page(self):
        elm = self.driver.find_element_by_locator(self.saved_candidate_search_name)
        self.__comparing(elm.text, CandidateData.candidate_search_result_page.get("saved_candidate_search_name"))

        elm = self.driver.find_element_by_locator(self.filter_label)
        self.__comparing(elm.text, CandidateData.candidate_search_result_page.get("filter_label"))

        return

    def verify_record_count(self):
        return self.get_text(self.record_count)

    def get_check_box_elem(self, candidate_name):

        def find_candidate_name(_candidate_name):
            check_box_elems = self.driver.find_elements_by_locator(self.check_box)
            for check_box_elem in check_box_elems:
                if check_box_elem.get_attribute("data-candidatename") == _candidate_name:
                    return check_box_elem

        result = find_candidate_name(_candidate_name=candidate_name)
        # TODO OPen submission and Same name
        if not result:
            pagination_parent_elem = self.driver.find_element_by_locator(self.pagination_parent)
            pagination_parent_elems = pagination_parent_elem.find_elements(*self.pagination_tags)
            total_pages = len(pagination_parent_elems[1:-1])
            for i in range(total_pages):
                next_page_elem = self.driver.find_element_by_locator(self.next_page)
                self.driver.execute_script("arguments[0].scrollIntoView();", next_page_elem)
                self.do_click(next_page_elem)
                time.sleep(2)
                result = find_candidate_name(_candidate_name=candidate_name)
                if result:
                    return result

        if not result:
            # TODO need to add logging
            raise BaseError(f"Candidate Name: {candidate_name} not found.")
        return result

    def open_candidate_profile(self, candidate_name):
        elem = self.get_check_box_elem(candidate_name=candidate_name)
        resume_id = elem.get_attribute("value")
        return self.open_url(self.get_all_hrefs(specific_href=resume_id))

    def open_job_title(self, candidate_name):
        elem = self.get_check_box_elem(candidate_name=candidate_name)
        job_id = elem.get_attribute("data-jobid")
        return self.open_url(self.get_all_hrefs(specific_href=job_id))

    def select_candidate(self, candidate_name):
        elem = self.get_check_box_elem(candidate_name=candidate_name)
        return self.do_click(elem)

    # return values of a column in the List format
    def get_candidate_column_values(self, column):
        # check if result record exists
        time.sleep(3)
        elm_result_sheet = self.driver.find_element_by_locator(self.result_sheet)
        elms = elm_result_sheet.find_elements(*self.check_box1)
        if len(elms) == 0:
            self.sr_logger.logger.info("-- Candidate Search returns 0 record.")
            return 0

        # get the column position in the header
        # elms = elm_result_sheet.find_elements(By.XPATH, self.result_sheet_header)
        elms = self.driver.find_elements(*self.result_sheet_header)
        count = len(elms)
        pos = 0
        for elm in elms:
            if column in elm.text:
                break
            pos += 1

        # get column values list
        # elms = elm_result_sheet.find_elements(By.XPATH, self.result_sheet_column)
        elms = self.driver.find_elements(*self.result_sheet_column)
        col_list = []
        for i in range(len(elms)//count):
            loc = pos + i * count
            col_value = elms[loc].text
            col_list.append(col_value)

        return col_list

    def sort_candidate_column_header(self, column, ordering, date=""):
        # elm_result_sheet = self.driver.find_element_by_locator(self.result_sheet)
        elms = self.driver.find_elements(*self.result_sheet_header)
        for elm in elms:
            if column in elm.text:
                self.do_click(elm)
                break
        else:
            self.sr_logger.logger.error(f"There is no such a column {column}.")

        col_list = self.get_candidate_column_values(column)
        self.verify_ordering(col_list, ordering, date)
        return

    # alist: a list of string values or dates
    # direction: "asc", "desc"
    def verify_ordering(self, alist, direction, date=""):
        if len(alist) == 0:
            return self.sr_logger.logger.error("There is 0 record.")
        date_format = "%m/%d/%y"
        for i in range(len(alist)-1):
            if date == "date":
                date1 = datetime.datetime.strptime(alist[i], date_format).date()
                date2 = datetime.datetime.strptime(alist[i + 1], date_format).date()
            if direction == "asc":
                if date == "date":
                    if date1 > date2:
                        raise Exception(f"column values sorting: {alist[i]} and {alist[i + 1]}.")
                else:
                    if alist[i].lower() > alist[i+1].lower():
                        raise Exception(f"column values sorting: {alist[i]} and {alist[i + 1]}.")
            elif direction == "desc":
                if date == "date":
                    if date1 < date2:
                        raise Exception(f"column values sorting: {alist[i]} and {alist[i + 1]}.")
                else:
                    if alist[i].lower() < alist[i+1].lower():
                        raise Exception(f"column values sorting: {alist[i]} and {alist[i+1]}.")

        return

    def verify_value_exist(self, a_value, alist):
        if len(alist) == 0:
            self.sr_logger.logger.error("There is 0 record.")
            return
        for i in range(len(alist)):
            assert a_value in alist[i], "value NOT exist."

    # base_date: today - days_diff
    # dates: a list of dates
    # direction: "older", "newer"
    def compare_date_range(self, days_diff, dates, direction):
        if len(dates) == 0:
            self.sr_logger.logger.error("There is 0 record.")
            return
        date_format = "%m/%d/%y"
        for i in range(len(dates)):
            base_date = datetime.date.today() - datetime.timedelta(days_diff)
            the_date = datetime.datetime.strptime(dates[i], date_format).date()
            if direction == "older":
                assert the_date > base_date, "date NOT older than."
            elif direction == "newer":
                assert the_date < base_date, "date NOT newer than."

    def __comparing(self, source, target):
        if source == target:
            self.sr_logger.logger.info(f"-- {source} is correct")
            assert source == target
        else:
            self.sr_logger.logger.error(f"@@ {source} is NOT correct")

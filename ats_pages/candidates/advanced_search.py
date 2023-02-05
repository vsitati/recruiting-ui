from selenium.webdriver.common.by import By
from common.common import Common
from helpers.utils import BaseError, round_up
import time
import datetime
import itertools
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
    table_row = (By.TAG_NAME, "tr")
    table_column = (By.TAG_NAME, "td")
    table_heading = (By.TAG_NAME, "th")


class CandidateAdvancedSearch(Common, Elements):
    def __init__(self, driver):
        super().__init__(driver)

    def verify_is_candidate_search_result_page(self):
        elm = self.driver.find_element_by_locator(self.saved_candidate_search_name)
        self.__comparing(elm.text, CandidateData.candidate_search_result_page.get("saved_candidate_search_name"))

        elm = self.driver.find_element_by_locator(self.filter_label)
        self.__comparing(elm.text, CandidateData.candidate_search_result_page.get("filter_label"))

        return

    def get_advanced_search_count(self):
        self.driver.find_element_by_locator(self.record_count)
        try:
            record_count = int(self.get_text(self.record_count))
        except ValueError:
            time.sleep(self.sleep_time)
            record_count = int(self.get_text(self.record_count))
        return record_count

    def get_check_box_elem(self, candidate_name, records_per_page=25):

        def find_candidate_name(_candidate_name):
            check_box_elems = self.driver.find_elements_by_locator(self.check_box)
            for check_box_elem in check_box_elems:
                if check_box_elem.get_attribute("data-candidatename") == _candidate_name:
                    return check_box_elem

        result = find_candidate_name(_candidate_name=candidate_name)
        # TODO OPen submission and Same name
        if not result:
            tot_records_found = self.get_advanced_search_count()
            total_pages = round_up(tot_records_found/records_per_page)

            print(f"Total pages: {total_pages}")
            for i in range(total_pages):
                next_page_elem = self.driver.find_element_by_locator(self.next_page)
                self.driver.execute_script("arguments[0].scrollIntoView();", next_page_elem)
                self.do_click(next_page_elem)
                time.sleep(2)
                print(f"Page: {i}/{total_pages}")
                result = find_candidate_name(_candidate_name=candidate_name)
                if result:
                    return result

        if not result:
            # TODO need to add logging
            assert False, f"Candidate Name: {candidate_name} not found."
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
    def get_candidate_column_values(self, column_name):
        # check if result record exists
        time.sleep(3)
        elm_result_sheet = self.driver.find_element_by_locator(self.result_sheet)
        _rows = elm_result_sheet.find_elements(*self.table_row)

        rows = (row.find_elements(*self.table_column) for row in _rows)

        elms = elm_result_sheet.find_elements(*self.check_box1)
        if len(elms) == 0:
            self.sr_logger.logger.info("-- Candidate Search returns 0 record.")
            return 0

        table_heading_elems = self.driver.find_elements_by_locator(self.table_heading)
        table_headings = [table_heading_elem.text.replace("↑", "").replace("↓", "")
                          for table_heading_elem in table_heading_elems]
        column_name_index = table_headings.index(column_name)

        row_info = [[col.text for col in row][column_name_index] for row in rows if row]
        # row_info = list()
        # column_name_index = table_headings.index(column_name)
        # col_text_list = ((col.text for col in row) for row in rows if row)
        # for col_text in col_text_list:
        #     row_info.append(list(col_text)[column_name_index])
        # # for _rows in rows:
        # #     if _rows:
        # #         col_text = list()
        # #         for _row in _rows:
        # #             col_text.append(_row.text)
        # #         row_info.append(col_text[column_name_index])
        return row_info

        # return [[col.text for col in row][column_name_index] for row in rows if row]

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
    # date_time: date: date only; time: date and time; nothing: not a date format
    def verify_ordering(self, alist, direction, date_time=""):
        if len(alist) == 0:
            return self.sr_logger.logger.error("There is 0 record.")
        date_format = "%m/%d/%y"
        time_format = "%m/%d/%y, %I:%M %p"
        for i in range(len(alist)-1):
            if date_time == "date":
                date1 = datetime.datetime.strptime(alist[i], date_format).date()
                date2 = datetime.datetime.strptime(alist[i + 1], date_format).date()
            if date_time == "time":
                date1 = datetime.datetime.strptime(alist[i], time_format)
                date2 = datetime.datetime.strptime(alist[i + 1], time_format)

            if direction == "asc":
                if date_time == "date" or date_time == "time":
                    if date1 > date2:
                        raise Exception(f"column values sorting: {alist[i]} and {alist[i + 1]}.")
                else:
                    if alist[i].lower() > alist[i+1].lower():
                        raise Exception(f"column values sorting: {alist[i]} and {alist[i + 1]}.")
            elif direction == "desc":
                if date_time == "date" or date_time == "time":
                    if date1 < date2:
                        raise Exception(f"column values sorting: {alist[i]} and {alist[i + 1]}.")
                else:
                    if alist[i].lower() < alist[i+1].lower():
                        raise Exception(f"column values sorting: {alist[i]} and {alist[i + 1]}.")
        return

    def verify_value_exist(self, a_value, alist):
        if len(alist) == 0:
            return self.sr_logger.logger.error("There is 0 record.")

        for list_val in alist:
            assert a_value in list_val, "value DOES NOT exist."

    # base_date: today - days_diff
    # dates: a list of dates
    # direction: "older", "newer"
    def compare_in_last_days_range(self, days_diff, dates):
        date_format = "%m/%d/%y"
        past_date = datetime.date.today() - datetime.timedelta(days_diff)
        todays_date = datetime.date.today()

        if len(dates) == 0:
            self.sr_logger.logger.error("There is 0 record.")
            return

        format_dates = [datetime.datetime.strptime(date, date_format).date() for date in dates]
        format_dates.sort()  # Sorted from oldest to newer date

        oldest_date, *_ = format_dates
        latest_date = format_dates[-1]

        assert past_date <= oldest_date <= latest_date, \
            f"past date: {past_date} <= oldest date: {oldest_date} <= latest date: {latest_date} "
        assert latest_date <= todays_date, \
            f"latest date: {latest_date} CANNOT be newer than today's date: {todays_date}"

    def compare_date_range(self, dates, date_start, date_end):
        if len(dates) == 0:
            self.sr_logger.logger.error("There is 0 record.")
            return
        date_format = "%m/%d/%Y"
        date_format1 = "%m/%d/%y"
        date_start = datetime.datetime.strptime(date_start, date_format).date()
        date_end = datetime.datetime.strptime(date_end, date_format).date()
        for i in range(len(dates)):
            the_date = datetime.datetime.strptime(dates[i], date_format1).date()
            if date_start <= the_date <= date_end:
                continue
            else:
                raise BaseError(f"{the_date} not within: {date_start}, {date_end}")

    def __comparing(self, source, target):
        if source == target:
            self.sr_logger.logger.info(f"-- {source} is correct")
            assert source == target
        else:
            self.sr_logger.logger.error(f"@@ {source} is NOT correct")

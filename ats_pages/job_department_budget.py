from common.common import Common
from selenium.webdriver.common.by import By
from test_data.test_data_details import JobData
from time import sleep


class Elements:
    # Department Information
    business_unit = (By.ID, "businessUnitId")
    department = (By.ID, "department_id_label")
    hiring_manager = (By.ID, "HireManager_label")
    recruiting_team = (By.ID, "jobUsers_input")
    industry = (By.ID, "industry")
    business_function = (By.ID, "function")
    budgeted_salary = (By.ID, "BudgetedSalary")
    budgeted_currency = (By.ID, "budgetcurrency")
    budgeted_quarter = (By.ID, "budgetedQuarter")
    budgeted_year = (By.ID, "budgetedyear")

    # Fee Agency
    select_fee_agency = (By.ID, "agency")
    select_all = (By.CLASS_NAME, "selectAll")
    deselect_all = (By.CLASS_NAME, "deselectAll")

    # Buttons
    continue_btn = (By.ID, "jobform2_submit")
    reset_btn = (By.ID, "jobform2_rset")


class JobDepartmentBudget(Common, Elements):
    def __init__(self, driver):
        super().__init__(driver)

    def fill_out_all_job_departments_fields(self):
        # Department Information
        # self.select_from_dropdown(self.business_unit, JobData.job_data.get("business_unit"))
        self.select_auto_complete(self.department, JobData.job_data.get("department"))
        self.select_auto_complete(self.hiring_manager, JobData.job_data.get("hiring_manager"))
        self.select_auto_complete(self.recruiting_team, JobData.job_data.get("recruiting_team"))
        self.select_from_dropdown(self.industry, JobData.job_data.get("industry"))
        self.select_from_dropdown(self.business_function, JobData.job_data.get("business_function"))
        self.enter_richtext_integer(self.budgeted_salary, JobData.job_data.get("budgeted_salary"))
        self.select_from_dropdown(self.budgeted_currency, JobData.job_data.get("budgeted_currency"))
        self.select_from_dropdown(self.budgeted_quarter, JobData.job_data.get("budgeted_quarter"))
        self.select_from_dropdown(self.budgeted_year, JobData.job_data.get("budgeted_year"))

        # Fee Agency
        self.go_click(self.select_all)
        self.go_click(self.deselect_all)
        self.select_multiselect_list(self.select_fee_agency, JobData.job_data.get("select_fee_agency"))

        # Buttons
        sleep(self.sleep_time)
        self.go_click(self.continue_btn)

from ats_pages.base import BasePage
from selenium.webdriver.common.by import By


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


class JobDepartmentBudget(BasePage, Elements):
    def __init__(self, driver):
        super().__init__(driver)

    def fill_out_all(self):
        # Department Information
        self.select_dropdown_element(self.business_unit, "business_unit")
        self.select_auto_complete_element(self.department, "department")
        self.select_auto_complete_element(self.hiring_manager, "hiring_manager")
        self.select_auto_complete_element(self.recruiting_team, "recruiting_team")
        self.select_dropdown_element(self.industry, "industry")
        self.select_dropdown_element(self.business_function, "business_function")
        self.enter_richtext_integer_element(self.budgeted_salary, "budgeted_salary")
        self.select_dropdown_element(self.budgeted_currency, "budgeted_currency")
        self.select_dropdown_element(self.budgeted_quarter, "budgeted_quarter")
        self.select_dropdown_element(self.budgeted_year, "budgeted_year")

        # Fee Agency
        self.go_click(self.select_all)
        self.go_click(self.deselect_all)
        self.select_multiselect_list_element(self.select_fee_agency, "select_fee_agency")

        # Buttons
        self.go_click(self.reset_btn)

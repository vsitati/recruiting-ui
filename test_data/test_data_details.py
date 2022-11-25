from test_data.company_data import CompanyData
from test_data.job_data import JobData
from test_data.validation_data import ValidationData
from test_data.cx_candidate_apply.quick_apply.quick_apply_form_data import QuickApplyForm


class TestData(CompanyData, ValidationData, QuickApplyForm):
    pass


class TestDataJob(JobData):
    pass

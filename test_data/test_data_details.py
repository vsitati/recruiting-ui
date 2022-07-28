from test_data.company_data import CompanyData
from test_data.job_data import JobData
from test_data.validation_data import ValidationData


class TestData(CompanyData, ValidationData):
    pass


class TestDataJob(JobData):
    pass

from test_data.company_data import CompanyData
from test_data.job_data import JobData
from test_data.validation_data import ValidationData
from test_data.cx_candidate_apply.quick_apply.quick_apply_form_data import QuickApplyForm
from test_data.cx_candidate_apply.portal_langauge_text import PortalLanguageTextData


class SrTestData(CompanyData, ValidationData,
                 QuickApplyForm, PortalLanguageTextData):
    pass

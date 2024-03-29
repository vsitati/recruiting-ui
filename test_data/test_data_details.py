from test_data.company_data import CompanyData
from test_data.job_data import JobData
from test_data.candidate_data import CandidateData
from test_data.validation_data import ValidationData
from test_data.cx_candidate_apply.quick_apply.quick_apply_form_data import QuickApplyForm
from test_data.cx_candidate_apply.portal_langauge_text import PortalLanguageTextData
from test_data.cx_candidate_apply.configured_apply.configured_apply_form_data import ConfiguredApplyForm


class SrTestData(CompanyData, ValidationData,
                 QuickApplyForm, PortalLanguageTextData, ConfiguredApplyForm):
    pass

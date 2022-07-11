from ats_pages.base import BasePage
from selenium.webdriver.common.by import By


class Elements:
    # Job Administration
    recruiting_manager = (By.ID, "mgrid")
    assigned_recruiter = (By.ID, 'ownerid')
    replies_emailed_to = (By.ID, 'mailings')

    # Job Information
    job_template = (By.ID, "job_template_id_label")
    hiring_workflow = (By.ID, 'workflowId')
    evergreen_job = [By.ID, 'isEvergreen_']
    internal_job_title = (By.ID, 'job_title')
    posted_job_title = (By.ID, 'ext_job_title')
    tracking_code = (By.ID, 'trackingcode')
    number_of_positions = (By.ID, "numofpositions")
    require_eForm_submission = [By.ID, "display_eform_"]
    status = (By.ID, 'status')
    position_type = (By.ID, 'jobtype')
    job_level = (By.ID, "joblev")
    job_duration = (By.ID, 'duration')
    expected_start_date = (By.ID, 'start')

    # Location Details
    job_location_code = (By.ID, "location_id_label")
    country = (By.ID, "country")
    address_line_1 = (By.ID, "addressLine1")
    address_line_2 = (By.ID, "addressLine2")
    city = (By.ID, "city")
    state = (By.ID, "state")
    zip_postal_code = (By.ID, "postal_code")
    additional_locations = (By.ID, "additionalLocations_input")

    # Compliance
    eeo1_job_category = (By.ID, 'eeoccat')
    aap_job_group = (By.ID, 'eeogroup')
    talent_assessment = (By.ID, 'packageId')
    do_not_display_assessment_on_job_portal = (By.ID, 'recruiterInitiatedAssessment')

    # Position Requirements
    travel = (By.ID, "travel")
    per_diem_included = [By.ID, "perdiem_"]
    minimum_salary = (By.ID, "salmin")
    maximum_salary = (By.ID, "salmax")
    salary_type = (By.ID, "saltype")
    salary_currency = (By.ID, "salcurrency")
    level_of_education = (By.ID, "degree")
    years_of_experience = (By.ID, "experyrs")

    # EmployeeReferrals.com
    list_on_employeeReferralscom = [By.ID, "hasEmployeeReferral_"]
    referral_bonus = (By.ID, 'erReferralBonus')
    referral_points = (By.ID, 'erReferralPoints')
    keywords = (By.ID, 'erKeywords')
    negative_keywords = (By.ID, 'erNegativeKeywords')
    hot_job = [By.ID, 'erIsHotJob_']

    # Description/Skills
    job_description = (By.ID, "jobdescription_ifr")
    required_skills = (By.ID, "requiredskills_ifr")
    required_experience = (By.ID, "experience_ifr")
    skills_candidate_should_possess = (By.ID, "internalskills_ifr")
    notes_on_position = (By.ID, "internaldesc_ifr")

    # Custom Fields
    job_grade = (By.ID, "worldco_jobgrade_cstfld")
    exemption_status = (By.ID, "worldco_exempstatus_cstfld")
    newdate = (By.ID, "TestCustomDate_cstfld")
    collect_eeo_for_this_job = (By.ID, "dspeeoform_cstfld")

    # Buttons
    continue_btn = (By.ID, "jobform1_submit")
    reset_btn = (By.ID, "jobform1_reset")


class JobPositionDetails(BasePage, Elements):
    def __init__(self, driver):
        super().__init__(driver)

    def fill_out_minimum(self):
        # Job Administration
        self.select_dropdown_element(self.assigned_recruiter, "assigned_recruiter")

        # Job Information
        self.enter_text_element(self.internal_job_title, "internal_job_title")
        self.enter_text_element(self.posted_job_title, "posted_job_title")
        self.enter_text_element(self.tracking_code, "tracking_code")

        # Location Details
        self.select_dropdown_element(self.country, "country")
        self.enter_text_element(self.address_line_1, "address_line_1")
        self.enter_text_element(self.address_line_2, "address_line_2")
        self.enter_text_element(self.city, "city")
        self.select_dropdown_element(self.state, "state")
        self.enter_text_element(self.zip_postal_code, "zip_postal_code")

        # Compliance
        # Position Requirements

        # EmployeeReferrals.com
        self.enter_richtext_integer_element(self.referral_bonus, "referral_bonus")
        self.enter_richtext_integer_element(self.referral_points, "referral_points")

        # Description/Skills
        self.enter_richtext_element(self.job_description, "job_description")

        # Custom Fields
        self.select_dropdown_element(self.exemption_status, "exemption_status")
        self.select_dropdown_element(self.collect_eeo_for_this_job, "collect_eeo_for_this_job")

        # Buttons
        self.go_click(self.continue_btn)

    def fill_out_all(self):
        # Job Administration
        self.select_dropdown_element(self.recruiting_manager, "recruiting_manager")
        self.select_dropdown_element(self.assigned_recruiter, "assigned_recruiter")
        self.select_dropdown_element(self.replies_emailed_to, "replies_emailed_to")

        # Job Information
        # self.select_auto_complete_element(self.job_template, "job_template")
        self.select_dropdown_element(self.hiring_workflow, "hiring_workflow")
        self.click_radio_yes_no_element(self.evergreen_job, "evergreen_job")
        self.enter_text_element(self.internal_job_title, "internal_job_title")
        self.enter_text_element(self.posted_job_title, "posted_job_title")
        self.enter_text_element(self.tracking_code, "tracking_code")
        self.enter_richtext_integer_element(self.number_of_positions, "number_of_positions")
        self.click_radio_yes_no_element(self.require_eForm_submission, "require_eForm_submission")
        self.select_dropdown_element(self.status, "status")
        self.select_dropdown_element(self.position_type, "position_type")
        self.select_dropdown_element(self.job_level, "job_level")
        self.select_dropdown_element(self.job_duration, "job_duration")
        self.pck_datepicker_element(self.expected_start_date, "expected_start_date")

        # Location Details
        # self.select_auto_complete_element(self.job_location_code, "job_location_code")
        self.select_dropdown_element(self.country, "country")
        self.enter_text_element(self.address_line_1, "address_line_1")
        self.enter_text_element(self.address_line_2, "address_line_2")
        self.enter_text_element(self.city, "city")
        self.select_dropdown_element(self.state, "state")
        self.enter_text_element(self.zip_postal_code, "zip_postal_code")
        self.select_auto_complete_element(self.additional_locations, "additional_locations")

        # Compliance
        self.select_dropdown_element(self.eeo1_job_category, "eeo1_job_category")
        self.select_dropdown_element(self.aap_job_group, "aap_job_group")
        self.select_dropdown_element(self.talent_assessment, "talent_assessment")
        self.check_checkbox_element(self.do_not_display_assessment_on_job_portal, "do_not_display_assessment_on_job_portal")

        # Position Requirements
        self.select_dropdown_element(self.travel, "travel")
        self.click_radio_yes_no_element(self.per_diem_included, "per_diem_included")
        self.enter_text_element(self.minimum_salary, "minimum_salary")
        self.enter_text_element(self.maximum_salary, "maximum_salary")
        self.select_dropdown_element(self.salary_type, "salary_type")
        self.select_dropdown_element(self.salary_currency, "salary_currency")
        self.select_dropdown_element(self.level_of_education, "level_of_education")
        self.select_dropdown_element(self.years_of_experience, "years_of_experience")

        # EmployeeReferrals.com
        self.click_radio_yes_no_element(self.list_on_employeeReferralscom, "list_on_employeeReferralscom")
        self.enter_richtext_integer_element(self.referral_bonus, "referral_bonus")
        self.enter_richtext_integer_element(self.referral_points, "referral_points")
        self.enter_text_element(self.keywords, "keywords")
        self.enter_text_element(self.negative_keywords, "negative_keywords")
        self.click_radio_yes_no_element(self.hot_job, "hot_job")

        # Description/Skills
        self.enter_richtext_element(self.job_description, "job_description")
        self.enter_richtext_element(self.required_skills, "required_skills")
        self.enter_richtext_element(self.required_experience, "required_experience")
        self.enter_richtext_element(self.skills_candidate_should_possess, "skills_candidate_should_possess")
        self.enter_richtext_element(self.notes_on_position, "notes_on_position")

        # Custom Fields
        self.enter_text_element(self.job_grade, "job_grade")
        self.select_dropdown_element(self.exemption_status, "exemption_status")
        self.pck_datepicker_element(self.newdate, "newdate")
        self.select_dropdown_element(self.collect_eeo_for_this_job, "collect_eeo_for_this_job")

        # Buttons
        self.go_click(self.continue_btn)

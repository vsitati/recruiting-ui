from common.common import Common
from selenium.webdriver.common.by import By
from test_data.test_data_details import JobData
from time import sleep


class Elements:
    # Job Administration
    recruiting_manager = (By.ID, "mgrid")
    assigned_recruiter = (By.ID, 'ownerid')
    replies_emailed_to = (By.ID, 'mailings')

    # Job Information
    job_template = (By.ID, "job_template_id_label")
    closed_date = (By.ID, 'closeddate')
    hiring_workflow = (By.ID, 'workflowId')
    evergreen_job = [By.ID, 'isEvergreen_']
    internal_job_title = (By.ID, 'job_title')
    posted_job_title = (By.ID, 'ext_job_title')
    tracking_code = (By.ID, 'trackingcode')
    number_of_positions = (By.ID, "numofpositions")
    require_eForm_submission = [By.ID, "display_eform_"]
    posting_status = (By.ID, 'status')
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

    save_btn = (By.CSS_SELECTOR, "button.lifesuite__float-right:nth-child(1)")
    cancel_btn = (By.CSS_SELECTOR, "button.lifesuite__float-right:nth-child(2)")


class JobPositionDetails(Common, Elements):
    def __init__(self, driver):
        super().__init__(driver)

    # class PostingStatus(enumerate):
    #     Normal = "Normal - Int./Ext. Applicants"
    #     External = "External"
    #     Internal = "Internal"

    def fill_out_minimum_job_details_fields(self):
        # Job Administration
        self.select_from_dropdown(self.assigned_recruiter, JobData.job_data.get("assigned_recruiter"))

        # Job Information
        self.enter_text(self.internal_job_title, JobData.job_data.get("internal_job_title"))
        self.enter_text(self.posted_job_title, JobData.job_data.get("posted_job_title"))
        self.enter_text(self.tracking_code, JobData.job_data.get("tracking_code"))

        # Location Details
        self.select_from_dropdown(self.country, JobData.job_data.get("country"))
        self.enter_text(self.address_line_1, JobData.job_data.get("address_line_1"))
        self.enter_text(self.address_line_2, JobData.job_data.get("address_line_2"))
        self.enter_text(self.city, JobData.job_data.get("city"))
        self.select_from_dropdown(self.state, JobData.job_data.get("state"))
        self.enter_text(self.zip_postal_code, JobData.job_data.get("zip_postal_code"))

        # Compliance
        # Position Requirements

        # EmployeeReferrals.com
        self.enter_richtext_integer(self.referral_bonus, JobData.job_data.get("referral_bonus"))
        self.enter_richtext_integer(self.referral_points, JobData.job_data.get("referral_points"))

        # Description/Skills
        self.enter_richtext(self.job_description, JobData.job_data.get("job_description"))

        # Custom Fields
        self.select_from_dropdown(self.exemption_status, JobData.job_data.get("exemption_status"))
        self.select_from_dropdown(self.collect_eeo_for_this_job, JobData.job_data.get("collect_eeo_for_this_job"))

        # Buttons
        self.go_click(self.continue_btn)

    def fill_out_all_job_details_fields(self):
        # Job Administration
        self.select_from_dropdown(self.recruiting_manager, JobData.job_data.get("recruiting_manager"))
        self.select_from_dropdown(self.assigned_recruiter, JobData.job_data.get("assigned_recruiter"))
        self.select_from_dropdown(self.replies_emailed_to, JobData.job_data.get("replies_emailed_to"))

        # Job Information
        # self.select_auto_complete(self.job_template, JobData.job_data.get("job_template"))
        self.select_from_dropdown(self.hiring_workflow, JobData.job_data.get("hiring_workflow"))
        self.click_radio_yes_no(self.evergreen_job, JobData.job_data.get("evergreen_job"))
        self.enter_text(self.internal_job_title, JobData.job_data.get("internal_job_title"))
        self.enter_text(self.posted_job_title, JobData.job_data.get("posted_job_title"))
        self.enter_text(self.tracking_code, JobData.job_data.get("tracking_code"))
        self.enter_richtext_integer(self.number_of_positions, JobData.job_data.get("number_of_positions"))
        # self.click_radio_yes_no(self.require_eForm_submission, JobData.job_data.get("require_eForm_submission"))
        self.select_from_dropdown(self.posting_status, JobData.job_data.get("posting_status_normal"))
        self.select_from_dropdown(self.position_type, JobData.job_data.get("position_type"))
        self.select_from_dropdown(self.job_level, JobData.job_data.get("job_level"))
        self.select_from_dropdown(self.job_duration, JobData.job_data.get("job_duration"))
        self.pick_datepicker(self.expected_start_date, JobData.job_data.get("expected_start_date"))

        # Location Details
        # self.select_auto_complete(self.job_location_code, JobData.job_data.get("job_location_code"))
        self.select_from_dropdown(self.country, JobData.job_data.get("country"))
        self.enter_text(self.address_line_1, JobData.job_data.get("address_line_1"))
        self.enter_text(self.address_line_2, JobData.job_data.get("address_line_2"))
        self.enter_text(self.city, JobData.job_data.get("city"))
        self.select_from_dropdown(self.state, JobData.job_data.get("state"))
        self.enter_text(self.zip_postal_code, JobData.job_data.get("zip_postal_code"))
        self.select_auto_complete(self.additional_locations, JobData.job_data.get("additional_locations"))

        # Compliance
        self.select_from_dropdown(self.eeo1_job_category, JobData.job_data.get("eeo1_job_category"))
        self.select_from_dropdown(self.aap_job_group, JobData.job_data.get("aap_job_group"))
        # self.select_from_dropdown(self.talent_assessment, JobData.job_data.get("talent_assessment"))
        # self.check_checkbox(self.do_not_display_assessment_on_job_portal,
        #                     JobData.job_data.get("do_not_display_assessment_on_job_portal"))

        # Position Requirements
        self.select_from_dropdown(self.travel, JobData.job_data.get("travel"))
        self.click_radio_yes_no(self.per_diem_included, JobData.job_data.get("per_diem_included"))
        self.enter_text(self.minimum_salary, JobData.job_data.get("minimum_salary"))
        self.enter_text(self.maximum_salary, JobData.job_data.get("maximum_salary"))
        self.select_from_dropdown(self.salary_type, JobData.job_data.get("salary_type"))
        self.select_from_dropdown(self.salary_currency, JobData.job_data.get("salary_currency"))
        self.select_from_dropdown(self.level_of_education, JobData.job_data.get("level_of_education"))
        self.select_from_dropdown(self.years_of_experience, JobData.job_data.get("years_of_experience"))

        # EmployeeReferrals.com
        self.click_radio_yes_no(self.list_on_employeeReferralscom, JobData.job_data.get("list_on_employeeReferralscom"))
        self.enter_richtext_integer(self.referral_bonus, JobData.job_data.get("referral_bonus"))
        self.enter_richtext_integer(self.referral_points, JobData.job_data.get("referral_points"))
        self.enter_text(self.keywords, JobData.job_data.get("keywords"))
        self.enter_text(self.negative_keywords, JobData.job_data.get("negative_keywords"))
        self.click_radio_yes_no(self.hot_job, JobData.job_data.get("hot_job"))

        # Description/Skills
        self.enter_richtext(self.job_description, JobData.job_data.get("job_description"))
        self.enter_richtext(self.required_skills, JobData.job_data.get("required_skills"))
        self.enter_richtext(self.required_experience, JobData.job_data.get("required_experience"))
        self.enter_richtext(self.skills_candidate_should_possess,
                            JobData.job_data.get("skills_candidate_should_possess"))
        self.enter_richtext(self.notes_on_position, JobData.job_data.get("notes_on_position"))

        # Custom Fields
        self.enter_text(self.job_grade, JobData.job_data.get("job_grade"))
        self.select_from_dropdown(self.exemption_status, JobData.job_data.get("exemption_status"))
        # self.pick_datepicker(self.newdate, JobData.job_data.get("newdate"))
        self.select_from_dropdown(self.collect_eeo_for_this_job, JobData.job_data.get("collect_eeo_for_this_job"))

        # Buttons
        sleep(self.sleep_time)
        self.go_click(self.continue_btn)

    def edit_job_details_fields(self):
        # Job Administration
        self.select_from_dropdown(self.replies_emailed_to, JobData.job_data.get("replies_emailed_to_edit"))

        # Job Information
        self.pick_datepicker(self.closed_date, JobData.job_data.get("closed_date"))
        self.click_radio_yes_no(self.evergreen_job, JobData.job_data.get("evergreen_job_edit"))
        self.enter_text(self.internal_job_title, JobData.job_data.get("internal_job_title_edit"))
        # self.enter_text(self.posted_job_title, JobData.job_data.get("posted_job_title_edit"))
        self.select_from_dropdown(self.position_type, JobData.job_data.get("position_type_edit"))
        self.select_from_dropdown(self.job_duration, JobData.job_data.get("job_duration_edit"))
        self.pick_datepicker(self.expected_start_date, JobData.job_data.get("expected_start_date_edit"))

        # Job Location
        self.enter_text(self.city, JobData.job_data.get("city_edit"))
        self.select_from_dropdown(self.state, JobData.job_data.get("state_edit"))
        self.select_auto_complete(self.additional_locations, JobData.job_data.get("additional_locations_edit"))

        # Compliance
        # Position Requirements
        self.select_from_dropdown(self.travel, JobData.job_data.get("travel_edit"))
        self.select_from_dropdown(self.salary_type, JobData.job_data.get("salary_type_edit"))

        # EmployeeReferrals.com
        self.enter_richtext_integer(self.referral_bonus, JobData.job_data.get("referral_bonus_edit"))
        self.click_radio_yes_no(self.hot_job, JobData.job_data.get("hot_job_edit"))

        # Description/Skills
        self.enter_richtext(self.required_skills, JobData.job_data.get("required_skills_edit"))
        self.enter_richtext(self.required_experience, JobData.job_data.get("required_experience_edit"))

        # Custom Fields
        self.enter_text(self.job_grade, JobData.job_data.get("job_grade_edit"))
        self.select_from_dropdown(self.collect_eeo_for_this_job, JobData.job_data.get("collect_eeo_for_this_job_edit"))

        self.go_click(self.save_btn)

        return

    def edit_job_posting_status(self, posting_status):
        self.select_from_dropdown(self.posting_status, posting_status)
        self.go_click(self.save_btn)

        return

    def edit_job_title_clone(self):
        self.enter_text(self.internal_job_title, JobData.job_data.get("internal_job_title_clone"))
        self.enter_text(self.posted_job_title, JobData.job_data.get("posted_job_title_clone"))
        self.go_click(self.save_btn)

        return

from common.common import Common
from selenium.webdriver.common.by import By
from test_data.test_data_details import JobData
import datetime


class Elements:
    header = (By.CLASS_NAME, 'appListRowDisplayOdd')
    posted_job_title = (By.ID, 'postedJobTitleColonLabelValue')
    internal_job_title = (By.ID, "internalJobTitleColonLabelValue")
    tracking_code = (By.ID, 'trackingCodeColonLabelValue')
    hiring_workflow = (By.ID, 'hiringWorkflowColonLabelValue')
    evergreen_job = [By.ID, 'evergreenJobColonLabelValue']
    job_category = (By.ID, "jobCategoryColonLabelValue")
    job_template = (By.ID, "jobTemplateColonLabelValue")
    eeoc_job_category = (By.ID, "eEOCJobCategoryColonLabelValue")
    status = (By.ID, 'jobStatusColonLabelValue')
    number_of_positions = (By.ID, "numberofPositionsColonLabelValue")
    number_of_positions_filled = (By.ID, "numberofPositionsFilledColonLabelValue")
    job_id = (By.ID, "jobIdColonLabelValue")
    job_description = (By.ID, "jobDescriptionColonLabelValue")
    required_skills = (By.ID, "requiredSkillsColonLabelValue")
    job_location_code = (By.ID, "jobLocationCodeColonLabelValue")
    job_location = (By.ID, "jobLocationColonLabelValue")
    additional_locations = (By.ID, "additionalLocationsValue")
    position_type = (By.ID, 'positionTypeLabelValue')
    posted_date = (By.ID, "postingDateColonLabelValue")
    original_posting_date = (By.ID, "originalPostedDateColonLabelValue")
    required_experience = (By.ID, "requiredExperienceColonLabelValue")
    years_of_experience = (By.ID, "yearsOfExperienceColonLabelValue")
    level_of_education = (By.ID, "levelofEducationColonLabelValue")
    starting_date = (By.ID, 'startingDateColonLabelValue')
    job_duration = (By.ID, 'jobDurationColonLabelValue')
    per_diem_included = [By.ID, "perDiemIncludedColonLabelValue"]
    salary_type = (By.ID, "salaryTypeColonLabelValue")
    salary_currency = (By.ID, "salaryCurrencyColonLabelValue")
    minimum_salary = (By.ID, "minimumSalaryColonLabelValue")
    maximum_salary = (By.ID, "maximumSalaryColonLabelValue")
    travel = (By.ID, "travelColonLabelValue")
    list_on_employeeReferralscom = [By.ID, "listOnEmployeeReferralsLabelValue"]
    referral_bonus = (By.ID, 'referralBonusLabelValue')
    referral_points = (By.ID, 'referralPointsLabelValue')
    keywords = (By.ID, 'keywordsLabelValue')
    negative_keywords = (By.ID, 'negativeKeywordsLabelValue')
    hot_job = [By.ID, 'hotJobLabelValue']
    assigned_recruiter = (By.ID, 'assignedRecruiterColonLabelValue')
    recruiting_manager = (By.ID, "recruitingManagerColonLabelValue")
    hiring_manager = (By.ID, "hiringManagerColonLabelValue")
    recruiting_team = (By.ID, "recruitingTeamValue")
    business_unit = (By.ID, "businessUnitColonLabelValue")
    department = (By.ID, "departmentDivisionLabelValue")
    business_function = (By.ID, "businessFunctionColonLabelValue")
    industry = (By.ID, "industryColonLabelValue")
    budgeted_currency = (By.ID, "budgetCurrencyColonLabelValue")
    budgeted_salary = (By.ID, "budgetedSalaryColonLabelValue")
    budgeted_quarter = (By.ID, "budgetedQuarterColonLabelValue")
    talent_assessment = (By.ID, 'talentAssessmentColonLabelValue')
    do_not_display_assessment_on_job_portal = (By.ID, 'recruiterInitiatedAssessmentValue')
    internal_notes = (By.ID, "")
    internal_skills = (By.ID, "")
    add_note = (By.ID, 'jobInternalNotes')
    add_note_btn = (By.ID, 'saveInternalNotes')

    cancel_btn = (By.ID, 'returnButton')


class JobPositionDetailsView(Common, Elements):
    def __init__(self, driver):
        super().__init__(driver)

    def verify_header(self):
        elm = self.driver.find_element_by_locator(self.header)
        elms = elm.find_elements(By.CLASS_NAME, "jobPostingDetailsTD")
        for elm in elms:
            if elm.text == JobData.job_data.get("assigned_recruiter"):
                self.sr_logger.logger.info("-- Verified assigned recruiter.")
                continue
            elif elm.text == JobData.job_data.get("hiring_manager"):
                self.sr_logger.logger.info("-- Verified hiring manager.")
                continue
            elif elm.text == JobData.job_data.get("status"):
                self.sr_logger.logger.info("-- Verified posting status.")
                continue
        return

    def verify_all_fields(self):
        self.__comparing(self.driver.find_element_by_locator(self.posted_job_title).text,
                         JobData.job_data.get("posted_job_title"))
        self.__comparing(self.driver.find_element_by_locator(self.internal_job_title).text,
                         JobData.job_data.get("internal_job_title"))
        self.__comparing(self.driver.find_element_by_locator(self.tracking_code).text,
                         JobData.job_data.get("tracking_code"))
        self.__comparing(self.driver.find_element_by_locator(self.hiring_workflow).text,
                         JobData.job_data.get("hiring_workflow"))
        self.__comparing(self.driver.find_element_by_locator(self.evergreen_job).text,
                         JobData.job_data.get("evergreen_job"))
        self.__comparing(self.driver.find_element_by_locator(self.job_category).text,
                         JobData.job_data.get("category_radio_list"))
        self.__comparing(self.driver.find_element_by_locator(self.eeoc_job_category).text,
                         JobData.job_data.get("eeo1_job_category"))
        self.__comparing(self.driver.find_element_by_locator(self.status).text, JobData.job_data.get("status"))
        self.__comparing(self.driver.find_element_by_locator(self.number_of_positions).text,
                         JobData.job_data.get("number_of_positions"))
        self.__comparing(self.driver.find_element_by_locator(self.number_of_positions_filled).text, 0)
        self.__comparing(self.driver.find_element_by_locator(self.job_description).text,
                         JobData.job_data.get("job_description"))
        self.__comparing(self.driver.find_element_by_locator(self.required_skills).text,
                         JobData.job_data.get("required_skills"))
        self.__comparing(self.driver.find_element_by_locator(self.job_location).text,
                         JobData.job_data.get("city"))
        self.__comparing(self.driver.find_element_by_locator(self.additional_locations).text,
                         JobData.job_data.get("additional_locations"))
        self.__comparing(self.driver.find_element_by_locator(self.position_type).text,
                         JobData.job_data.get("position_type"))
        today = datetime.datetime.today().strftime("%#m/%#d/%y")
        self.__comparing(self.driver.find_element_by_locator(self.posted_date).text, today)
        self.__comparing(self.driver.find_element_by_locator(self.original_posting_date).text, today)
        self.__comparing(self.driver.find_element_by_locator(self.required_experience).text,
                         JobData.job_data.get("required_experience"))
        self.__comparing(self.driver.find_element_by_locator(self.years_of_experience).text,
                         JobData.job_data.get("years_of_experience"))
        self.__comparing(self.driver.find_element_by_locator(self.level_of_education).text,
                         JobData.job_data.get("level_of_education"))
        self.__comparing(self.driver.find_element_by_locator(self.starting_date).text,
                         JobData.job_data.get("expected_start_date"))
        self.__comparing(self.driver.find_element_by_locator(self.job_duration).text,
                         JobData.job_data.get("job_duration"))
        self.__comparing(self.driver.find_element_by_locator(self.per_diem_included).text,
                         JobData.job_data.get("per_diem_included"))
        self.__comparing(self.driver.find_element_by_locator(self.salary_type).text,
                         JobData.job_data.get("salary_type"))
        self.__comparing(self.driver.find_element_by_locator(self.salary_currency).text,
                         JobData.job_data.get("salary_currency"))
        self.__comparing(self.driver.find_element_by_locator(self.minimum_salary).text,
                         JobData.job_data.get("minimum_salary"))
        self.__comparing(self.driver.find_element_by_locator(self.maximum_salary).text,
                         JobData.job_data.get("maximum_salary"))
        self.__comparing(self.driver.find_element_by_locator(self.travel).text,
                         JobData.job_data.get("travel"))
        self.__comparing(self.driver.find_element_by_locator(self.list_on_employeeReferralscom).text,
                         JobData.job_data.get("list_on_employeeReferralscom"))
        self.__comparing(self.driver.find_element_by_locator(self.referral_bonus).text,
                         JobData.job_data.get("referral_bonus"))
        self.__comparing(self.driver.find_element_by_locator(self.referral_points).text,
                         JobData.job_data.get("referral_points"))
        self.__comparing(self.driver.find_element_by_locator(self.keywords).text,
                         JobData.job_data.get("keywords"))
        self.__comparing(self.driver.find_element_by_locator(self.negative_keywords).text,
                         JobData.job_data.get("negative_keywords"))
        self.__comparing(self.driver.find_element_by_locator(self.hot_job).text,
                         JobData.job_data.get("hot_job"))
        self.__comparing(self.driver.find_element_by_locator(self.assigned_recruiter).text,
                         JobData.job_data.get("assigned_recruiter"))
        self.__comparing(self.driver.find_element_by_locator(self.hiring_manager).text,
                         JobData.job_data.get("hiring_manager"))
        self.__comparing(self.driver.find_element_by_locator(self.business_unit).text,
                         JobData.job_data.get("business_unit"))
        self.__comparing(self.driver.find_element_by_locator(self.department).text,
                         JobData.job_data.get("department"))
        self.__comparing(self.driver.find_element_by_locator(self.business_function).text,
                         JobData.job_data.get("business_function"))
        self.__comparing(self.driver.find_element_by_locator(self.industry).text,
                         JobData.job_data.get("industry"))
        self.__comparing(self.driver.find_element_by_locator(self.budgeted_currency).text,
                         JobData.job_data.get("budgeted_currency"))
        self.__comparing(self.driver.find_element_by_locator(self.budgeted_salary).text,
                         JobData.job_data.get("budgeted_salary"))
        self.__comparing(self.driver.find_element_by_locator(self.budgeted_quarter).text,
                         JobData.job_data.get("budgeted_quarter"))
        # self.__comparing(self.driver.find_element_by_locator(self.talent_assessment).text,
        #                  JobData.job_data.get("talent_assessment"))
        # self.__comparing(self.driver.find_element_by_locator(self.do_not_display_assessment_on_job_portal).text,
        #                  JobData.job_data.get("do_not_display_assessment_on_job_portal"))

        self.enter_text(self.add_note, JobData.job_data.get("add_note"))
        # self.go_click(self.add_note_btn)    # TODO: not correct

        # self.driver.find_element_by_locator((By.LINK_TEXT, "CX Link")).click()

        self.go_click(self.cancel_btn)

        return

    def verify_posting_status(self, job_status):
        self.__comparing(self.driver.find_element_by_locator(self.status).text, job_status)

    def verify_from_temp(self):
        self.__comparing(self.driver.find_element_by_locator(self.internal_job_title).text,
                         JobData.job_data.get("internal_job_title_temp"))
        self.__comparing(self.driver.find_element_by_locator(self.job_template).text,
                         JobData.job_data.get("job_template"))
        self.__comparing(self.driver.find_element_by_locator(self.job_location_code).text,
                         JobData.job_data.get("job_location_code_temp"))
        self.__comparing(self.driver.find_element_by_locator(self.hiring_workflow).text,
                         JobData.job_data.get("hiring_workflow_temp"))
        self.__comparing(self.driver.find_element_by_locator(self.eeoc_job_category).text,
                         JobData.job_data.get("eeo1_job_category_temp"))
        # ToDo: bug: RND-7374
        # self.__comparing(self.driver.find_element_by_locator(self.industry).text,
        #                  JobData.job_data.get("industry_temp"))
        # self.__comparing(self.driver.find_element_by_locator(self.department).text,
        #                  JobData.job_data.get("department_temp"))
        # self.__comparing(self.driver.find_element_by_locator(self.business_function).text,
        #                  JobData.job_data.get("business_function_temp"))
        # self.__comparing(self.driver.find_element_by_locator(self.job_duration).text,
        #                  JobData.job_data.get("job_duration_temp"))
        self.__comparing(self.driver.find_element_by_locator(self.position_type).text,
                         JobData.job_data.get("position_type_temp"))
        self.__comparing(self.driver.find_element_by_locator(self.years_of_experience).text,
                         JobData.job_data.get("years_of_experience_temp"))
        self.__comparing(self.driver.find_element_by_locator(self.level_of_education).text,
                         JobData.job_data.get("level_of_education_temp"))
        self.__comparing(self.driver.find_element_by_locator(self.per_diem_included).text,
                         JobData.job_data.get("per_diem_included_temp"))
        self.__comparing(self.driver.find_element_by_locator(self.travel).text,
                         JobData.job_data.get("travel_temp"))
        self.__comparing(self.driver.find_element_by_locator(self.salary_type).text,
                         JobData.job_data.get("salary_type_temp"))
        self.__comparing(self.driver.find_element_by_locator(self.maximum_salary).text,
                         JobData.job_data.get("maximum_salary_temp"))
        self.__comparing(self.driver.find_element_by_locator(self.minimum_salary).text,
                         JobData.job_data.get("minimum_salary_temp"))

    def verify_remote_country(self, job_location):
        job_loc = self.get_text(self.job_location)
        self.__comparing(job_loc, job_location)
        return

    def __comparing(self, source, target):
        if target is True:
            target = "Yes"
        target = str(target)
        if source == target:
            self.sr_logger.logger.info(f"-- {source} is correct")
            assert source == target
        elif target in source:
            self.sr_logger.logger.info(f"-- {source} is correct")
            assert target in source
        elif source in target:
            self.sr_logger.logger.info(f"-- {source} is correct")
            assert source in target
        else:
            self.sr_logger.logger.error(f"@@ {source} is NOT correct")
            # raise Exception(f"{source} is NOT correct")

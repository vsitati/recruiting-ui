import pytest
import allure
from cx_pages.career_sites import CareerSites
from cx_pages.jobs_search import JobSearch
from cx_pages.login import Login
from cx_pages.base import BasePage


@pytest.mark.usefixtures("setup")
class TestCandidateExperience:
    @allure.title("CX Example Tests")
    @allure.description("Get Page Title")
    def test_get_page_title(self, get_test_info):
        login = Login(driver=self.driver)
        login.do_login(env_info=get_test_info)

        basepage = BasePage(self.driver)
        assert basepage.get_title() == "Career Sites - QA Automation Only"

    @allure.description("Navigate to a Job Search Page for a given Job Portal")
    def test_go_to_job_search_page(self, get_test_info):
        login = Login(driver=self.driver)
        login.do_login(env_info=get_test_info)

        cs = CareerSites(driver=self.driver)
        data = cs.get_career_sites(site_section="external")
        result = cs.filter_career_site(data=data, site_name="Corporate Career Portal - Indeed Apply")
        name, portal, settings = result
        cs.open_url(portal)
        assert cs.get_title() == "IzWNco KGme SXqHaSGYF XxUZVhtg ISnQN - zrKhMUy VfaqafzMu HJDjVKrGF gy CLn ce PkyxIlRrp zs"

        js = JobSearch(driver=self.driver)
        job_elem = js.find_job(title="Lab Technician (T05-NE) - AWabHyVZV")
        js.open_job(job_elem=job_elem)
        assert "Lab Technician (T05-NE)" in js.get_title()

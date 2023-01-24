import allure
import pytest
from allure_commons.types import AttachmentType
from utils.drivers import Drivers
from config import Config


def pytest_addoption(parser):
    parser.addoption("--company", action="store", default="qaautomationonly", help="Company name")
    parser.addoption("--user_role", action="store", default="rm", help="User Role")
    parser.addoption("--ats", action="store", default="ats_login", help="Choices for ATS: ['ats.ats_login', "
                                                                        "'ats.admin'(openadmin)]")
    parser.addoption("--cx", action="store", default="admin", help="cx.admin(admin page)")
    parser.addoption("--browser_language", action="store", default="english", help="Choices for Browser Language: "
                                                                                   "english, french, german, spanish")


@pytest.fixture(scope='session')
def get_test_info(request):
    return dict(
        company=request.config.getoption("--company"),
        user_role=request.config.getoption("--user_role"),
        ats=request.config.getoption("--ats"),
        cx=request.config.getoption("--cx"),
    )


def pytest_collection_modifyitems(config, items):
    keyword_expr = config.option.keyword
    mark_expr = config.option.markexpr
    if keyword_expr or mark_expr:
        return

    skip_marker = pytest.mark.skip(reason='smoke not selected')
    for item in items:
        if 'smoke' in item.keywords:
            item.add_marker(skip_marker)


@pytest.fixture()
def setup(request):
    config = Config.env_config
    driver = Drivers.get_driver(config, request.config.getoption("--browser_language"))
    driver.implicitly_wait(config["timeout"])
    request.cls.driver = driver
    before_failed = request.session.testsfailed
    if config["browser"] == "firefox":
        driver.maximize_window()
    yield

    if request.session.testsfailed != before_failed:
        allure.attach(driver.get_screenshot_as_png(),
                      name=request.function.__name__,
                      attachment_type=AttachmentType.PNG)
    driver.quit()

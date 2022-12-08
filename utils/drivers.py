from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from helpers.webdriver_extended import WebDriverExtended
from helpers.webdriver_listener import WebDriverListener


class Drivers:
    @staticmethod
    def get_driver(config, language):
        if config["browser"] == "chrome":
            options = webdriver.ChromeOptions()
            # Removes descriptor ERROR in logs: https://github.com/SeleniumHQ/selenium/issues/10225
            options.add_experimental_option('excludeSwitches', ['enable-logging'])
            options.add_argument("start-maximized")
            if language == "english":
                options.add_argument("--lang=en")
            elif language == "french":
                options.add_argument("--lang=fr")
            elif language == "german":
                options.add_argument("--lang=de")
            elif language == "spanish":
                options.add_argument("--lang=es")
            if config["headless_mode"] is True:
                options.add_argument("--headless")
            driver = WebDriverExtended(
                webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options),
                WebDriverListener()
            )
            return driver
        elif config["browser"] == "firefox":
            options = webdriver.FirefoxOptions()
            if config["headless_mode"] is True:
                options.headless = True
            driver = WebDriverExtended(
                webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=options),
                WebDriverListener()
            )
            return driver
        raise Exception("Provide valid driver name")

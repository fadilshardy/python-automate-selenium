import chromedriver_autoinstaller
import os

from dataclasses import dataclass
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from subprocess import CREATE_NO_WINDOW
from core import path

from modules.browser.driverOptions import DriverOptions


@dataclass
class Driver:
    """
    Represents Webdriver class.
    """

    driver_options: object = DriverOptions().options
    resource_path: str = path.get_resource_path()

    def check_webdriver(self) -> None:
        """
        check if webdriver is available and updated to the latest version, if not then update the driver

        :return: None
        """

        chromedriver_autoinstaller.install(path=self.resource_path)

    def get_webdriver_path(self) -> str:
        """
        check and get the matched driver version path installed on user's machine

        :return: matched driver version path
        """

        chrome_version = chromedriver_autoinstaller.get_chrome_version()

        chromedriver_version = chromedriver_autoinstaller.utils.get_matched_chromedriver_version(
            chrome_version)

        major_version = chromedriver_autoinstaller.utils.get_major_version(
            chromedriver_version)

        driver_path = os.path.join(
            self.resource_path, major_version, 'chromedriver.exe')

        return driver_path

    def get_driver(self) -> webdriver:
        """
        initiate the webdriver and return the instance.

        :return: webdriver instance
        """

        self.check_webdriver()

        chrome_service = ChromeService(self.get_webdriver_path())

        chrome_service.creationflags = CREATE_NO_WINDOW

        webdriver.DesiredCapabilities.CHROME['acceptSslCerts'] = True
        driverInstance = webdriver.Chrome(
            service=chrome_service, options=self.driver_options)
        driverInstance.execute_script(
            "Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
        driverInstance.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
            "source":
                "const newProto = navigator.__proto__;"
                "delete newProto.webdriver;"
                "navigator.__proto__ = newProto;"
        })

        return driverInstance

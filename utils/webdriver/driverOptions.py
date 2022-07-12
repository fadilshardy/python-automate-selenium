from selenium.webdriver import ChromeOptions


class DriverOptions():

    def __init__(self):
        self.options = ChromeOptions()
        self.options.page_load_strategy = 'normal'
        self.options.add_argument('--no-sandbox')
        self.options.add_argument('--start-maximized')
        self.options.add_argument('--disable-dev-shm-usage')
        self.options.add_argument("--incognito")
        self.options.add_argument(
            '--disable-blink-features=AutomationControlled')
        self.options.add_experimental_option('useAutomationExtension', False)
        self.options.add_experimental_option(
            "excludeSwitches", ["enable-automation", 'enable-logging'])
        self.options.add_argument("disable-infobars")
        self.options.add_experimental_option("detach", True)

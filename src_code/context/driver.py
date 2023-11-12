from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from appium import webdriver as appium_wd
from context.config import settings


class Driver(object):
    class SeleniumDriverNotFound(Exception):
        pass

    def __init__(self, tag_browser=settings.default_browser):
        if settings.execute_in_grid:
            cloud_url = settings.grid_uri
            if tag_browser == "chrome":
                options = ChromeOptions()
                cloud_options = {}
                options.set_capability('cloud:options', cloud_options)
                self.driver = webdriver.Remote(cloud_url, options=options)
            elif tag_browser == "firefox":
                options = FirefoxOptions()
                cloud_options = {}
                options.set_capability('cloud:options', cloud_options)
                self.driver = webdriver.Remote(cloud_url, options=options)
            else:
                raise SeleniumDriverNotFound(
                    f"{settings.browser} not currently supported")
        else:
            if tag_browser == "chrome":
                self.driver = webdriver.Chrome()
                self.driver.maximize_window()
            elif tag_browser == "firefox":
                self.driver = webdriver.Firefox()
                self.driver.maximize_window()
            else:
                raise SeleniumDriverNotFound(
                    f"{settings.browser} not currently supported")

    def get_driver(self):
        return self.driver

    def stop_driver(self):
        self.driver.quit()

    def clear_cookies(self):
        self.driver.delete_all_cookies()

    def navigate(self, url):
        self.driver.get(url)


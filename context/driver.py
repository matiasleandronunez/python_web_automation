from selenium import webdriver
from context.config import settings


class Driver(object):
    instance = None

    class SeleniumDriverNotFound(Exception):
        pass

    @classmethod
    def get_instance(cls):
        if not cls.instance:
            cls.instance = Driver()
        return cls.instance

    def __init__(self, tag_browser=None):

        if tag_browser:
            if tag_browser == "chrome":
                self.driver = webdriver.Chrome()
                self.driver.maximize_window()
        else:
            if settings.default_browser == "chrome":
                self.driver = webdriver.Chrome()
                self.driver.maximize_window()
            elif settings.default_browser == "firefox":
                self.driver = webdriver.Firefox()
            else:
                raise SeleniumDriverNotFound(
                    f"{settings.browser} not currently supported")

    def get_driver(self):
        return self.driver

    def stop_instance(self):
        self.driver.quit()
        instance = None

    def clear_cookies(self):
        self.driver.delete_all_cookies()

    def navigate(self, url):
        self.driver.get(url)


driver = Driver.get_instance()

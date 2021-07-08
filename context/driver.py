from selenium import webdriver
from context.config import settings


class Driver(object):
    class SeleniumDriverNotFound(Exception):
        pass

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

    def stop_driver(self):
        self.driver.quit()

    def clear_cookies(self):
        self.driver.delete_all_cookies()

    def navigate(self, url):
        self.driver.get(url)


#driver = Driver.get_instance()

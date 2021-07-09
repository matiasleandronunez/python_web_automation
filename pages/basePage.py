from context.config import settings
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from abc import abstractmethod


class Locator:
    def __init__(self, l_type, selector):
        self.l_type = l_type
        self.selector = selector

    def parameterize(self, *args):
        self.selector = self.selector.format(*args)


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @abstractmethod
    def _validate_page(self):
        return

    def open_url(self, url):
        self.driver.get(url)

    def _execute_with_wait(self, condition):
        return WebDriverWait(self.driver.get_driver(), settings.driver_timeout).until(condition)

    def element_exists(self, locator):
        try:
            self._execute_with_wait(
                ec.presence_of_element_located(
                    (locator.l_type, locator.selector))
            )
            return True
        except TimeoutException:
            return False

    def get_element(self, locator):
        if not self.element_exists(locator):
            raise NoSuchElementException(f"Could not find {locator.selector}")

        return self.driver.get_driver().find_element(locator.l_type, locator.selector)

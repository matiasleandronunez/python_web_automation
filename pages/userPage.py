import string
import random

from model.Customer import Customer
from pages.basePage import BasePage, Locator
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class UserPage(BasePage):
    instance = None
    _CREATE_USER_ID = Locator(By.NAME, "username")
    _CREATE_PASS_ID = Locator(By.NAME, "password")
    _CREATE_SIGNUP_BUTTON = Locator(By.CSS_SELECTOR, "div.createFormButton > button")
    _SUCCESS_MESSAGE = Locator(By.CSS_SELECTOR, "div.successMessage")

    def __init__(self, driver):
        super().__init__(driver)

    def create_random_user(self):
        user = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(8))
        password = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(8))

        self.get_element(self._CREATE_USER_ID).send_keys(user)
        self.get_element(self._CREATE_PASS_ID).send_keys(password)
        self.get_element(self._CREATE_SIGNUP_BUTTON).click()

        return Customer(username=user, password=password)

    def is_success_message_displayed(self):
        return self.get_element(self._SUCCESS_MESSAGE).text == "Congratulations! Your account has been created!"


from context.driver import driver
from helpers import apihelper
from helpers.custom_exceptions import RequestUnexpected


def after_all(context):
    driver.stop_instance()

def before_scenario(context, scenario):
    driver.clear_cookies()

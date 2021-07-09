from context import driver
from helpers import apihelper
from helpers.custom_exceptions import RequestUnexpected
from pages.storefrontPage import StorefrontPage
from pages.checkoutPage import CheckoutPage
from pages.userPage import UserPage

def after_scenario(context, scenario):
    context.driver.stop_driver()

def before_scenario(context, scenario):
    b = [i for i in scenario.tags if i.startswith('Browser:')]

    if b:
        d = driver.Driver(tag_browser=b)
        context.driver = d
    else:
        d = driver.Driver()
        context.driver = d

    context.driver.clear_cookies()

    # Intantiate pages into context for use within the test
    context.checkout_page = CheckoutPage(context.driver)
    context.storefront_page = StorefrontPage(context.driver)
    context.user_create_page = UserPage(context.driver)


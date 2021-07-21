from context import driver
from helpers import apihelper
from helpers.custom_exceptions import RequestUnexpected, RequestReturnedNonOK
from model.Customer import Customer
from pages.storefrontPage import StorefrontPage
from pages.checkoutPage import CheckoutPage
from pages.userPage import UserPage


def before_feature(context, feature):
    if 'api_feature' in feature.tags:
        # Create customer for update API scenario
        try:
            context.existing_customer = Customer()
            apihelper.post_customer(context.existing_customer)

            context.to_update = apihelper.post_customer(Customer())

            context.to_delete = apihelper.post_customer(Customer())
        except (RequestUnexpected):
            raise KeyboardInterrupt("Error creating data, execution aborted")


def before_scenario(context, scenario):
    b = [i for i in context.scenario.tags if i.startswith('Browser:')]

    if b:
        d = driver.Driver(tag_browser=b.pop().split(':', 1)[1])
        context.driver = d
    elif 'no_ui' in context.scenario.tags or 'no_ui' in context.feature.tags:
        #No need for pages nor driver if tests are not UI driven
        return
    else:
        d = driver.Driver()
        context.driver = d

    context.driver.clear_cookies()

    # Instantiate pages into context for use within the test
    context.checkout_page = CheckoutPage(context.driver)
    context.storefront_page = StorefrontPage(context.driver)
    context.user_create_page = UserPage(context.driver)

def after_scenario(context, scenario):
    if 'no_ui' in scenario.tags or 'no_ui' in context.feature.tags:
        return
    else:
        context.driver.stop_driver()

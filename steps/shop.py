from behave import given, when, then
from behave import matchers
matchers.use_step_matcher("re")
from context.config import settings
from context.driver import driver
from pages.storefrontPage import storefront_page
from pages.checkoutPage import checkout_page

@given(u'I go to the storefront')
def go_to_sf(context):
    driver.navigate(settings.url)

@when('I click on add (\d+) times for (.*)')
def step_impl(context, times, tile_title):
    storefront_page.add_to_cart_by_item_name(tile_title, int(times))


@when(u'I proceed to checkout')
def step_impl(context):
    storefront_page.checkout_cart()


@then(u'I verify (.*) was added to the cart (\d+) times')
def step_impl(context, tile_title, times):
    assert checkout_page.get_cart_items()[tile_title] == int(times), f"expected {tile_title} to be added {times}, was {checkout_page.get_cart_items()[tile_title]}"


@then(u'I verify subtotal equals (\d+) by (\d+)')
def step_impl(context, price, quantity):
    assert int(price) * int(quantity) == checkout_page.get_subtotal()


@then(u'I verify taxes amount \$1.50 by (\d+)')
def step_impl(context, quantity):
    assert 1.5 * int(quantity) == checkout_page.get_taxes()
from behave import given, when, then
from behave import matchers
from helpers import apihelper

matchers.use_step_matcher("re")
from context.config import settings


@given(u'I go to the storefront')
def go_to_sf(context):
    context.driver.navigate(settings.url)

@when('I click on add (\d+) times for (.*)')
def step_impl(context, times, tile_title):
    context.storefront_page.add_to_cart_by_item_name(tile_title, int(times))


@when(u'I proceed to checkout')
def step_impl(context):
    context.storefront_page.checkout_cart()


@then(u'I verify (.*) was added to the cart (\d+) times')
def step_impl(context, tile_title, times):
    assert context.checkout_page.get_cart_items()[tile_title] == int(times), f"expected {tile_title} to be added {times}, was {context.checkout_page.get_cart_items()[tile_title]}"


@then(u'I verify subtotal equals (\d+) by (\d+)')
def step_impl(context, price, quantity):
    assert int(price) * int(quantity) == context.checkout_page.get_subtotal()


@then(u'I verify taxes amount \$1.50 by (\d+)')
def step_impl(context, quantity):
    assert 1.5 * int(quantity) == context.checkout_page.get_taxes()


@then(u'I verify all items are displayed')
def step_impl(context):
    assert len(apihelper.get_all_products()) == context.storefront_page.displayed_cards_count()


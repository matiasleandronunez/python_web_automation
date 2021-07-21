from behave import given, when, then
from behave import matchers
matchers.use_step_matcher("re")
from helpers import apihelper
from helpers.custom_exceptions import *


@given(u'I post an existing customer to the customer create endpoint')
def step_impl(context):
    try:
        apihelper.post_customer(context.existing_customer)
    except RequestUnexpected as e:
        context.exc = e


@then(u'I verify I get a conflict response from the API')
def step_impl(context):
    assert context.exc is not None
    assert isinstance(context.exc, RequestReturnedConflict)


@given(u'I delete a customer to the customer delete endpoint')
def step_impl(context):
    context.response_httpcode = apihelper.delete_customer(context.to_delete)


@then(u'I verify I get a no content response from the API')
def step_impl(context):
    assert context.response_httpcode == 204


@given(u'I post a new customer to the customer create endpoint')
def step_impl(context):
    context.response_id = apihelper.post_customer()


@then(u'I verify I get the customer ID from the API response')
def step_impl(context):
    assert int(context.response_id) > 0


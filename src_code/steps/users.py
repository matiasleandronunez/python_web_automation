from behave import given, when, then
from behave import matchers
matchers.use_step_matcher("re")
from context.config import settings
from helpers import apihelper


@when(u'I go to the user creation screen')
def step_impl(context):
    context.storefront_page.create_user_link()


@when(u'I sign up a new user')
def step_impl(context):
    context.user = context.user_create_page.create_random_user()


@then(u'I verify the new user account was created')
def step_impl(context):
    assert context.user_create_page.is_success_message_displayed(), "Expected user creation success message to be displayed"
    assert apihelper.get_login_token(context.user).status_code == 200
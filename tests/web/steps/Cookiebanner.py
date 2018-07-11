from behave import given, when, then
from tests.pageobjects.cookiebanner import cookiebannerPageObject
from nose.tools import assert_in, assert_equal, assert_true, assert_false

@given('goto page')
def step_impl(context):
    context.current_page = cookiebannerPageObject()
    context.current_page.open().waitToDrawHome()

@then ('cookie banner present')
def step_impl(context):
    context.current_page.cookieTitlePresent()
    context.current_page.cookieTextPresent()
    context.current_page.cookieButtonsPresent()

@then ('click on accept')
def step_impl(context):
    context.current_page.acceptCookieButton()

@then('cookie banner disappears')
def step_impl(context):
    context.current_page.cookieTitleNotVisible()
    context.current_page.cookieTextNotVisible()
    context.current_page.cookieButtonsNotVisible()


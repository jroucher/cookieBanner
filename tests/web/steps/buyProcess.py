from behave import given, when, then
from tests.pageobjects.buyProcess import BuyProcessPageObject
from nose.tools import assert_in, assert_equal, assert_true, assert_false

@given('goto page')
def step_impl(context):
	context.current_page = BuyProcessPageObject()
	context.current_page.open().waitToDrawHome().setElements()
	
@given ('add item to shopping cart')
def step_impl(context):
	context.current_page.addItemToCart().waitToDrawHome()

@then ('go to shopping cart')
def step_impl(context):
	context.current_page.goToCart().waitToDrawCart()
 
@then ('at least one item is present')
def step_impl(context):
	context.current_page.itemPresent()
	
# /* ------------------------------------------------- */


@then ('Proceed to checkout')
def step_impl(context):
	context.current_page.checkout().waitToDrawCheckout()
	
@then ('Complete the form and go next')
def step_impl(context):
    context.current_page.typeForm().waitToDrawPay()

@then ('Select payment method and complete payment')
def step_impl(context):
	context.current_page.pay().waitToDrawSomeMoreData()
	context.current_page.MoreData()
	
# /* ------------------------------------------------- */

from behave import *
from compare import expect

use_step_matcher("re")

@then('I log out Automation Practice')
def step_impl(context):
    context.su.clickElement(context.HeaderFooter.sign_out)

@then('I click My Account')
def step_impl(context):
    context.su.clickElement(context.HeaderFooter.my_account)
    actualTextmyaccountWelcome = context.su.getTextWebElement(context.MyAccount.myaccountWelcome);
    print("Found actualTextmyaccountWelcome: %s \n" % actualTextmyaccountWelcome)
    expect(actualTextmyaccountWelcome.lower()).to_contain('Welcome to your account'.lower())

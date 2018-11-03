from behave import *
from compare import expect

use_step_matcher("re")

@then('I log out Automation Practice')
def step_impl(context):
    context.su.click_element(context.HeaderFooter.sign_out)

@then('I click My Account')
def step_impl(context):
    context.su.click_element(context.HeaderFooter.my_account)
    actualTextmyaccountWelcome = context.su.get_text_web_element(context.MyAccount.myaccountWelcome)
    expect(actualTextmyaccountWelcome.lower()).to_contain('Welcome to your account'.lower())

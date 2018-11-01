from behave import *
from compare import expect

use_step_matcher("re")

@given('I log out Automation Practice')
def step_impl(context):
    context.su.clickElement(context.HeaderFooter.sign_out)

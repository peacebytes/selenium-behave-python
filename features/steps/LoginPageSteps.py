from behave import *
from compare import expect

use_step_matcher("re")

@step('I have logged into Automation Practice')
def step_impl(context):
    context.su.visit(context.host)
    context.su.clickElement(context.HeaderFooter.sign_in)
    context.LoginPage.login(username=context.user,passwd=context.passwd)

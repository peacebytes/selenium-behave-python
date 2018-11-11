from behave import *

use_step_matcher("re")

@step('I have logged into Automation Practice')
def step_impl(context):
    context.su.visit(context.host)
    context.su.click_element(context.HeaderFooter.sign_ins)
    context.LoginPage.login(username=context.user,passwd=context.passwd)

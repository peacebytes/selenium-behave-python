from behave import *
from features.lib.pages import *
from compare import expect

use_step_matcher("re")

@step('I login automationpractice website')
def step_impl(context):
    page = LoginPage(context)
    page.login(username=context.user,passwd=context.passwd)

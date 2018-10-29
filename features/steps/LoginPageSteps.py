from behave import *
from features.lib.pages import *
from compare import expect

use_step_matcher("re")

@step('I login with username "([^"]*)" and password "([^"]*)"')
def step_impl(context,username,password):
    page = LoginPage(context)
    page.login(username=username,passwd=password)

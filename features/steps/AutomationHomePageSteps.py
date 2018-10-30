from behave import *
from features.lib.pages import *
from compare import expect

use_step_matcher("re")


@when('I open automationpractice website "([^"]*)"')
def step_impl(context, aut_site):
    page = AutomationHomePage(context)
    page.visit(aut_site)
    page.sign_in.click()

@when('I open automationpractice website')
def step_impl(context):
    page = AutomationHomePage(context)
    page.visit(context.host)
    page.sign_in.click()

@then("I verify that I successfully logged in by logging out")
def step_impl(context):
    AutomationHomePage(context).sign_out.click()

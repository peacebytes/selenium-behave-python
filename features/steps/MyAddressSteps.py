from behave import *
from compare import expect
import time
use_step_matcher("re")

@then('I add all addressses from test data')
def step_impl(context):
    for addr in context.testdata['addresses']:
        context.MyAddress.addAddress(addr)

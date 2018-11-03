from behave import *
from compare import ensure

use_step_matcher("re")

@then('I add all addressses from test data')
def step_impl(context):
    for addr in context.testdata['addresses']:
        if context.MyAddress.add_address(addr) is True:
            #Asserting adding is complete
            ensure(context.MyAddress.is_address_existed(addr['alias']) == True, True, "Fail to add new address %s" % addr['alias'])

@then('I update address "([^"]*)"')
def step_impl(context, address_name):
    new_address_alias = context.MyAddress.update_address(address_name)
    if new_address_alias is not None:
        #Asserting update is complete
        ensure(context.MyAddress.is_address_existed(new_address_alias) == True, True)
        ensure(context.MyAddress.is_address_existed(address_name) == False, True, "Fail to update address %s" % address_name)

@then('I delete address "([^"]*)"')
def step_impl(context, address_name):
    if context.MyAddress.delete_address(address_name) is True:
        #Asserting delete is completes
        ensure(context.MyAddress.is_address_existed(address_name) == False, True, "Fail to delete address %s" % address_name)


from behave import *
from compare import expect

use_step_matcher("re")

@then('I click on "([^"]*)"')
def step_impl(context, optionToClick):
    for webEle in context.MyAccount.myaccountLinkList:
        actualTextmyaccountLink = context.su.getTextWebElement(webEle)
        if (actualTextmyaccountLink.lower()==(optionToClick.lower())):
            context.su.clickElement(webEle)
            break
    # assert I clicked on expected option successfully
    actualTextpageHeader = context.su.getTextWebElement(context.MyAccount.pageHeader)
    expect(optionToClick.lower()).to_contain(actualTextpageHeader.lower())

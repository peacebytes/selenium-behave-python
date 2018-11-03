from behave import *
from compare import expect

use_step_matcher("re")

@then('I click on "([^"]*)"')
def step_impl(context, optionToClick):
    for webEle in context.MyAccount.myaccountLinkList:
        actualTextmyaccountLink = context.su.get_text_web_element(webEle)
        if (actualTextmyaccountLink.lower()==(optionToClick.lower())):
            context.su.click_element(webEle)
            break
    # assert I clicked on expected option successfully
    actualTextpageHeader = context.su.get_text_web_element(context.MyAccount.pageHeader)
    expect(optionToClick.lower()).to_contain(actualTextpageHeader.lower())

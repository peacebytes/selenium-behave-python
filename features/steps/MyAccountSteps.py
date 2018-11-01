from behave import *
from compare import expect

use_step_matcher("re")

@then('I click on "([^"]*)"')
def step_impl(context, optionToClick):
    for webEle in context.MyAccount.myaccountLinkList:
        actualTextmyaccountLink = context.su.getTextWebElement(webEle)
        print("Found actualTextmyaccountLink: %s \n" % actualTextmyaccountLink)
        if (actualTextmyaccountLink.lower()==(optionToClick.lower())):
            context.su.clickElement(webEle)
            break
    # assert I clicked on expected option successfully
    actualTextpageHeader = context.su.getTextWebElement(context.MyAccount.pageHeader)
    print("Found actualTextpageHeader: %s \n" % actualTextpageHeader)
    expect(optionToClick.lower()).to_contain(actualTextpageHeader.lower())

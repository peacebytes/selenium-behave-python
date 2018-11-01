__author__ = 'switbe'
from selenium.webdriver.common.by import By
from .base_page_object import BasePage


class MyAccount(BasePage):

    def __init__(self, context):
        BasePage.__init__(self, context)

    locator_dictionary = {
        "myaccountWelcome": (By.CSS_SELECTOR, 'p.info-account'),
        "myaccountLinkList": (By.CSS_SELECTOR, 'ul.myaccount-link-list > li'),
        "pageHeader": (By.CSS_SELECTOR, 'h1')
    }

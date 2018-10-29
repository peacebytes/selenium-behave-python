from selenium.webdriver.common.by import By
from base_page_object import BasePage


class AutomationHomePage(BasePage):

    def __init__(self, context):
        BasePage.__init__(
            self,
            context.browser)

    locator_dictionary = {
        "sign_in": (By.LINK_TEXT, 'Sign in'),
        "contact_us": (By.LINK_TEXT, 'Contact us'),
        "sign_out": (By.LINK_TEXT, 'Sign out')
    }

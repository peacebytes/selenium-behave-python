__author__ = 'switbe'
from selenium.webdriver.common.by import By
from .base_page_object import BasePage


class LoginPage(BasePage):
    locator_dictionary = {
        "email": (By.ID, 'email'),
        "password": (By.ID, 'passwd'),
        "signin_button": (By.ID, 'SubmitLogin')
    }

    def __init__(self, context):
        BasePage.__init__(self, context)
        self.su = context.su

    def login(self,username,passwd):
        self.su.enterText(username, self.email)
        self.su.enterText(passwd, self.password)
        self.su.clickElement(self.signin_button)

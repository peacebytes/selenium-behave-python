import time
import traceback
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *

class SeleniumUtils(object):

    def __init__(self, context):
        self.timeout = context.timeout
        self.browser = context.wdriver

    def get_elements(self, *loc):
        return self.browser.find_elements(*loc)

    def find_elements_under_parent_element(self, parent_element, *loc):
        list_web_element = parent_element.find_elements(*loc)
        if len(list_web_element) == 1:
            return list_web_element[0]
        else:
            return list_web_element

    def visit(self,url):
        self.browser.get(url)

    def click_element_forcefully(self, webElement):
        webElement.click()

    def click_element(self, webElement):
        self.wait_for_web_element(webElement)
        webElement.click()

    def enter_text(self, text, webElement):
        self.wait_for_web_element(webElement)
        webElement.clear()
        webElement.send_keys(text)

    def hover(self, webElement):
        self.wait_for_web_element(webElement)
        ActionChains(self.browser).move_to_element(webElement).perform()
        # I don't like this but hover is sensitive and needs some sleep time
        time.sleep(5)

    def get_text_web_element(self, webElement):
        self.wait_for_web_element(webElement)
        return webElement.text

    def get_value_web_element(self, webElement):
        self.wait_for_web_element(webElement)
        return webElement.get_attribute('value')

    def select_option_from_select_list(self, option, webElementList):
        for webEle in webElementList:
            foundOption = self.get_text_web_element(webEle)
            if (foundOption.lower()==(option.lower())):
                self.click_element(webEle)
                break

    def wait_for_web_element(self, webElement):
        try:
            webElement = WebDriverWait(self.browser,self.timeout).until(
                EC.visibility_of(webElement)
            )
        except TimeoutException:
            traceback.print_exc()

    def wait_for_alert_then_accept(self):
        try:
            WebDriverWait(self.browser,self.timeout).until(
                EC.alert_is_present()
            )
            alert = self.browser.switch_to.alert
            alert.accept()
            self.browser.switch_to.default_content()
        except TimeoutException:
            traceback.print_exc()

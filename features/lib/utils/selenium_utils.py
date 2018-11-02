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

    def find_elements(self, *loc):
        return self.browser.find_elements(*loc)

    def find_elementsUnderParentElement(self, parentElement, *loc):
        listWebElement = parentElement.find_elements(*loc)
        if len(listWebElement) == 1:
            return listWebElement[0]
        else:
            return listWebElement

    def visit(self,url):
        self.browser.get(url)

    def clickElementForcefully(self, webElement):
        webElement.click()

    def clickElement(self, webElement):
        self.waitForWebElement(webElement)
        webElement.click()

    def enterText(self, text, webElement):
        self.waitForWebElement(webElement)
        webElement.clear()
        webElement.send_keys(text)

    def hover(self, element):
        self.waitForWebElement(webElement)
        ActionChains(self.browser).move_to_element(element).perform()
        # I don't like this but hover is sensitive and needs some sleep time
        time.sleep(5)

    def getTextWebElement(self, webElement):
        self.waitForWebElement(webElement)
        return webElement.text

    def getTextWebElementNowait(self, webElement):
        return webElement.text

    def waitForWebElement(self, webElement):
        try:
            webElement = WebDriverWait(self.browser,self.timeout).until(
                EC.visibility_of(webElement)
            )
        except(TimeoutException,StaleElementReferenceException):
            traceback.print_exc()

    def selectOptionFromSelectList(self, option, webElementList):
        for webEle in webElementList:
            foundOption = self.getTextWebElement(webEle)
            if (foundOption.lower()==(option.lower())):
                self.clickElement(webEle)
                break

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

    def find_element(self, *loc):
        try:
            element = WebDriverWait(self.browser,self.timeout).until(
                EC.presence_of_element_located(loc)
            )
        except(TimeoutException,StaleElementReferenceException):
            traceback.print_exc()

        try:
            element = WebDriverWait(self.browser,self.timeout).until(
                EC.visibility_of_element_located(loc)
            )
        except(TimeoutException,StaleElementReferenceException):
            traceback.print_exc()
        # I could have returned element, however because of lazy loading, I am seeking the element before return
        return self.browser.find_element(*loc)

    def find_elements(self, *loc):
        try:
            element = WebDriverWait(self.browser,self.timeout).until(
                EC.presence_of_element_located(loc)
            )
        except(TimeoutException,StaleElementReferenceException):
            traceback.print_exc()

        try:
            element = WebDriverWait(self.browser,self.timeout).until(
                EC.visibility_of_element_located(loc)
            )
        except(TimeoutException,StaleElementReferenceException):
            traceback.print_exc()
        # I could have returned element, however because of lazy loading, I am seeking the element before return
        return self.browser.find_elements(*loc)

    def visit(self,url):
        self.browser.get(url)

    def clickElement(self, webElement):
        try:
            webElement = WebDriverWait(self.browser,self.timeout).until(
                EC.visibility_of(webElement)
            )
        except(TimeoutException,StaleElementReferenceException):
            traceback.print_exc()
        webElement.click()

    def enterText(self, text, webElement):
        try:
            webElement = WebDriverWait(self.browser,self.timeout).until(
                EC.visibility_of(webElement)
            )
        except(TimeoutException,StaleElementReferenceException):
            traceback.print_exc()
        webElement.clear()
        webElement.send_keys(text)

    def hover(self, element):
        try:
            webElement = WebDriverWait(self.browser,self.timeout).until(
                EC.visibility_of(webElement)
            )
        except(TimeoutException,StaleElementReferenceException):
            traceback.print_exc()
        ActionChains(self.browser).move_to_element(element).perform()
        # I don't like this but hover is sensitive and needs some sleep time
        time.sleep(5)

    def getTextWebElement(self, webElement):
        try:
            webElement = WebDriverWait(self.browser,self.timeout).until(
                EC.visibility_of(webElement)
            )
        except(TimeoutException,StaleElementReferenceException):
            traceback.print_exc()
        return webElement.text

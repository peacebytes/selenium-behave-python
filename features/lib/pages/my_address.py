__author__ = 'switbe'
from selenium.webdriver.common.by import By
from .base_page_object import BasePage
class MyAddress(BasePage):

    def __init__(self, context):
        BasePage.__init__(self, context)
        self.su = context.su

    locator_dictionary = {
        "addAddressButton": (By.XPATH, '//a[@title="Add an address"]'),
        "address1": (By.ID, 'address1'),
        "city": (By.ID, 'city'),
        "id_state": (By.ID, 'id_state'),
        "postcode": (By.ID, 'postcode'),
        "id_country": (By.ID, 'id_country'),
        "phone": (By.ID, 'phone'),
        "alias": (By.ID, 'alias'),
        "submitAddressButton": (By.ID, 'submitAddress'),
        "state_options": (By.XPATH, "//*[@id='id_state']/option"),
        "country_options": (By.XPATH, "//*[@id='id_country']/option"),
        "selected_country": (By.CSS_SELECTOR, "#uniform-id_country > span"),
        "selected_state": (By.CSS_SELECTOR, "#uniform-id_state > span"),
        "addressesList": (By.CSS_SELECTOR, "div.address"),
        "addressLines": (By.CSS_SELECTOR, "ul > li")
    }

    def getAddressDetails(self, parentElement):
        return self.su.find_elementsUnderParentElement(parentElement, *self.locator_dictionary['addressLines'])

    def isAddressExisted(self, addressName):
        for webEle in self.addressesList:
            addr = self.su.getTextWebElement(self.getAddressDetails(webEle)[0])
            print("Got addr : %s \n" % addr)
            if (addr.lower()==(addressName.lower())):
                return True
        return False

    def addAddress(self, addressDetails):
        if (self.isAddressExisted(addressDetails["alias"]) is False):
            self.su.clickElement(self.addAddressButton)
            self.su.enterText(addressDetails["address1"], self.address1)
            self.su.enterText(addressDetails["city"], self.city)
            defaultState = self.su.getTextWebElement(self.selected_state)
            if (defaultState != addressDetails["state_option"]):
                self.su.clickElementForcefully(self.id_state)
                self.su.selectOptionFromSelectList(addressDetails["state_option"], self.state_options)
            self.su.enterText(addressDetails["postcode"], self.postcode)
            defaultCountry = self.su.getTextWebElement(self.selected_country)
            if (defaultCountry != addressDetails["country_option"]):
                self.su.clickElementForcefully(self.id_country)
                self.su.selectOptionFromSelectList(addressDetails["country_option"], self.country_options)
            self.su.enterText(addressDetails["phone"], self.phone)
            self.su.enterText(addressDetails["alias"], self.alias)
            self.su.clickElement(self.submitAddressButton)

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
        "submitAddressButton": (By.ID, 'submitAddressButton'),
        "state_options": (By.ID, "//*[@id='id_state']/option"),
        "country_options": (By.ID, "//*[@id='id_country']/option")
    }

    def addAddress(self, addressDetails):
        self.su.clickElement(self.addAddressButton)
        print ("addressDetails['address1']: %s \n" % addressDetails["address1"])
        self.su.enterText(addressDetails["address1"], self.address1)
        # SeleniumUtils.enterText(city, dataAddress.get("city"));
        # SeleniumUtils.clickElementForcefully(id_state);
        # for (WebElement webEle : state_options) {
        #     String foundState = SeleniumUtils.getTextWebElement(webEle).toLowerCase();
        #     if (foundState.toLowerCase().equals(dataAddress.get("state_option").toLowerCase())) {
        #         SeleniumUtils.clickElement(webEle);
        #         break;
        #     }
        # }
        # SeleniumUtils.enterText(postcode, dataAddress.get("postcode"));
        # SeleniumUtils.clickElementForcefully(id_country);
        # for (WebElement webEle : country_options) {
        #     String foundCountry = SeleniumUtils.getTextWebElement(webEle).toLowerCase();
        #     if (foundCountry.toLowerCase().equals(dataAddress.get("country_option").toLowerCase())) {
        #         SeleniumUtils.clickElement(webEle);
        #         break;
        #     }
        # }
        # SeleniumUtils.enterText(phone, dataAddress.get("phone"));
        # SeleniumUtils.enterText(alias, dataAddress.get("alias"));
        # SeleniumUtils.clickElement(submitAddressButton);
